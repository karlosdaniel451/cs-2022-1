## Semana 1 - Dia 25/05/2022 - Aulas 001a004 - Atividade Supervisionada


1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto de pelo menos uma pÃ¡gina, descrito com suas prÃ³prias palavras, destacando:
* As definiÃ§Ãµes dos conceitos envolvidos;
* As principais caracterÃ­sticas deste conceito (pelo menos umas cinco).

### REST API

#### Definições

##### API

API (Application Programming Interface) é uma
especificação para a construção ou integração
de sistemas de software. Exemplos de APIs
conhecidas são a Win32 API, POSIX API e a API
REST do GitHub. Repare que uma API é uma
especificação ou interface, que pode ou não 
estar implementada. Na verdade, uma mesma API
pode ter diversas implementações. Por exemplo,
a POSIX API é implementada por diversos
sistemas operacionais baseados em UNIX. Logo,
os sistemas que implementam a POSIX API
oferecem uma interface comum na qual é
possível interagir com eles, para, por
exemplo, invocar uma chamada de sistema.

Uma API Web, é uma especificação de como
interagir com um servidor/serviço Web que,
por definição, se dá por meio do protocolo
HTTP.

##### API REST

REST (REpresentational State Transfer) é um
padrão arquitetural para APIs de sistemas de
hipermídia distribuídos, sendo o mais conhecido
destes sistemas hipermídia, a Web. Dessa forma,
uma API Web que adere ao conjunto de princípios
e definições do padrão REST, pode ser chamada
de API REST e serviço Web que a implementa,
Serviço Web Restful.

O padrão REST foi apresentando na dissertação de
Mestrado do cientista da computação Roy Fielding
em 2000. Não coincidentemente, Fielding também
foi um dos principais autores da especificação
do protocolo de aplicação HTTP.

Os critérios para que uma API Web seja considerada
uma API REST são:

- Ter uma arquitetura cliente-servidor sem estado,
na qual o cliente navega por um conjunto de recursos
gerenciados pelo servidor. Recurso, no contexto
de APIs REST, significa qualquer informação,
como imagens, documentos ou um registro em um
banco de dados. Como a comunicação deve ser sem
estado (*stateless*), logo cada requisição enviada
pelo cliente é autocontida e o servidor não armazena
informação sobre o cliente quando elas ocorrem.

- Cada recurso deve ser identificado unicamente e
deve ter uma representação uniforme quando seu
estado é trocado entre o cliente e o servidor.

- Cada recurso deve possuir descrições, ou metadados,
além de possíveis ações que o cliente pode executar nele.

- O cliente deve necessitar apenas da URL inicial do
servidor Web, logo deve ser capaz de navegar entre
qualquer recurso através de hyperlinks.

### Referências:

- What is REST - REST API Tutorial. Disponível em <https://restfulapi.net/>.
- What is a REST API? Disponível em <https://www.redhat.com/en/topics/api/what-is-a-rest-api>.

