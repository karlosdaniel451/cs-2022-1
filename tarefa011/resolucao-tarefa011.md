## Padrões de codificação

Um padrão de codificação é um conjunto de convenções, guias e padronizações que pode ser seguido ao
escrever código em alguma linguagem de programação ou marcação.

Padrões de codificação, ou em inglês *Code Style Guides*, podem ser definidos para organizações
inteiras, times ou até mesmo projetos específicos. Dentre os tópicos cobertos por tais padrões,
estão:

- Indentação.
- Espaços em brancos.
- Nomenclatura de variáveis, funções, métodos, classes e constantes.
- Nomenclatura e organização de arquivos de código-fonte ou configuração.
- Comentários.
- Uso de chaves e de ponto e vírgulas.
- Número máximo de caracteres por linha.
- Uso de exceções.
- Uso de variáveis globais e constantes.

A definição e uso de padrões de codificação são altamente indicados em projetos com muito
colaboradores, como projetos *open-source*, ou que passarão por diversas modificações ao longo de
seu ciclo de vida, como os projetos ágeis desenvolvidos em incrementos constantes.

Alguns exemplos de padrões de codificações são:

- [Google Style Guides](https://google.github.io/styleguide/). Define padrões de codificação para diversas linguagens a ser seguido nos projetos open-source da Google.
- [Linux Kernel Style Guide](https://www.kernel.org/doc/html/v4.10/process/coding-style.html). Descreve um estilo codificação preferido para o projeto do kernel Linux.
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/). Define convenções de codificação ao se utilizar a biblioteca padrão do Python. 
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/). Conjunto de aforismos que propões uma filosofia para projetar e escrever programas em Python focados em legibilidade e simplicidade.

### Talk is cheap. Show me the code

Para exemplificar melhor o conceito de padrões de codificação, veremos uma aplicação real com alguns códigos em Python utilizando-se da PEP 8 e de algumas ferramentas que facilitam a adoção de de tal padrão.

