"""
Agente Inteligente com LangChain + Hugging Face
Disciplina: [Nome da Disciplina]
Grupo: [Nome dos integrantes]
"""

from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 256,
        "temperature": 0.7,
        "do_sample": True,
    },
)

print("✅ Modelo carregado com sucesso!\n")

# ─────────────────────────────────────────────
# 2. DEFINE O TEMPLATE DE PROMPT
# ─────────────────────────────────────────────
template = PromptTemplate(
    input_variables=["comando"],
    template=(
        "Você é um assistente inteligente e prestativo. "
        "Responda em português de forma clara e objetiva.\n\n"
        "Usuário: {comando}\n"
        "Assistente:"
    ),
)

# ─────────────────────────────────────────────
# 3. MONTA A CHAIN (pipeline do agente)
# ─────────────────────────────────────────────
chain = template | llm | StrOutputParser()

# ─────────────────────────────────────────────
# 4. LOOP PRINCIPAL DO CHATBOT
# ─────────────────────────────────────────────
def rodar_agente():
    print("=" * 50)
    print("       🤖 AGENTE INTELIGENTE - LangChain")
    print("=" * 50)
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        comando = input("Você: ").strip()

        if not comando:
            print("⚠️  Por favor, digite algum comando.\n")
            continue

        if comando.lower() in ["sair", "exit", "quit"]:
            print("\n👋 Encerrando o agente. Até logo!")
            break

        print("🤖 Agente: ", end="", flush=True)
        resposta = chain.invoke({"comando": comando})
        print(resposta)
        print()


if __name__ == "__main__":
    rodar_agente()