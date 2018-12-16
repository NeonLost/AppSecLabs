from flask import Flask
from improper_input_validation_1.server import improper_input_validation_1
from sql_injection_1.server import sql_injection_1
from sql_injection_2.server import sql_injection_2
from crlf_injection_1.server import crlf_injection_1
from padding_oracle_1.server import padding_oracle_1


app = Flask(__name__)
app.register_blueprint(improper_input_validation_1)
app.register_blueprint(sql_injection_1)
app.register_blueprint(sql_injection_2)
app.register_blueprint(crlf_injection_1)
app.register_blueprint(padding_oracle_1)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')
