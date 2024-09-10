# sistema-bancario
Desafio de projeto da DIO

Descrição: Este projeto implementa um sistema bancário simples que permite ao usuário realizar operações básicas de uma conta bancária por meio de um menu interativo. O sistema oferece funcionalidades para depósitos, saques e consulta de extrato.

Funcionalidades:

Depósito:

O usuário pode depositar um valor em sua conta.
O valor depositado deve ser positivo, e se for válido, o saldo é atualizado e o histórico de depósitos é registrado.
Caso o valor seja inválido (menor ou igual a zero), o sistema alerta o usuário para inserir um valor maior.
Saque:

O usuário pode realizar saques, desde que o valor do saque não exceda o saldo disponível.
É possível fazer no máximo 3 saques. Caso o usuário tente realizar mais saques, o sistema emitirá uma mensagem de erro.
O valor do saque deve ser positivo e menor que o saldo; caso contrário, a operação não é realizada.
Extrato:

O usuário pode visualizar o extrato de sua conta, que inclui um histórico de todos os depósitos e saques realizados.
Se não houver movimentações, o sistema informa ao usuário que não foram realizadas operações.
Interface:

O sistema exibe um menu interativo com opções para depósito, saque, extrato e sair.
O usuário interage com o sistema por meio de comandos simples (A, B, C, X) para selecionar a operação desejada.
Funcionamento: O sistema utiliza uma abordagem baseada em loops e condicionais para gerenciar as operações bancárias. A interação com o usuário é feita por meio de inputs e mensagens impressas no console. O código é estruturado em funções para facilitar a modularização e a manutenção.

Exemplo de uso:

O usuário escolhe a operação desejada.
Para depósito, insere o valor e o saldo é atualizado.
Para saque, insere o valor e verifica-se se o saldo e o limite de saques permitem a operação.
Para extrato, o histórico de movimentações e o saldo atual são exibidos.
