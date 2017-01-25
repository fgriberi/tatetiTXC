# define simple flask app
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', position=(0,0))

if __name__ == "__main__":
    app.run()
