from flask import Flask
from routes import calculator_bp

app = Flask(__name__)
app.register_blueprint(calculator_bp)

if __name__ == "__main__":
    app.run(debug=True)
