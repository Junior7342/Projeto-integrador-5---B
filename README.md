# Projeto-integrador-5-B

Devem ser instaladas as seguintes bibliotecas:
~~~
pip install flask flask_sqlalchemy flask_migrate flask_login mysql-connector-python
~~~

Para criar o banco de dados realizar os seguintes comandos no terminal:
~~~
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
~~~
Em seguida, no terminal executar o comando
~~~
python app.py
~~~
Por último, acessar o site http://127.0.0.1:5000/
