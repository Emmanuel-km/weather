# A new look at this project

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)


    
    @app.route('/')
    def home():
        return render_template('index.html')
    @app.route('/hello')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)