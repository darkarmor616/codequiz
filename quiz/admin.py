from django.contrib import admin
from .models import Categoria, Questao, Alternativa, Pontuacao

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 4
    max_num = 5  # Máximo 5 alternativas por questão

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'total_questoes', 'publicado', 'pode_publicar_status']
    search_fields = ['nome']
    list_filter = ['publicado']
    
    def total_questoes(self, obj):
        return obj.questoes.count()
    total_questoes.short_description = 'Total de Questões'
    
    def pode_publicar_status(self, obj):
        return '✅ Sim' if obj.pode_publicar() else '❌ Não (mín. 5 questões)'
    pode_publicar_status.short_description = 'Pode Publicar?'
    
    def save_model(self, request, obj, form, change):
        # RRN02: Validar publicação
        if obj.publicado and not obj.pode_publicar():
            from django.contrib import messages
            messages.error(request, 'Não é possível publicar! A categoria precisa ter pelo menos 5 questões.')
            obj.publicado = False
        super().save_model(request, obj, form, change)

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ['pergunta_resumida', 'categoria', 'dificuldade', 'pontos', 'total_alternativas', 'criado_em']
    list_filter = ['categoria', 'dificuldade', 'criado_em']
    search_fields = ['pergunta']
    inlines = [AlternativaInline]
    
    def pergunta_resumida(self, obj):
        return obj.pergunta[:50] + '...' if len(obj.pergunta) > 50 else obj.pergunta
    pergunta_resumida.short_description = 'Pergunta'
    
    def total_alternativas(self, obj):
        return obj.alternativas.count()
    total_alternativas.short_description = 'Alternativas'

@admin.register(Pontuacao)
class PontuacaoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'categoria', 'pontos_totais', 'questoes_corretas', 
                    'questoes_respondidas', 'percentual_acerto', 'data_quiz']
    list_filter = ['categoria', 'data_quiz']
    search_fields = ['usuario__username']
    readonly_fields = ['usuario', 'categoria', 'pontos_totais', 'questoes_respondidas', 
                       'questoes_corretas', 'data_quiz']
    
    def has_add_permission(self, request):
        return False
