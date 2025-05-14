
from flask import Flask
from app.routes.hello import hello_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)