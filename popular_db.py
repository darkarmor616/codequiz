import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Categoria, Questao, Alternativa

# Limpar dados existentes
print("Limpando banco de dados...")
Alternativa.objects.all().delete()
Questao.objects.all().delete()
Categoria.objects.all().delete()

# Criar categorias
print("Criando categorias...")
python = Categoria.objects.create(
    nome="Python",
    descricao="Questões sobre a linguagem Python",
    publicado=False  # Será publicado após adicionar 5+ questões
)

javascript = Categoria.objects.create(
    nome="JavaScript",
    descricao="Questões sobre JavaScript e programação web",
    publicado=False
)

logica = Categoria.objects.create(
    nome="Lógica de Programação",
    descricao="Questões fundamentais de lógica e algoritmos",
    publicado=False
)

# Questões de Python
print("Criando questões de Python...")

q1 = Questao.objects.create(
    categoria=python,
    pergunta="Qual é a forma correta de criar uma lista em Python?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q1, texto="lista = {1, 2, 3}", correta=False)
Alternativa.objects.create(questao=q1, texto="lista = [1, 2, 3]", correta=True)
Alternativa.objects.create(questao=q1, texto="lista = (1, 2, 3)", correta=False)
Alternativa.objects.create(questao=q1, texto="lista = <1, 2, 3>", correta=False)

q2 = Questao.objects.create(
    categoria=python,
    pergunta="Qual palavra-chave é usada para definir uma função em Python?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q2, texto="function", correta=False)
Alternativa.objects.create(questao=q2, texto="def", correta=True)
Alternativa.objects.create(questao=q2, texto="func", correta=False)
Alternativa.objects.create(questao=q2, texto="define", correta=False)

q3 = Questao.objects.create(
    categoria=python,
    pergunta="O que o método .append() faz em uma lista?",
    dificuldade="medio",
    pontos=15
)
Alternativa.objects.create(questao=q3, texto="Remove o último elemento", correta=False)
Alternativa.objects.create(questao=q3, texto="Adiciona um elemento no final", correta=True)
Alternativa.objects.create(questao=q3, texto="Ordena a lista", correta=False)
Alternativa.objects.create(questao=q3, texto="Inverte a lista", correta=False)

q4 = Questao.objects.create(
    categoria=python,
    pergunta="Qual é o resultado de: print(type([]))?",
    dificuldade="medio",
    pontos=15
)
Alternativa.objects.create(questao=q4, texto="<class 'tuple'>", correta=False)
Alternativa.objects.create(questao=q4, texto="<class 'list'>", correta=True)
Alternativa.objects.create(questao=q4, texto="<class 'dict'>", correta=False)
Alternativa.objects.create(questao=q4, texto="<class 'array'>", correta=False)

q5_python = Questao.objects.create(
    categoria=python,
    pergunta="Como você comenta uma linha em Python?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q5_python, texto="// comentário", correta=False)
Alternativa.objects.create(questao=q5_python, texto="# comentário", correta=True)
Alternativa.objects.create(questao=q5_python, texto="/* comentário */", correta=False)
Alternativa.objects.create(questao=q5_python, texto="<!-- comentário -->", correta=False)

# Questões de JavaScript
print("Criando questões de JavaScript...")

q5 = Questao.objects.create(
    categoria=javascript,
    pergunta="Qual palavra-chave declara uma variável com escopo de bloco?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q5, texto="var", correta=False)
Alternativa.objects.create(questao=q5, texto="let", correta=True)
Alternativa.objects.create(questao=q5, texto="variable", correta=False)
Alternativa.objects.create(questao=q5, texto="const (apenas)", correta=False)

q6 = Questao.objects.create(
    categoria=javascript,
    pergunta="Como você escreve um comentário de uma linha em JavaScript?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q6, texto="# comentário", correta=False)
Alternativa.objects.create(questao=q6, texto="// comentário", correta=True)
Alternativa.objects.create(questao=q6, texto="<!-- comentário -->", correta=False)
Alternativa.objects.create(questao=q6, texto="/* comentário */", correta=False)

q7 = Questao.objects.create(
    categoria=javascript,
    pergunta="Qual método converte uma string em número inteiro?",
    dificuldade="medio",
    pontos=15
)
Alternativa.objects.create(questao=q7, texto="parseInt()", correta=True)
Alternativa.objects.create(questao=q7, texto="toInteger()", correta=False)
Alternativa.objects.create(questao=q7, texto="convertInt()", correta=False)
Alternativa.objects.create(questao=q7, texto="stringToInt()", correta=False)

q8_js = Questao.objects.create(
    categoria=javascript,
    pergunta="O que é o DOM em JavaScript?",
    dificuldade="medio",
    pontos=15
)
Alternativa.objects.create(questao=q8_js, texto="Document Object Model - Representação da estrutura HTML", correta=True)
Alternativa.objects.create(questao=q8_js, texto="Data Object Method - Método de dados", correta=False)
Alternativa.objects.create(questao=q8_js, texto="Dynamic Output Module - Módulo de saída", correta=False)
Alternativa.objects.create(questao=q8_js, texto="Digital Operation Manager - Gerenciador de operações", correta=False)

q9_js = Questao.objects.create(
    categoria=javascript,
    pergunta="Qual é a forma correta de criar um array em JavaScript?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q9_js, texto="var arr = (1, 2, 3)", correta=False)
Alternativa.objects.create(questao=q9_js, texto="var arr = [1, 2, 3]", correta=True)
Alternativa.objects.create(questao=q9_js, texto="var arr = {1, 2, 3}", correta=False)
Alternativa.objects.create(questao=q9_js, texto="var arr = <1, 2, 3>", correta=False)

# Questões de Lógica
print("Criando questões de Lógica...")

q8 = Questao.objects.create(
    categoria=logica,
    pergunta="O que é um algoritmo?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q8, texto="Uma linguagem de programação", correta=False)
Alternativa.objects.create(questao=q8, texto="Sequência de passos para resolver um problema", correta=True)
Alternativa.objects.create(questao=q8, texto="Um tipo de loop", correta=False)
Alternativa.objects.create(questao=q8, texto="Um banco de dados", correta=False)

q9 = Questao.objects.create(
    categoria=logica,
    pergunta="Qual estrutura de repetição executa pelo menos uma vez?",
    dificuldade="medio",
    pontos=15
)
Alternativa.objects.create(questao=q9, texto="for", correta=False)
Alternativa.objects.create(questao=q9, texto="while", correta=False)
Alternativa.objects.create(questao=q9, texto="do-while", correta=True)
Alternativa.objects.create(questao=q9, texto="if-else", correta=False)

q10 = Questao.objects.create(
    categoria=logica,
    pergunta="O que é recursão em programação?",
    dificuldade="dificil",
    pontos=20
)
Alternativa.objects.create(questao=q10, texto="Um loop infinito", correta=False)
Alternativa.objects.create(questao=q10, texto="Uma função que chama a si mesma", correta=True)
Alternativa.objects.create(questao=q10, texto="Um tipo de variável", correta=False)
Alternativa.objects.create(questao=q10, texto="Um método de ordenação", correta=False)

q11_logica = Questao.objects.create(
    categoria=logica,
    pergunta="Qual é a complexidade de tempo de uma busca binária?",
    dificuldade="dificil",
    pontos=20
)
Alternativa.objects.create(questao=q11_logica, texto="O(n)", correta=False)
Alternativa.objects.create(questao=q11_logica, texto="O(log n)", correta=True)
Alternativa.objects.create(questao=q11_logica, texto="O(n²)", correta=False)
Alternativa.objects.create(questao=q11_logica, texto="O(1)", correta=False)

q12_logica = Questao.objects.create(
    categoria=logica,
    pergunta="O que é uma variável?",
    dificuldade="facil",
    pontos=10
)
Alternativa.objects.create(questao=q12_logica, texto="Um espaço na memória para armazenar dados", correta=True)
Alternativa.objects.create(questao=q12_logica, texto="Um tipo de função", correta=False)
Alternativa.objects.create(questao=q12_logica, texto="Um operador lógico", correta=False)
Alternativa.objects.create(questao=q12_logica, texto="Uma estrutura de repetição", correta=False)

# Publicar categorias que têm 5+ questões
print("\nPublicando categorias...")
for cat in [python, javascript, logica]:
    if cat.pode_publicar():
        cat.publicado = True
        cat.save()
        print(f"✅ {cat.nome} publicada ({cat.questoes.count()} questões)")
    else:
        print(f"❌ {cat.nome} não pode ser publicada ({cat.questoes.count()}/5 questões)")

print("\n✅ Banco de dados populado com sucesso!")
print(f"📚 {Categoria.objects.count()} categorias criadas")
print(f"❓ {Questao.objects.count()} questões criadas")
print(f"📝 {Alternativa.objects.count()} alternativas criadas")
print(f"🌐 {Categoria.objects.filter(publicado=True).count()} categorias publicadas")
