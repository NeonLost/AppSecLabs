import os
from flask import Blueprint, jsonify, request


crlf_injection_1 = Blueprint('crlf_injection_1', __name__)

users_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.txt')


@crlf_injection_1.route('/challenges/crlf_injection_1/auth', methods=['GET', 'POST'])
def auth():
    try:
        login = request.values.get('login')
        password = request.values.get('password')

        user = get_user_by_login_and_pass(login, password)

        user_data = {}
        if user[0] == 'admin':
            user_data['flag'] = '4d0beb1562755ffa5641e249c9b05bb5'
        user_data['role'] = user[0]
        user_data['login'] = user[1]
        return jsonify(user_data)
    except BaseException:
        return jsonify({'error': 'Invalid credentials'})


@crlf_injection_1.route('/challenges/crlf_injection_1/reg', methods=['GET', 'POST'])
def register():
    try:
        login = request.values.get('login')
        password = request.values.get('password')

        user_exists = is_user_exists(login)
        if user_exists:
            return jsonify({'error': 'User exist'})

        set_user_to_db(login, password)
        return jsonify({'status': 'ok'})
    except BaseException:
        return jsonify({'error': 'Unable to register new user'})


def get_user_by_login_and_pass(login, password):
    if not os.path.exists(users_path):
        return None

    with open(users_path, 'r') as db:
        for line in db.readlines():
            user = line.strip().split(' ')
            if len(user) == 3 and user[1] == login and user[2] == password:
                return user
    return None


def is_user_exists(login):
    if not os.path.exists(users_path):
        return False

    with open(users_path, 'r') as db:
        for line in db.readlines():
            user = line.strip().split(' ')
            if len(user) == 3 and user[1] == login:
                return True
    return False


def set_user_to_db(login, password):
    with open(users_path, 'a+') as db:
        db.write('guest ' + login + ' ' + password + '\r')
    return True
