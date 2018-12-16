import urllib
from padding_oracle_1.crypto import AESCipher
from flask import Blueprint, jsonify, request


padding_oracle_1 = Blueprint('padding_oracle_1', __name__)


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


admin_user = User('admin', '9d5348e3ea0e22c29d4ac55dc7f629e4')
users = {admin_user.login: admin_user}
KEY = 'd72b3fcb'
FLAG = '633973df1fb04d4dbd3b0adefe787c5e'


@padding_oracle_1.route('/labs/padding_oracle_1/reg', methods=['GET', 'POST'])
def register():
    try:
        login = request.values.get('login')
        password = request.values.get('password')

        if not login or not password:
            return jsonify({'error': 'Empty password or login'})

        user_exists = is_user_exists(login)
        if user_exists:
            return jsonify({'error': 'User exist'})

        create_new_user(login, password)
        return jsonify({'status': 'ok'})
    except BaseException:
        return jsonify({'error': 'Unable to register new user'})


@padding_oracle_1.route('/labs/padding_oracle_1/auth', methods=['GET', 'POST'])
def auth():
    login = request.values.get('login')
    password = request.values.get('password')

    if not login or not password:
        return jsonify({'error': 'Empty password or login'})

    user = get_user_by_login_and_pass(login, password)
    if user is not None:
        token = urllib.parse.quote(create_token(login))
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid credentials'})


@padding_oracle_1.route('/labs/padding_oracle_1/info', methods=['GET', 'POST'])
def info():
    token = request.values.get('token')

    if not token:
        return jsonify({'error': 'Missing token'})

    login = get_login_from_token(urllib.parse.unquote(token))
    user = users.get(login)

    if user and user.login == 'admin':
        return jsonify({'info': {
            'login': user.login,
            'flag': FLAG
        }})
    elif user:
        return jsonify({'info': {
            'login': user.login
        }})
    else:
        return jsonify({'error': 'Access denied'})


def get_user_by_login_and_pass(login, password):
    user = users.get(login)
    if user is not None and user.password == password:
        return user
    return None


def is_user_exists(login):
    user = users.get(login)
    return user is not None


def create_new_user(login, password):
    user = User(login, password)
    users.update({user.login: user})


def create_token(login):
    cipher = AESCipher(KEY).encrypt('user=' + login)
    return cipher

def get_login_from_token(token):
    clear_text = AESCipher(KEY).decrypt(token)
    try:
        return clear_text.decode('utf-8').replace('user=', '')
    except:
        return ''

