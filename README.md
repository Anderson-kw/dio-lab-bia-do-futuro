# Mentor Primeiro Salário 💰

Este projeto foi desenvolvido como parte do desafio **"Construa Seu Assistente Virtual Com Inteligência Artificial"** do bootcamp da DIO. 

O **Mentor Primeiro Salário** é um agente de Inteligência Artificial Generativa com uma interface web interativa, focado em democratizar a educação financeira preventiva. Seu objetivo é ajudar jovens adultos que acabaram de ingressar no mercado de trabalho a organizar o primeiro salário, evitar o endividamento precoce e iniciar a construção de uma reserva de emergência sólida.

---

## 🎯 O Problema e a Solução

A transição para a vida adulta traz o primeiro contracheque, mas raramente vem acompanhada de educação financeira. Muitos jovens caem na armadilha dos juros rotativos do cartão de crédito ou inflam o seu estilo de vida precocemente.

O **Mentor Primeiro Salário** atua como um conselheiro empático e blindado contra alucinações. Ele não recomenda investimentos de risco (como ações ou criptomoedas), focando estritamente em metodologias seguras:
*   Aplicação da regra **50-30-20** para divisão do orçamento.
*   Conscientização sobre o pagamento integral da fatura do cartão de crédito.
*   Direcionamento para produtos de liquidez diária (Tesouro Selic, CDB 100% CDI) para a construção da Reserva de Emergência.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as ferramentas mais modernas do ecossistema de IA e dados:

*   **Linguagem:** Python
*   **Interface Web:** Streamlit (para renderização reativa do front-end)
*   **LLM (Large Language Model):** Google Gemini API (modelo `gemini-3-flash-preview` via o novo SDK `google-genai`)
*   **Gestão de Variáveis:** `python-dotenv`

---

## 📂 Estrutura do Projeto

A arquitetura do projeto separa claramente a interface, a base de conhecimento estática e as documentações de avaliação:

```text
assistente-financeiro-ia/
├── data/
│   ├── regras_financeiras.md      # Cartilha rigorosa de finanças para a IA
│   ├── perfil_usuario.json        # Dados mockados do cliente em sessão
│   └── cenarios_orcamento.json    # Faixas salariais para context awareness
├── docs/
│   ├── 01-documentacao-agente.md  # Arquitetura e persona do agente
│   ├── 02-base-conhecimento.md    # Estratégia de integração de dados
│   ├── 03-prompts.md              # System Prompts e regras de restrição
│   ├── 04-metricas.md             # Casos de uso e testes de alucinação
│   └── 05-pitch.md                # Roteiro de apresentação da solução
├── .gitignore                     # Proteção de credenciais
├── requirements.txt               # Dependências do projeto
└── app.py                         # Código principal (Back-end + UI Streamlit)
```

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para testar o assistente localmente na sua máquina:

**1. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/assistente-financeiro-ia.git](https://github.com/seu-usuario/assistente-financeiro-ia.git)
cd assistente-financeiro-ia
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente:**
Crie um arquivo chamado `.env` na raiz do projeto e insira a sua chave de API do Google AI Studio:
```env
GEMINI_API_KEY=sua_chave_secreta_aqui
```

**5. Inicie a aplicação:**
```bash
python -m streamlit run app.py
```
A interface será aberta automaticamente no seu navegador padrão, pronta para uso!