A ferramenta [pycodestyle](https://pypi.org/project/pycodestyle/) pode ser utilizada para checar se
determinado código adere às convenções definidas na PEP 8 e pode ser instalada com o seguinte comando:

```pip install pycodestyle```

Por exemplo, digamos que a convenção de apenas uma importação de módulo por linha foi violada no seguinte trecho de código:

```python
import os, sys
```

Para checar violações da PEP 8 e apontar onde tais violações ocorreram, basta digitar:

```pycodestyle --show-source --show-pep8 testsuite/<source_file_to_be_checked>```

Neste caso, a saída do pycodestyle seria a seguinte:

```
violoation-of-single-importation-per-line.py:1:10: E401 multiple imports on one line
import os, sys
         ^
    Place imports on separate lines.

    Okay: import os\nimport sys
    E401: import sys, os

    Okay: from subprocess import Popen, PIPE
    Okay: from myclas import MyClass
    Okay: from foo.bar.yourclass import YourClass
    Okay: import myclass
    Okay: import foo.bar.yourclass
```

Além do pycodestyle, outra ferramenta bastante útil quanto à aderência da PEP 8 é a [autoep8](https://pypi.org/project/autopep8/), podendo ser instalada com o comando:

```pip install autopep8```

O autopep8 automatiza a formatação de códigos-fonte em Python de acordo com a PEP 8 e utiliza o pycodestyle para determinar violações deste padrão.

Por exemplo, digamos que tenhamos o seguinte código com múltiplas violações da PEP 8:

```python
import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)
def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));
class Example3(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
                    return (sys.path, some_string)

```

Podemos automaticamente corrigir tal código-fonte quanto a PEP 8 com o comando:

```autopep8 --in-place --aggressive --aggressive <source_file_to_be_formatted>```

Após a execução deste comando, o arquivo a ser formatado teria o seguinte código-fonte:

```python
import math
import sys


def example1():
    # This is a long comment. This should be wrapped to fit within 72
    # characters.
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        'long': 'Long code lines should be wrapped within 79 characters.',
        'other': [
            math.pi,
            100,
            200,
            300,
            9876543210,
            'This is a long string that goes on'],
        'more': {
            'inner': 'This whole logical line should be wrapped.',
            some_tuple: [
                1,
                20,
                300,
                40000,
                500000000,
                60000000000000000]}}
    return (some_tuple, some_variable)


def example2(): return ('' in {'f': 2}) in {'has_key() is deprecated': True}


class Example3(object):
    def __init__(self, bar):
        # Comments should have a space after the hash.
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
            return (sys.path, some_string)

```

### Referências

- [Google Style Guides](https://google.github.io/styleguide/).
- [Linux Kernel Style Guide](https://www.kernel.org/doc/html/v4.10/process/coding-style.html).
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/).
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/).
- [TABLELESS - Introdução aos padrões de codificação](https://tableless.com.br/introducao-a-padroes-de-codificacao/)
- [The Hitchhiker's Guide to Python - Code Style](https://docs.python-guide.org/writing/style/).
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/).
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/).
- [pycodestyle](https://pypi.org/project/pycodestyle/).
- [autopep8](https://pypi.org/project/autopep8/).


## Padrão Reflexão

**Reflexão**, em inglês *Reflection*, é um padrão arquitetural que fornece um mecanismo para mudar as propriedades e
comportamentos de um programa dinamicamente, isto é, em tempo de execução. Neste padrão, a aplicação é dividia logicamente
em dois níveis:

- **Meta level**: fornece informações sobre o propriedades da aplicação em tempo de execução.
- **Base level**: fornece a lógica da aplicação e é construída sobre o meta level de modo que responda às mudanças ocorridas em tal nível.

Um conceito necessário para a reflexão é a **Introspecção (Introspection)**, no qual é possível ler informações sobre a
aplicação em tempo real. A reflexão vai um passo além, permitindo também alterar tal informações.

O padrão reflexão é geralmente utilizado por programas e bibliotecas que precisam examinar e alterar suas propriedades e
comportamento em tempo de execução, como a **Java Virtual Machine (JVM)** e ferramentas de testes automatizados e debugging. Introspecção e, principalmente a reflexão, são técnicas e padrões considerados como mais avançados e devem ser
utilizados com cuidado e quando se entende por completo os fundamentos da linguagem em questão.

### Talk is cheap. Show me the code

Em Python, a forma mais simples de obter informação sobre um objeto em tempo de execução é invocando o método `type()`.
Veja que tal método permite apenas a introspecção, já que só permite ler, mas não alterar, o tipo de um objeto.

Exemplos:

```python
>>> type(1)
<class 'int'>

>>> type(1.0)
<class 'float'>

>>> type(int)
<class 'type'>

>>> type([])
<class 'list'>

>>> type(type)
<class 'type'>
```
Além disso, o método `isinstance()` pode ser usado para checar se um objeto é instância de uma determinada classe:

```python
>>> isinstance(1, int)
True

>>> isinstance(1.0, float)
True

>> isinstance(int, type)
True

>> isinstance([], list)
True

>> isinstance(type, type)
True
```

Outras funções úteis para obter informações sobre objetos no Python são:

- `hasattr()`: Checa se um objeto tem um determinado atributo.
- `id()`: Obtém um ID unique de um objeto.
- `dir()`: Obtém uma lista contendo todos os atributos e métodos de um objeto.
- `vars()`: Obtém um dicionário de todas as variáveis de instância de um objeto
- `callable()`: Checa se um objeto é um *callable*

Se for necessário fazer uma instrospecção mais avançada, é possível utilizar o módulo built-in do Python [inspect](https://docs.python.org/3/library/inspect.html).

Até o momento, só foi mostrado como realizar a introspecção no Python, ou seja, ler informações sobre objetos em tempo de
execução. Porém, tal linguagem também permite alterar essas informações dinamicamente, alcançando assim a reflexão.

Por exemplo, é possível adicionar atributos em objetos dinamicamente:

```python
>>> class A:
    pass

>>> A.x = 1

>>> a = A()

>>> a.y = 2

>>> a.y
2

>>> a.x
1
```
Por fim, também é possível adicionar métodos dinamicamente, através da função `setattr()`:

```python
>>> def init(self):
    self.x = 1

>>> class A:
    pass

>>> setattr(A, '__init__', init)

>>> a = A()

>>> a.x
1
```

### Referências

- [Reflection Architectural Pattern](http://software-pattern.org/Reflection).
- [Understanding Reflection](https://www.oreilly.com/library/view/pattern-oriented-software-architecture/9781119963998/chap16-sec001.html).
- [Python Reflection and Introspection](https://betterprogramming.pub/python-reflection-and-introspection-97b348be54d8).


## Programação defensiva
TODO
