from flask import Flask, request, jsonify
import cPickle, base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    # take user input to take the amount of data
    if request.values.get("name"):
        try:
            data = cPickle.loads(base64.b64decode(request.values.get("name")))
            log(str(data))
            return jsonify(str(data))
        except:
            pass
    string_to_return = 'Hi. Who are you? Are u John Doe? <a href="/?name='+base64.b64encode(cPickle.dumps('John'))+'">Check the name</><br/>'
    string_to_return += '<a href="/log">See logs</a>'
    return string_to_return


@app.route('/log', methods=['GET', 'POST'])
def log(info=""):
    # take user input to take the amount of data
    if request.values.get("some") or info <> "":
        with open("log", "a") as file:
            file.writelines(request.values.get("some")+"\n") if info == "" else file.writelines(info+"\n")
    with open("log", "r") as file:
        return file.read()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
