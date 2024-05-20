# Projeto-integrador-5

## Instalação
Este projeto deve ser clonado do Github e executado localmente no Visual Studio ou em software equivalente, com suporte para Python e Flask.
Devem ser instaladas as seguintes bibliotecas do Python:
~~~
pip install flask
pip install flask_sqlalchemy
pip install flask_migrate
pip install flask_login
pip install mysql-connector-python
~~~

Para criar o banco de dados realizar os seguintes comandos no terminal do Visual Studio:
~~~
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
~~~
Em seguida, no terminal executar o comando
~~~
python app.py
~~~
Por último, acessar o site http://127.0.0.1:5000/ (esse link vai aparecer no próprio terminal do Visual Studio). Pronto! O aplicativo está rodando!

## Rodando o aplicativo
Por ser um MVP (Minimum Viable Product, ou Produto Mínimo Viável), o aplicativo ainda possui funcionalidades limitadas. Para utilizá-lo, seguir as instruções contidas no tutorial em vídeo disponível neste repositório

## Membros do grupo
* Cintia Mascari Martim - Idealização de conceito, planejamento e protótipo do frontend
* Helvio Rosa Pinto - Elaboração dos documentos com as jornadas dos usuários
* Mamede Rodrigues Junior - Criação do repositório no Github e do arquivo README, app em Flask, backend em Python e banco em SQLite
* Tiago Anselmo Pereira - Protótipo inicial do backend em Python
* Vinicius Jose Matias Marques - Preparação do frontend, com estilização em HTML/CSS

## Protótipo no Figma
https://www.figma.com/design/cOfYcr5hKxTSPKVYmlp1Um/Untitled?node-id=57-31&t=ZBbKyywfsEQNnplg-0

## Revisão do projeto apresentado e definição da prova de conceito
Este projeto é uma nova versão do projeto apresentado na disciplina Projeto Integrador 5 - parte 1. Na disciplina anterior foi desenvolvido um protótipo de backend em Python, faltando ajustes quanto à validação dos dados inseridos e tratamento de erros e exceções. Em virtude das dificuldades de tempo e pela redução de um membro na equipe, não havia sido possível finalizar o app em Flask e nem o backend em Python. Assim, o script em Python exibia uma interface de usuário simples, utilizando o próprio terminal da IDE, apenas para validar a inclusão dos dados na jornada do usuário. O banco de dados seria em PostgreSQL. O repositório de dados associado à prova de conceito do projeto utilizou dicionários em Python, estrutura de dados suficiente para validação daquela ideia inicial.

Na versão atual ocorreram as seguintes evoluções no sistema:
* Finalização do app utilizando o Flask
* Revisão completa do backend em Python, ajustando-o à arquitetura utilizada pelo Flask
* Acréscimo das seguintes funcionalidades no backend:
   1. Login de usuário;
   2. Logout de usuário;
   3. Solicitar troca de disco;
   4. Procurar disco
* Criação de banco de dados em SQLite, substituindo os dicionários em Python
* Integração do frontend com o backend. Agora o app possui interface web, rodando um servidor em Flask

## Descrição do projeto
Aplicativo Cadê Meu Vinil?

Olá novo usuário!

O aplicativo Cadê Meu Vinil? tem como objetivo conectar diversos usuários interessados em compartilhar seus discos através de troca, compra e venda numa plataforma segura e interativa. A versão atual é um MVP (Minimum Viable Product, ou Produto Mínimo Viável), que oferece as seguintes funcionalidades:
1. Registrar novo usuário
2. Realizar login de usuário
3. Realizar logout de usuário
4. Adicionar disco
5. Solicitar troca de disco
6. Procurar disco

## Estrutura do diretório de arquivos do projeto
**Pasta static** - pasta com os arquivos CSS para estilização. Inclui também a pasta assets, com arquivos de imagem utilizados frontend do projeto

**Pastas migrations e _pycache__** - pastas criadas pelo flask_sqlalchemy para gerenciar as migrações do banco de dados

**Pasta templates** - pasta com os modelos (templates) das paginas html exibidas pelo aplicativo

**Diretório raiz** - contém os arquivos README.md; models.py (define as classes utilizadas no backend em Python e define a criação de algumas entradas no banco de dados, com alguns usuários e discos para exemplo); app.db (arquivo do banco de dados); config.py (configuração do banco de dados); e app.py (arquivo em Python/Flask, que cria as routes entre as páginas html e as funções do backend. Além de inicializar o app)


