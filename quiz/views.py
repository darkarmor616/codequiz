from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Categoria, Questao, Alternativa, Pontuacao
import random

def home(request):
    # RRN02: Mostrar apenas categorias publicadas com 5+ questões
    categorias = Categoria.objects.filter(publicado=True)
    return render(request, 'quiz/home.html', {'categorias': categorias})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/registro.html', {'form': form})

@login_required
def iniciar_quiz(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    
    # RRN03: Verificar se usuário já fez o quiz hoje
    if not Pontuacao.pode_fazer_quiz(request.user, categoria):
        messages.warning(request, 'Você já realizou este quiz hoje! Tente novamente amanhã. ⏰')
        return redirect('home')
    
    # RRN02: Verificar se categoria tem pelo menos 5 questões
    questoes = list(categoria.questoes.all())
    if len(questoes) < 5:
        messages.warning(request, 'Esta categoria ainda não possui questões suficientes (mínimo 5).')
        return redirect('home')
    
    if not questoes:
        messages.warning(request, 'Esta categoria ainda não possui questões.')
        return redirect('home')
    
    # Embaralhar questões
    random.shuffle(questoes)
    
    # Armazenar IDs das questões na sessão
    request.session['questoes_ids'] = [q.id for q in questoes]
    request.session['questao_atual'] = 0
    request.session['pontos'] = 0
    request.session['corretas'] = 0
    request.session['categoria_id'] = categoria_id
    
    return redirect('questao')

@login_required
def questao(request):
    questoes_ids = request.session.get('questoes_ids', [])
    questao_atual = request.session.get('questao_atual', 0)
    
    if not questoes_ids or questao_atual >= len(questoes_ids):
        return redirect('resultado')
    
    questao = Questao.objects.get(id=questoes_ids[questao_atual])
    alternativas = list(questao.alternativas.all())
    random.shuffle(alternativas)
    
    total_questoes = len(questoes_ids)
    
    context = {
        'questao': questao,
        'alternativas': alternativas,
        'questao_numero': questao_atual + 1,
        'total_questoes': total_questoes,
        'pontos': request.session.get('pontos', 0),
    }
    
    return render(request, 'quiz/questao.html', context)

@login_required
def responder(request, alternativa_id):
    if request.method != 'POST':
        return redirect('home')
    
    alternativa = get_object_or_404(Alternativa, id=alternativa_id)
    
    # Verificar resposta
    if alternativa.correta:
        request.session['pontos'] = request.session.get('pontos', 0) + alternativa.questao.pontos
        request.session['corretas'] = request.session.get('corretas', 0) + 1
        messages.success(request, 'Resposta correta! 🎉')
    else:
        messages.error(request, f'Resposta incorreta. A correta era: {alternativa.questao.alternativas.get(correta=True).texto}')
    
    # Próxima questão
    request.session['questao_atual'] = request.session.get('questao_atual', 0) + 1
    
    return redirect('questao')

@login_required
def resultado(request):
    pontos = request.session.get('pontos', 0)
    corretas = request.session.get('corretas', 0)
    questoes_ids = request.session.get('questoes_ids', [])
    categoria_id = request.session.get('categoria_id')
    
    total_questoes = len(questoes_ids)
    percentual = (corretas / total_questoes * 100) if total_questoes > 0 else 0
    
    # Salvar pontuação
    if categoria_id:
        categoria = Categoria.objects.get(id=categoria_id)
        Pontuacao.objects.create(
            usuario=request.user,
            categoria=categoria,
            pontos_totais=pontos,
            questoes_respondidas=total_questoes,
            questoes_corretas=corretas
        )
    
    # Limpar sessão
    for key in ['questoes_ids', 'questao_atual', 'pontos', 'corretas', 'categoria_id']:
        request.session.pop(key, None)
    
    context = {
        'pontos': pontos,
        'corretas': corretas,
        'total': total_questoes,
        'percentual': round(percentual, 1),
    }
    
    return render(request, 'quiz/resultado.html', context)

def ranking(request):
    pontuacoes = Pontuacao.objects.select_related('usuario', 'categoria').all()[:50]
    
    context = {
        'pontuacoes': pontuacoes,
    }
    
    return render(request, 'quiz/ranking.html', context)
