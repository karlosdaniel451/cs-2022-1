### Semana 4 - Dia 15/06/2022 - Aulas 025a028 - Atividade Supervisionada
1. Participação na Campus Party
2. Informar o nome e a data do(s) evento(s) que você participou;
3. Descrever suas observações a respeito do evento, bem como da Campus Party de uma forma geral.
4. Commitar o texto no seu repositório pessoal, até as 23h59min do dia 24/06/2022.


A Campus Party é um festival de tecnologia, empreendedorismo e inovação com edições em várias cidades do Brasil e do mundo.

A Campus Party Goiás 2 foi a 2º edição da Campus em Goiás e aconteceu do dia 15 ao dia 18 de junho de 2022 em Goiânia.

Neste evento, participei de palestras e *talks* sobre DevOps, Open Data, IOT, trabalho no exterior entre outros temas.


#### Evento participado escolhido para a atividade: OpenSearch: Análise de Dados poderosa e Opensource.

Nome da palestrante: Thaynara Mendes.
Horário: 19:30h - 19:55h do dia 17.
Palco: Bancada Metabotix
Referências:

- Documentação oficial: https://opensearch.org/.
- URL do repositório de exemplo feito pela palestrante: https://github.com/thaycafe/opensearch_lab_CPGO.

Nesta *talk*, a palestrante fez uma introdução à ferramenta de análise de dados livre e de código-aberto OpenSearch, permitindo
injetar, realizar buscas, visualizar e analisar dados. Além disso, tal ferramenta pode ser extentida por plugins para aprimorar as buscas,
segurança, performance, funcionalidades de *machine learning* e muito mais.

O OpenSearch surguiu como um fork mais aberto e livre do Elasticsearch e do Kibana, oferecendo uma licença, a Apache2.0, mais aberta e focada
na comunidade do que a anterior, a licença Elastic. Assim como o Elasticsearch, o OpenSearch é baseado no Lucene, uma biblioteca de indexação
e busca escrita em Java.

Os principais casos de uso do OpenSearch são:

- Análise de logs;
- Monitoramento de aplicações em tempo real;
- Análise de clickstream
- Backend de pesquisas.

Depois que dados são adicionados ao OpenSearch, é possível realizar pesquisas textuais utilizado funcionalidades como buscas baseadas em
atributos, múltiplos índices, ranking e ordenação por pontuação, entre outros.

Portanto, os princípais usos de tal ferramenta e outras de buscas textuais, são no backend de aplicações que envolvem buscas, como a
Wikipedia e plataformas de E-Commerce e na análise de log.

O OpenSearch é um motor de busca e análise de dados distribuído, o que implica numa arquitetura organizada em **cluster** de **nodes**,
em que cada node é um servidor que armazena os dados e processa as requisições de busca.
Os dados são organizados em **indices**, que são coleções de **documentos JSON**.

A interação com os clusters se dá através de uma API REST flexível. Com tal API, é possível obter informações sobre a saúde dos clusters,
modificar índices, obter estatísticas de uso, entre outras ações. Por exemplo, um documento JSON poderia ser adicionado a um índices
com a seguinte requisição HTTP:

```
PUT https://<host>:<port>/<index-name>/_doc/<document-id>
{
  "title": "The Wind Rises",
  "release_date": "2013-07-20"
}
```

Tal documento poderia ser buscado com a seguinte requisição, onde *wind* é a string na qual a busca será baseada:

```
GET https://<host>:<port>/<index-name>/_search?q=wind
```



