from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, User, Disk, Exchange, init_db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso. Por favor, faça o login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Usuário ou senha inválidos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add_disk', methods=['GET', 'POST'])
@login_required
def add_disk():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        year = request.form['year']
        disk = Disk(title=title, artist=artist, year=year, owner_id=current_user.id)
        db.session.add(disk)
        db.session.commit()
        flash('Disco adicionado com sucesso.')
        return redirect(url_for('index'))
    return render_template('add_disk.html')

@app.route('/exchange_disks', methods=['GET', 'POST'])
@login_required
def exchange_disks():
    if request.method == 'POST':
        from_disk_id = request.form['from_disk_id']
        to_disk_id = request.form['to_disk_id']
        from_disk = Disk.query.get(from_disk_id)
        to_disk = Disk.query.get(to_disk_id)
        if from_disk and to_disk and from_disk.owner_id == current_user.id:
            exchange = Exchange(disk_id=to_disk.id, from_user_id=current_user.id, to_user_id=to_disk.owner_id, status='pending')
            db.session.add(exchange)
            db.session.commit()
            flash('Pedido de troca enviado.')
            return redirect(url_for('index'))
        flash('Pedido de troca inválido.')
    disks = Disk.query.filter(Disk.owner_id != current_user.id).all()
    return render_template('exchange_disks.html', disks=disks)

@app.route('/search_disks', methods=['GET', 'POST'])
def search_disks():
    disks = []
    if request.method == 'POST':
        search_term = request.form['search_term']
        disks = Disk.query.filter((Disk.title.ilike(f'%{search_term}%')) | (Disk.artist.ilike(f'%{search_term}%'))).all()
    return render_template('search_disks.html', disks=disks)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
