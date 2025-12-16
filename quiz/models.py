from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # RRN07: Nome único
    descricao = models.TextField(blank=True)
    publicado = models.BooleanField(default=False)  # RRN02: Controle de publicação
    
    class Meta:
        verbose_name_plural = "Categorias"
    
    def __str__(self):
        return self.nome
    
    def pode_publicar(self):
        """RRN02: Quiz só pode ser publicado com pelo menos 5 perguntas"""
        return self.questoes.count() >= 5
    
    def save(self, *args, **kwargs):
        # RRN07: Validar nome único
        if not self.pk:  # Novo objeto
            if Categoria.objects.filter(nome__iexact=self.nome).exists():
                raise ValidationError(f"Já existe uma categoria com o nome '{self.nome}'")
        super().save(*args, **kwargs)

class Questao(models.Model):
    DIFICULDADE_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='questoes')
    pergunta = models.TextField()
    dificuldade = models.CharField(max_length=10, choices=DIFICULDADE_CHOICES, default='medio')
    pontos = models.IntegerField(default=10)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"
        ordering = ['categoria', 'dificuldade']
    
    def __str__(self):
        return f"{self.categoria.nome} - {self.pergunta[:50]}"

class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='alternativas')
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['questao', 'texto']  # RRN09: Alternativa única por questão
    
    def __str__(self):
        return f"{self.texto[:50]} - {'Correta' if self.correta else 'Incorreta'}"
    
    def save(self, *args, **kwargs):
        # RRN01: Apenas uma alternativa correta por questão
        if self.correta:
            # Remover correta de outras alternativas desta questão
            Alternativa.objects.filter(questao=self.questao, correta=True).update(correta=False)
        super().save(*args, **kwargs)

class Pontuacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pontuacoes')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pontos_totais = models.IntegerField(default=0)
    questoes_respondidas = models.IntegerField(default=0)
    questoes_corretas = models.IntegerField(default=0)
    data_quiz = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Pontuação"
        verbose_name_plural = "Pontuações"
        ordering = ['-pontos_totais', '-data_quiz']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.pontos_totais} pontos"
    
    @property
    def percentual_acerto(self):
        if self.questoes_respondidas > 0:
            return (self.questoes_corretas / self.questoes_respondidas) * 100
        return 0
    
    @staticmethod
    def pode_fazer_quiz(usuario, categoria):
        """RRN03: Não pode refazer o mesmo quiz no mesmo dia"""
        hoje = timezone.now().date()
        tentativa_hoje = Pontuacao.objects.filter(
            usuario=usuario,
            categoria=categoria,
            data_quiz__date=hoje
        ).exists()
        return not tentativa_hoje
