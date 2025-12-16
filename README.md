# 🎯 CodeQuiz - Sistema de Quiz de Programação

**Versão 2.0** - Com todas as Regras de Negócio implementadas

Sistema educacional desenvolvido em Django para estudantes de programação testarem seus conhecimentos.

---

## ✨ Funcionalidades

### Para Usuários
- ✅ Sistema de registro e login
- ✅ Categorias de programação (Python, JavaScript, Lógica)
- ✅ Quizzes com múltipla escolha
- ✅ Feedback imediato nas respostas
- ✅ Sistema de pontuação
- ✅ Ranking competitivo
- ✅ **NOVO:** Bloqueio de quiz repetido no mesmo dia

### Para Administradores
- ✅ Painel Django Admin completo
- ✅ CRUD de Categorias, Questões e Alternativas
- ✅ **NOVO:** Validação de 5 questões mínimas para publicar
- ✅ **NOVO:** Verificação automática de nome único
- ✅ **NOVO:** Status "Pode Publicar?" no admin
- ✅ Visualização de pontuações dos usuários

---

## 🚀 Como Executar

### 1. Criar ambiente virtual
```bash
python -m venv venv
```

### 2. Ativar ambiente
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar Django
```bash
pip install django
```

### 4. Aplicar migrations
```bash
python manage.py migrate
```

### 5. Popular banco de dados
```bash
python popular_db.py
```

### 6. Iniciar servidor
```bash
python manage.py runserver
```

### 7. Acessar
- **Site:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
  - Usuário: `admin`
  - Senha: `admin123`

---

## 🛡️ Regras de Negócio Implementadas

✅ RRN01: Apenas uma alternativa correta por questão  
✅ RRN02: Quiz só publicado com 5+ questões  
✅ RRN03: Bloqueio de quiz repetido no mesmo dia  
✅ RRN04: Cálculo automático de pontuação  
✅ RRN05: Apenas admin remove perguntas  
✅ RRN06: Todas questões devem ser respondidas  
✅ RRN07: Nome único para categorias  
✅ RRN08: Tema obrigatório  
✅ RRN09: Alternativa única por questão  
✅ RRN10: Autenticação obrigatória para gestão  

---

## 📊 Dados Incluídos

- 3 categorias (Python, JavaScript, Lógica)
- 15 questões (5 por categoria)
- 60 alternativas
- 1 usuário admin

---

## 🔧 Tecnologias

- Python 3.14.2
- Django 6.0
- SQLite3
- HTML5/CSS3/JavaScript

---

**Desenvolvido para Engenharia de Software**  
**Gabriel Corrêa Simões - Dezembro 2025**
