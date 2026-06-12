[LEIAME.txt](https://github.com/user-attachments/files/28860478/LEIAME.txt)
 Análise de Suicídios e Óbitos (DATASUS)

Neste projeto, desenvolvi um banco de dados MySQL para analisar dados de óbitos com base no padrão do DATASUS. Utilizando Views (consultas salvas), consigo responder rapidamente a perguntas relacionadas à idade, sexo, escolaridade e aos estados com maior número de registros.

 Como Rodar o Projeto

 1. Ajuste no MySQL Workbench (Super Importante💯💯💯)

O MySQL bloqueia a leitura de arquivos locais por questões de segurança. Para habilitar essa funcionalidade, realizei o seguinte procedimento:

1. Na tela inicial do Workbench, clique com o botão direito sobre a conexão utilizada e selecione Edit Connection.
2. Acesse a aba Advanced.
3. No campo Others, adicione o parâmetro:

`OPT_LOCAL_INFILE=1`

4. Salve as alterações e reinicie a conexão.

 2. Criar o Banco e Importar os Dados

1. Abri o script SQL do projeto no MySQL Workbench.
2. No comando `LOAD DATA LOCAL INFILE`, alterei o caminho do arquivo para o local onde o arquivo `suicidios.csv` está armazenado, utilizando barras normais (`/`).
3. Executei todo o script para criar a estrutura do banco e importar os dados.

 Como Construí o SQL

Organizei o projeto em três etapas principais:

 A Tabela (`obitos`)

Criei a tabela `obitos` de forma compatível com a estrutura do arquivo CSV. Para os campos de nascimento e óbito, utilizei o tipo `DATE`, o que facilitou os cálculos de idade durante as análises.

 A Importação dos Dados

Utilizei o comando `LOAD DATA LOCAL INFILE` por ser uma solução eficiente para importar milhares de registros em poucos segundos, sem comprometer o desempenho do Workbench.

 As Views de Análise

Criei diferentes Views para simplificar as consultas e evitar a reescrita de comandos SQL complexos:

* `listar_obito`: calcula a idade exata de cada pessoa e exibe informações como sexo e estado.
* `registros_suicidios`: filtra apenas os registros relacionados a suicídio, considerando os códigos CID-10 de X60 a X84 por meio de expressões regulares (`REGEXP`).
* `estados_afetados`: apresenta os 10 estados com maior número de registros.
* `nivel_escolaridade` e `registros_eciv`: agrupam os dados por escolaridade e estado civil.
* `media_estados`: calcula a média de idade das pessoas por estado.
* `casos`: gera um relatório consolidado relacionando estado, estado civil, escolaridade e causa do óbito.

 Como Visualizar os Resultados

Após executar todo o script, não é necessário refazer os cálculos. Basta consultar a View desejada:

```sql
-- Visualizar o total de suicídios por estado:
SELECT * FROM registros_suicidios;

-- Visualizar a média de idade por estado:
SELECT * FROM media_estados;
```

  
