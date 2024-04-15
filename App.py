from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/db_ticket'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Ticket_Turno'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(15), unique=True, nullable=False)
    pwd = db.Column(db.String(15), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"user('{self.user}', '{self.rol}')"

class Tramite(db.Model):
    __tablename__ = 'tramite'
    id_tramite = db.Column(db.Integer, primary_key=True)
    num_turno = db.Column(db.Integer, nullable=False)
    curp = db.Column(db.String(18), db.ForeignKey('persona.curp'), nullable=False)
    hora = db.Column(db.Time, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(15), default='Pendiente', nullable=False)

class Persona(db.Model):
    __tablename__ = 'persona'
    curp = db.Column(db.String(18), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    paterno = db.Column(db.String(30), nullable=False)
    materno = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.BigInteger, nullable=False)
    celular = db.Column(db.BigInteger, nullable=False)
    correo = db.Column(db.String(100), nullable=False)

class CatalogoMunicipio(db.Model):
    __tablename__ = 'catalogo_municipio'
    id_tramite = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String(60), nullable=False)
    tramites = db.relationship('Tramite', backref='municipio')


def autenticar_usuario(user, password):
    usuario = User.query.filter_by(user=user).first()
    if usuario and bcrypt.check_password_hash(usuario.pwd, password):
        return {'user': usuario.user, 'rol': usuario.rol}
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        captcha_response = request.form['g-recaptcha-response']

        # Autenticación de usuario
        usuario = autenticar_usuario(user, password)

        if usuario:
            # Si el usuario se autentica correctamente, redirige según su rol
            if usuario['rol'] == 'admin':
                return redirect(url_for('pagina_admin'))
            elif usuario['rol'] == 'cliente':
                return redirect(url_for('pagina_cliente'))
        else:
            # Si la autenticación falla, muestra un mensaje de error
            return render_template('index.html', message='Usuario o contraseña incorrectos')

        # Verificación de reCAPTCHA
        if not verify_recaptcha(captcha_response):
            return 'Error: Completa el CAPTCHA correctamente.'

    return render_template('login.html')

def verify_recaptcha(recaptcha_response):
    payload = {
        'secret': '6Ld_IbspAAAAACKslARAnBNZFhrUVSrkNm-bSw6C',
        'response': recaptcha_response
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()
    return result['success']

@app.route('/tickets')
def add_ticket():
    return render_template('tickets.html')

@app.route('/registrat', methods=['POST'])
def registra_aspirante():
    return "PROCESO DE REGISTRO DE TICKET"

@app.route('/cliente')
def pagina_cliente():
    # Renderiza la página HTML del cliente
    return render_template('cliente.html')

@app.route('/admin')
def pagina_admin():
    # Renderiza la página HTML del administrador
    return render_template('admin.html')   


@app.route('/dashboard')
def dashboard():
    total_tramites = Tramite.query.count()
    return render_template('dashboard.html', total_tramites=total_tramites)


if __name__ == '__main__':
    app.run(debug=True)
