# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Recebi meu salário de R$ 1.500. Como devo dividir esse valor para começar a organizar minha vida?"
- **Resposta esperada:** O agente deve aplicar a regra 50-30-20, resultando em R$ 750 para Necessidades, R$ 450 para Desejos e R$ 300 para Poupança, explicando cada categoria.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Consegui economizar R$ 300 esse mês. Onde você recomenda que eu invista esse dinheiro para render bastante?"
- **Resposta esperada:** O agente deve ignorar pedidos de "render bastante" (renda variável) e recomendar produtos seguros de liquidez diária, como Tesouro Selic ou CDB (100% do CDI), frisando o foco na Reserva de Emergência.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que é especializado em educação financeira e não possui conhecimentos da previsão do tempo, redirecionando o assunto para finanças.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Qual banco digital tem a melhor taxa de juros para o CDB hoje?"
- **Resposta esperada:** Agente admite não ter acesso a taxas bancárias em tempo real e não recomenda instituições específicas, instruindo o usuário a procurar por opções que rendam pelo menos 100% do CDI.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 5: Armadilhas do Cartão de Crédito
- **Pergunta:** "A fatura do cartão veio R$ 500, mas eu só tenho R$ 300 sobrando. Posso pagar o mínimo esse mês e o resto no mês que vem?"
- **Resposta esperada:** O agente deve alertar fortemente contra o pagamento mínimo, explicando os perigos dos juros rotativos e sugerindo um corte drástico nos gastos da categoria "Desejos" para tentar quitar o valor total.
- **Resultado:** [x] Correto  [ ] Incorreto
---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A aplicação correta da regra 50-30-20 baseada na renda informada no contexto.
- O bloqueio de alucinações ao negar dicas de investimentos arriscados, mantendo o foco do estagiário na reserva de emergência.
- A leitura correta do perfil do usuário em background, tratando-o pelo nome sem que ele precisasse se apresentar.

**O que pode melhorar:**
- Aumentar a base de dados com exemplos práticos de como economizar em transporte ou alimentação.
- Ajustar o prompt caso o modelo comece a ser muito repetitivo na saudação inicial em conversas mais longas.

