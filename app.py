import streamlit as st
from google import genai
from google.genai import types
import json
import os
from dotenv import load_dotenv

# ==========================================
# 1. Configurações Iniciais e Autenticação
# ==========================================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Instancia o cliente da nova biblioteca
client = genai.Client(api_key=API_KEY)

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Mentor Primeiro Salário",
    page_icon="💰",
    layout="centered"
)

# ==========================================
# 2. Funções de Carga de Dados
# ==========================================
@st.cache_data
def carregar_base_conhecimento() -> str:
    """Carrega as regras financeiras em Markdown."""
    try:
        with open("data/regras_financeiras.md", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Erro: Base de conhecimento não encontrada."

@st.cache_data
def carregar_perfil_usuario() -> dict:
    """Carrega o perfil financeiro atual do usuário."""
    try:
        with open("data/perfil_usuario.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# ==========================================
# 3. Inicialização de Estado (Session State)
# ==========================================
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {"role": "assistant", "content": "Olá! Sou o Mentor Primeiro Salário. Como posso ajudar a organizar suas finanças hoje?"}
    ]

# Configuração do novo SDK do Google
if "chat" not in st.session_state:
    regras = carregar_base_conhecimento()
    perfil = carregar_perfil_usuario()
    
    instrucoes_sistema = f"""
    Você é o Mentor Primeiro Salário, um educador financeiro empático e direto.
    
    BASE DE CONHECIMENTO (Sua única fonte de verdade):
    {regras}
    
    DADOS DO USUÁRIO ATUAL:
    - Nome: {perfil.get('usuario', {}).get('nome', 'Usuário')}
    - Renda Líquida: R$ {perfil.get('usuario', {}).get('renda_mensal_liquida', 0)}
    - Saldo Disponível: R$ {perfil.get('saldo_em_conta', 0)}
    
    DIRETRIZES:
    1. Nunca recomende ativos de renda variável.
    2. Aplique a regra 50-30-20 em simulações de orçamento.
    3. Seja cordial e explique os cálculos passo a passo.
    4. Se não souber algo, redirecione para a base de conhecimento.
    """
    
    # Nova forma de passar o system prompt
    config = types.GenerateContentConfig(
        system_instruction=instrucoes_sistema,
    )
    
    # Inicia o chat apontando para o modelo gratuito
    st.session_state.chat = client.chats.create(
        model="models/gemini-3.5-flash",
        config=config
    )

# ==========================================
# 4. Interface Gráfica (UI)
# ==========================================
with st.sidebar:
    st.title("📊 Painel do Usuário")
    perfil_dados = carregar_perfil_usuario()
    
    if perfil_dados:
        usuario = perfil_dados.get("usuario", {})
        st.write(f"**Nome:** {usuario.get('nome')}")
        st.write(f"**Fase:** {usuario.get('fase_profissional')}")
        st.write(f"**Renda Mensal:** R$ {usuario.get('renda_mensal_liquida')}")
        st.write(f"**Saldo Atual:** R$ {perfil_dados.get('saldo_em_conta')}")
        st.divider()
        st.write("🎯 **Objetivo Principal:**")
        st.info(usuario.get('objetivo_principal'))
    else:
        st.warning("Dados do usuário não carregados.")

st.title("Mentor Primeiro Salário 💰")
st.markdown("O seu assistente de educação financeira.")

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt_usuario := st.chat_input("Digite sua dúvida financeira..."):
    
    st.session_state.mensagens.append({"role": "user", "content": prompt_usuario})
    with st.chat_message("user"):
        st.markdown(prompt_usuario)
        
    with st.chat_message("assistant"):
        with st.spinner("Analisando suas finanças..."):
            try:
                # Nova sintaxe para enviar a mensagem
                resposta = st.session_state.chat.send_message(prompt_usuario)
                texto_resposta = resposta.text
                
                st.markdown(texto_resposta)
                st.session_state.mensagens.append({"role": "assistant", "content": texto_resposta})
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar a resposta: {e}")