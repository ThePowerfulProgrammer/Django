from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print(request.args, request.form)
        return render_template('index.html')
    else:
        # name = name index.html = {name} greet.html
        print(request.args, request.form)
        return render_template('greet.html', name=request.form.get('name', 'Seth'))

