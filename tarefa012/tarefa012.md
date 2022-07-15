# Tarefa 012 - Tratamento de Exceção - 13/07/2022

1. Crie uma classe que aceite a digitação de dois números e faça a divisão entre eles exibindo seu resultado. Sua classe deve tratar as seguintes exceções:
  * _ArithmeticException_ quando ocorrer uma divisão por zero.
  * _InputMismatchException_ quando o valor informado não é numérico.

2. Crie uma classe que crie um vetor de inteiros de 10 posições. Feito isso, permita que o usuário digite valores inteiros a fim de preencher este vetor. Não implemente nenhum tipo controle referente ao tamanho do vetor, deixe que o usuário digite valores até que a entrada 0 (zero) seja digitada.

  Uma vez digitado o valor 0, o mesmo deve ser inserido no vetor e a digitação de novos elementos deve ser interrompida. Feita toda a coleta dos dados, exiba-os em tela.

  Sua classe deve tratar as seguintes exceções:
    * _ArrayIndexOutOfBoundsException_ quando o usuário informar mais que 10 valores.
    * _InputMismatchException_ quando o usuário informar um valor que não é numérico.

3. Crie uma classe chamada _Login_, que possua os atributos _usuario_ e _senha_ (do tipo String) e um método chamado fazer_login(usuario, senha), que retorna uma _boolean_. Uma exceção do tipo _LoginInvalidoException_ deve ser lançada quando o usuário ou a senha não estiverem corretos. Esta classe de exceção deve ser criada por você. O Tratamento da exceção deverá ser feito em uma classe de teste (executável).

4. Crie uma classe chamada _ContaBancaria_, que possua o atributo _saldo_ do tipo _Double_, além dos métodos _depositar(Double Valor)_ e _sacar(Double valor)_. Uma exceção do tipo _SaldoInsuficienteException_ deve ser lançada quando se deseja fazer um saque de um valor superior ao saldo disponível. Esta classe de exceção deve ser criada por você. O Tratamento da exceção deverá ser feito em uma classe de teste (executável).

**INSTRUÇÕES**
1. A entrega deve ser feita no seu repositório pessoal, utilizado para a disciplina, dentro de uma pasta chamada **tarefa012**.
2. Arquivos de configurações locais não devem ser enviados para o repositório.
3. O prazo para entrega desta tarefa é as 23h59min do dia 13/07/2022, as 23h59min.
