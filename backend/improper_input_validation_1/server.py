import random
import string
import uuid
from flask import Blueprint, jsonify, request


improper_input_validation_1 = Blueprint('improper_input_validation_1', __name__)


class User:
    def __init__(self, login, password, amount, pan):
        self.login = login
        self.password = password
        self.amount = amount
        self.pan = pan


users = {}
tokens = {}


@improper_input_validation_1.route('/labs/improper_input_validation_1/reg', methods=['GET', 'POST'])
def register():
    try:
        login = request.values.get('login')
        password = request.values.get('password')

        user_exists = is_user_exists(login)
        if user_exists:
            return jsonify({'error': 'User exist'})

        create_new_user(login, password)
        return jsonify({'status': 'ok'})
    except BaseException:
        return jsonify({'error': 'Unable to register new user'})


@improper_input_validation_1.route('/labs/improper_input_validation_1/auth', methods=['GET', 'POST'])
def auth():
    login = request.values.get('login')
    password = request.values.get('password')

    user = get_user_by_login_and_pass(login, password)
    if user is not None:
        token = uuid.uuid4().hex
        tokens.update({token: login})
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid credentials'})


@improper_input_validation_1.route('/labs/improper_input_validation_1/info', methods=['GET', 'POST'])
def info():
    token = request.values.get('token')
    login = tokens.get(token)
    user = users.get(login)
    if user and user.amount > 0:
        return jsonify({'info': {
            'login': user.login,
            'flag': '39296fda6ce017f718bcea833eb6c3c6',
            'debit': {
                'amount': user.amount,
                'pan': user.pan
            }
        }})
    elif user:
        return jsonify({'info': {
            'login': user.login,
            'debit': {
                'amount': user.amount,
                'pan': user.pan
            }
        }})
    else:
        return jsonify({'error': 'Access denied'})


@improper_input_validation_1.route('/labs/improper_input_validation_1/transfer', methods=['GET', 'POST'])
def transfer():
    token = request.values.get('token')
    to_login = request.values.get('to')
    amount_str = request.values.get('amount')

    amount = 0
    if is_int(amount_str):
        amount = int(amount_str)
    else:
        return jsonify({'error': 'Amount must be positive number'})

    from_user = users.get(tokens.get(token))
    to_user = users.get(to_login)
    if from_user:
        if to_user:
            if from_user.amount >= amount:
                from_user.amount -= amount
                to_user.amount += amount
                return jsonify({'info': 'Success'})
            else:
                return jsonify({'error': 'Insufficient funds'})
        else:
            return jsonify({'error': 'User is not exist'})
    else:
        return jsonify({'error': 'Access denied'})


def is_int(s):
    try:
        int(s)
        return True
    except Exception:
        return False


def get_user_by_login_and_pass(login, password):
    user = users.get(login)
    if user is not None and user.password == password:
        return user
    return None


def is_user_exists(login):
    user = users.get(login)
    return user is not None


def create_new_user(login, password):
    new_user = User(login, password, 0, '*' + ''.join(random.choice(string.digits) for _ in range(4)))
    users.update({new_user.login: new_user})
