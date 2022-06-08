### Tarefa 003: Git Exercícios - 03/06/2021.

Responda as questões abaixo (exercite os comandos do git correspondentes). Lembre-se de que o “interessante” não é exatamente o conjunto de respostas, mas o processo de obtê-las e a experiência obtida com a execução dos comandos.


1. Qual o comando para obter a versão instalada do Git?
`git --version`

2. Qual o efeito da execução de cada um dos comandos abaixo?
  a. git help
  Imprime uma lista com a descrição dos comandos mais utilizados.

  b. git help checkout
  Imprime o manual do comando para trocar de branches ou restaurar a árvore de diretórios, com a descrição de todos os parâmetros e opções disponíveis.

  c. git help merge
  Imprime o manual do comando para mesclar/fundir históricos de commits.

  d. git init
  Cria um repositório git vazio ou reinicializa um já existente.

  e. git add --all
  Adiciona todas as mudanças para a zona de staging.

  f. git add -u
  
  g. git config -l
  List all variables set in config file, along with their values.
  Lista as variáveis de configuração do git, juntamente com seus valores.

  h. git mv a.txt b.txt
  Move o conteúdo do arquivo a.txt para um novo arquivo chamado b.txt.

  i. git reset --hard
  Desfaz as mudanças feitas em relação ao último commit, tanto na zona de staging como no diretório de trabalho.
  
  j. git log -27
  Visualiza o histórico dos 27 últimos commits.

3. O fluxo “clássico” de interação com o Git é algo como “alterar um ou mais arquivos”,
    “acrescentar essas mudanças para serem contemplados no próximo commit” e, finalmente, executar um “commit”. Quais os comandos necessários para realizar os dois últimos “passos” desse fluxo?

Os comandos sao: `git add <arquivos_a_serem_adicionados>`  e `git commit`.

4. Qual o comando deve ser executado para identificar o que foi alterado desde o último “commit”?
`git diff`

5. Em um dado repositório, arquivos simplesmente copiados para lá, ou seja, _untracked_, podem ser exibidos/identificados com que comando?
`git status`

6. Qual o comando para efetuar um _commit_?
`git commit`

7. Qual o comando que devemos empregar para descartar mudanças ocorridas no arquivo teste.txt, por exemplo?
`git restore teste.txt`

8. O que deve ser feito para que um determinado diretório do seu repositório seja ignorado pelo Git? Faça uma busca por **.gitignore**.
Adicionar o caminho do diretório ao arquivo .gitignore.

9. O que acontece se o seu repositório local for acidentalmente removido?
Todas as alterações em relação ao repositório remoto são perdidas.

10. Como clonar um repositório remoto?
`git clone <url_do_repositorio_remoto>`

11. Em alguns cenários **git log** pode produzir extensos resultados. Se houver interesse em visualizar o histórico de um repositório, onde cada mudança é fornecida exatamente em uma única linha, qual o comando que deve ser empregado?
`git log --oneline`

12. Em qual arquivo o Git armazena informações de configuração empregadas por usuário?
No arquivo .git.

13. Qual o comando para criar um repositório local?
`git init`

14. Qual o nome do diretório criado pelo Git quando se executa o comando **git init**?
`git init`

15. Qual o comando para adicionar todos os arquivos modificados? (Aqueles para os quais **git status** identificam como **modified**?)
`git add --all`

16. O Git faz uso do valor de hash conhecido por SHA1. O que isto significa? Qual o propósito? O que é SHA1?


17. Qual a palavra para indicar o último _commit_ em vez do valor de hash SHA1 correspondente?


18. Quando se cria dois arquivos usando um editor de texto qualquer e, na sequência, executamos o comando **git add -u**, os dois arquivos criados passam de _untracked_ para _new file_?


19. Qual o efeito da execução dos dois comandos abaixo, nesta ordem, em um dado repositório?
**git reset --soft HEAD~1**
**git reset --hard**

20. Após o emprego de um ambiente integrado de desenvolvimento (IDE), é comum a criação de arquivos e diretórios. Qual o comando que podemos empregar para remover arquivos e diretórios _untracked_?


21. Qual o nome do arquivo no qual podemos inserir a indicação para o Git de arquivos e diretórios a serem ignorados?
No arquivo .gitignore.

22. Quando se cria o arquivo _MinhaClasse.class_ em um dado diretório e desejamos que arquivos com a extensão .class, como neste caso, sejam ignorados por todos os membros de uma equipe que estão contribuindo com um dado projeto, como devemos proceder?
Adicionar "\*.class" no arquivo .gitignore.

23. jQuery é uma famosa biblioteca em JavaScript. Consulte detalhes em [jQuery](http://jquery.com). O repositório correspondente encontra-se em [gitRep](https://github.com/jquery/jquery.git). Faça o clone deste repositório.
`git clone https://github.com/jquery/jquery.git`

24. No repositório **jqueryrepo**, criado no passo anterior, qual o efeito do comando
**git shortlog -sne**?
Será impressa uma relação dos contribuidores que realizaram commits no repositório, constando o nome, endereço de e-mail e número de commits.
Essa lista de contribuidores estará ordenada descrescentemente pelo número de commits.

25. No repositório **jqueryrepo**, qual o efeito de **git remote -v**?
Será impresso o nome e URL do repositório remoto associado ao repositório local.

26. Um repositório Git pode ser etiquetado ao longo do tempo. Ou seja, _commits_ específicos podem ser “marcados” ou “etiquetados” para facilitar referências posteriores. Para listar todas as “etiquetas” (_tags_) estabelecidas para um dado repositório, qual comando deve ser executado?
`git tag -l`

27. Caso um dato repositório retorne muitas “marcas” ou “etiquetas” para o comando **git tag**, como retornar apenas aquelas que atendem a determinado padrão, por exemplo, iniciadas por 2.0?
`git tag -l 2.0*`

28. Qual o efeito do comando **git tag -a 3.4-gold -m “minha versão ouro”**?

29. Após executado o comando acima, qual o efeito de **git show 3.4-gold**?

30. O que o comando **git push origin 3.4-gold** teria como efeito?


31. Após executar um commit, qual o efeito de **git commit --amend**?
Sobrescreve o último commit realizado. Com tal comando, é possível modificar as alterações e mensagem de descrição do último commit.

32. Após executar **git add x.txt**, qual o efeito de **git reset HEAD x.txt**?

33. Após alterar o conteúdo de um arquivo committed em passo anterior, qual o efeito do comando **git checkout -- a.txt**?


34. Qual a diferença entre os comandos **git reset HEAD a.txt** e **git checkout -- a.txt**?

35. Veja como interpretar o resultado de git diff [aqui](https://medium.com/therobinkim/how-to-read-a-git-diff-6c87a9dc47c5). Execute, em um dos seus projetos, o comando **git diff HEAD~1 HEAD** e certifique-se de que entende o resultado apresentado.



INSTRUÇÕES:

1. No seu repositório pessoal, criar a pasta aula04.
2. Commitar este arquivo respondido nesta pasta.
3. A data limite para concluir esta tarefa é dia 07/06/2021, as 23h59min.











</DIV/>
