
# Processamento de Requisições de Peças

A arquitetura foi projetada para otimizar a entrega de peças por meio de um robô, levando em consideração a singularidade do robô em ação. Para evitar conflitos e garantir a eficiência no atendimento das requisições, adotamos um sistema baseado em fila. Aqui está uma visão detalhada de como as requisições de peças são processadas:

## 1. **Recebimento da Requisição**

Quando um técnico solicita uma peça, a requisição é imediatamente captada pelo sistema. Essa solicitação contém informações essenciais, como o identificador do técnico e detalhes da peça desejada.

## 2. **Verificação da Disponibilidade**

Antes de qualquer ação ser tomada pelo robô, o sistema verifica a disponibilidade da peça solicitada. Isso é feito consultando a tabela `Tool` no banco de dados:

- Se a peça **não estiver disponível**, o sistema informará o técnico, e a requisição será encerrada.
  
- Se a peça **estiver disponível**, o sistema continuará a processar a requisição.

## 3. **Processamento Baseado em Fila**

A fim de garantir que múltiplas requisições não causem conflitos ou sobrecarreguem o robô:

- A requisição atual entra em uma **fila de espera**. 
- Se não houver outras requisições sendo processadas, esta requisição é imediatamente atendida.
  
- Se houver uma requisição em andamento, as requisições subsequentes ficarão em espera (stand by) até que a requisição anterior seja concluída.

## 4. **Movimento do Robô**

Uma vez que a requisição esteja pronta para ser processada:

- O sistema recupera as coordenadas de localização da peça solicitada (usando os campos `location_x`, `location_y` e `location_name` da tabela `Tool`).
  
- O robô, então, se movimenta até o local especificado para recuperar a peça.

## 5. **Conclusão da Requisição**

Após o robô concluir a tarefa:

- A peça é marcada como "retirada" ou seu número em estoque é decrementado.
  
- O técnico é notificado de que a peça foi recuperada e está a caminho.
  
- A próxima requisição na fila (se houver) começa a ser processada.

