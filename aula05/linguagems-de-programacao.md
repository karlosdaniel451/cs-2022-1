# Linguagens de programação

## Scala

### Características gerais:

- Criada em 2004 por Martin Odersky na École Polytechnique Fédérale de Lausannne, na Suiça.

- A linguagem foi projetada visando ser concisa e resolver alguns dos problemas do Java apontados por críticos da linguagem na época.

- É compilada e interpretada, fortemente tipada, de propósito geral e com suporte tanto à programação funcional como à orientação a objetos.

- A linguagem fornece interoperabilidade com o Java, isso significa que o código-fonte de Scala, num arquivo .scala ou sc., é compilado
bytecode que, por sua vez, é executado pela JVM.

- Scala fornece um melhor suporte à programação funcional do que o Java, incluindo imutabilidade, lazy evaluation e pattern matching.
Outras características suportadas são: sobrecarga de operadores, parâmetros opcionais, parâmetros nomeados e strings cruas.


## Rust

### Características gerais:

- Criada em 2010 num projeto da Mozilla liderado por Graydon Hoare.

- A linguagem Rust foi projetada visando desempenho, confiabilidade e concorrência.

- É compilada, fortemente tipada, de propósito geral (mas com foco em programas de sistemas) multi-paradigma (funcional e estruturada).

- A linguagem pode ser considerada como uma alternativa mais moderna confiável em relação a linguagens como C e C++, principalmente por
ser projetada para evitar erros relacionados a dereferência de ponteiros nulos e memória compartilhada em programação multithread.
Para isso, o Rust não permite ponteiros (referências) nulao, dangling pointers e nem data races.

- A linguagem não possui um garbage coletor e o gerenciamento de memória é feito a partir do conceito de empréstimos e ownership.


## Python

- Criado em 1991 por Guido van Rossum.

- A linguagem foca em simplicidade, redigibilidade e produtividade.

- É compilada e interpretada, suporta programação orientada a objetos, funcional e estruturada e dinamicamente tipada com duck typing, mas com tipagem
gradual a partir da versão 3.5

- Devido a sua simplicidade e extensa comunidade e ecossitema de bibliotecas, a linguagem é utilizada em diversas áreas diferentes, como
desenvolvimento web, data science e análise de dados, inteligência artificial, simulações computacionais, estatística e automação.

- Alguns dos recursos fornecidos pela linguagem são: list comprehension, parâmetros opcionais e com valores padrão, passagem de parâmetros por nome,
patterm matching, gerenciamento de memória automático, programação concorrente e assíncrona e generics.


## Java

- Criado em 1995 num projeto da Sun Microsystems (comprada pela Oracle em 2010) liderado por James Gosling.

- A linguagem é focada em portabilidade, robustez e segurança.

- É compilada e interpretada, fortemente e estaticamente tipada, imperativa, com alguns recursos de programação funcional, mas com foco
maior em orientação a objetos.

- A linguagem possui tanto a fase de compilação como interpretação. Na primeira, código-fonte em Java (.java) é convertido para bytecode (.class) que,
por sua vez, é interpretado (executado) pela Java Virtual Machine (JVM).

- A linguagem é extensamente utilizada em aplicações corporativas, Web e Desktop.


## Aprofundando sobre o Python

A linguagem Python,

Os tipos de dados básicos do Python são: inteiros, ponto flutuante, números complexos, boolean e os tipos de *container*, ou compostos, como
string, list, tuple, set, frozenset e dict.

Curiosamente, a partir da versão 3, o Python não limita o tamanho máximo de valores inteiros, de modo que tal tamanho seja dependente dos sistema
e dos recursos disponíveis.

O Python suporta as higher order functions clássicas, como map(), filter(), reduce(), além de all() e any().

Os documentos utilizados para padronizar a linguagem são chamados de PEP (Python Enhancement Propostal) e mantidos e discutidos na PSF (Python Software
Foundation). A PEP 20, entitulada "The Zen of Python", define a filosofia da linguagem em 19 aforismos, sendo eles:

- O bonito é melhor do que o feio.
- O explícito é melhor do que o implícito.
- O simples é melhor do que o complexo.
- O complexo é melhor do que o complicado.
- O plano é melhor que o aninhado.
- O esparso é melhor do que o denso.
- A legibilidade conta.
- Casos especiais não são especiais o suficiente para quebrar regras.
- Embora praticidade supere a pureza.
- Em face da ambiguidade, recuse a tentação de adivinhar.
- Deve haver apenas um — e preferencialmente só um — caminho óbvio de fazer isso.
- Embora esse caminho possa não ser óbvio a princípio, a menos que você seja holandês.
- O agora é melhor do que o nunca.
- Embora o nunca é sempre melhor do que o exatamente agora.
- Se a implementação é difícil de explicar, isso é uma má ideia.
- Se a implementação é fácil de explicar, isso pode ser uma boa ideia.
- Os namespaces são ótimas ideias, vamos fazer mais!

Outra PEP particularmente importante é a PEP 8, que define o guia de estilo de codificação do Python, o que é de extrema importância, já que a
linguagem tem um grande foco em legibilidade.


