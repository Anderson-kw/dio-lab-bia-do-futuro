# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `regras_financeiras.md` | Markdown | Cartilha contendo os pilares de educação financeira (Regra 50-30-20, uso do cartão de crédito, reserva de emergência). |
| `perfil_usuario.json` | JSON | Armazenar o estado atual do usuário na sessão (renda líquida mensal, valor das despesas fixas e objetivos). |
| `cenarios_orcamento.json` | JSON | Modelos de distribuição de gastos pré-calculados para faixas salariais iniciais (ex: R$ 1.200 a R$ 3.000) para basear as simulações. |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram criados do zero para refletir especificamente o perfil de um jovem adulto. Em vez de utilizar portfólios complexos de investimentos ou históricos de transações extensos, o arquivo perfil_usuario.json foi simplificado para conter apenas a Renda Mensal Líquida, Gastos Fixos Estimados (como transporte, alimentação e internet) e o Saldo Inicial. O arquivo de regras (regras_financeiras.md) foi formatado em linguagem simples, removendo jargões de mercado para evitar que a IA utilize uma linguagem muito técnica na resposta.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

A leitura dos arquivos estáticos (regras_financeiras.md e cenarios_orcamento.json) é feita na inicialização da aplicação, podendo ser processada nativamente via módulo fs em uma API Node.js com TypeScript, ou carregada em um serviço caso o backend seja estruturado em Java com Spring Boot. O perfil do usuário (perfil_usuario.json) é mantido em memória durante a sessão ou atualizado em um banco de dados leve.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

As regras universais (como o conceito do 50-30-20 e o funcionamento do cartão de crédito) são injetadas diretamente no System Prompt no momento em que o modelo é instanciado, servindo como a fonte de verdade imutável. Já os dados do perfil_usuario.json são consultados dinamicamente e concatenados ao prompt de cada nova interação do usuário, garantindo que o agente tenha o contexto matemático atualizado para gerar os conselhos.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
[INSTRUÇÕES DO SISTEMA]
Você é o Mentor Primeiro Salário. Aplique a regra 50-30-20 para orientar o usuário e alerte sobre o pagamento integral da fatura do cartão. Não recomende investimentos de risco.

[CONTEXTO DO USUÁRIO]
Dados do Cliente:
- Nome: Lucas
- Fase: Primeiro Emprego (Estágio)
- Renda Líquida Mensal: R$ 1.500,00
- Foco atual: Montar reserva de emergência

Últimas despesas informadas:
- 05/07: Bilhete de Transporte - R$ 150,00
- 06/07: Lanche/Alimentação - R$ 80,00
- 08/07: Assinaturas de Streaming - R$ 60,00

[MENSAGEM DO USUÁRIO]
"Recebi meu salário hoje, paguei essas contas acima e sobrou R$ 1.210. Quanto disso eu devo guardar e quanto posso gastar no final de semana?"
...
```
