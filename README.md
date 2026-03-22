# 🤖 Agente Inteligente com LangChain

Projeto desenvolvido para a disciplina de [IA APLICADA].  
**Grupo:** [Eduarda Veloso, Panmela Karen, Saíra Aguiar]

---

## 📋 Descrição

Este projeto implementa um **agente inteligente** utilizando o framework **LangChain**
integrado com modelos de linguagem do **Hugging Face**, rodando **localmente** na máquina,
sem necessidade de créditos pagos.

O agente recebe um comando em texto do usuário e retorna uma resposta gerada por um LLM
(Large Language Model).

---

## 🧱 Arquitetura do Projeto

```
Usuário digita um texto
        ↓
  PromptTemplate        ← formata o comando
        ↓
  LLM (flan-t5-base)   ← gera a resposta
        ↓
  StrOutputParser       ← limpa e retorna o texto
        ↓
  Resposta exibida ao usuário
```

---

## 📁 Estrutura de Arquivos

```
agente-langchain/
├── agente.py          # Código principal do agente
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo
```

---

## ⚙️ Como Instalar e Rodar

### Pré-requisitos
- Python 3.9 ou superior instalado
- Conexão com internet (só na primeira execução, para baixar o modelo)

### Passo 1 — Clone ou baixe o projeto
```bash
# Se tiver git:
git clone <url-do-repositorio>
cd agente-langchain

# Ou descompacte o .zip e entre na pasta pelo terminal
```

### Passo 2 — Crie um ambiente virtual (recomendado)
```bash
python -m venv venv

# Ativar no Windows:
venv\Scripts\activate

# Ativar no Mac/Linux:
source venv/bin/activate
```

### Passo 3 — Instale as dependências
```bash
pip install -r requirements.txt
```

### Passo 4 — Execute o agente
```bash
python agente.py
```

---

## 💬 Exemplo de Uso

```
==================================================
       🤖 AGENTE INTELIGENTE - LangChain
==================================================
Digite 'sair' para encerrar o programa.

Você: O que é inteligência artificial?
🤖 Agente: Inteligência artificial é a capacidade de máquinas realizarem
tarefas que normalmente exigiriam inteligência humana, como raciocínio,
aprendizado e tomada de decisões.

Você: sair
👋 Encerrando o agente. Até logo!
```

---

## 🧠 Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| **LangChain** | Framework principal do agente |
| **Hugging Face** | Repositório do modelo de linguagem |
| **google/flan-t5-base** | Modelo LLM rodando localmente |
| **Python** | Linguagem de programação |

---

## 🚀 Possíveis Extensões do Agente

- 🧠 **Memória de conversa** — o agente lembrar mensagens anteriores da mesma sessão
- 🌐 **Busca na web** — integrar ferramenta de pesquisa em tempo real
- 📄 **Leitura de documentos** — responder perguntas sobre PDFs enviados pelo usuário
- 🎙️ **Interface de voz** — entrada e saída por áudio
- 💻 **Interface gráfica** — criar uma tela visual com Gradio ou Streamlit

---

## 📚 Referências

- [Documentação LangChain](https://python.langchain.com/docs/)
- [Hugging Face Models](https://huggingface.co/models)
- [google/flan-t5-base](https://huggingface.co/google/flan-t5-base)