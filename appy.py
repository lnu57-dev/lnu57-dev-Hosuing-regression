# Flask example
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # parse form values: request.form['income'], etc.
        # compute prediction, return template with prediction_text
        pass
    return render_template('index.html')
