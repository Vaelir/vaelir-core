from flask import Flask
from api.status import status_bp
from api.memory import memory_bp

app = Flask(__name__)
app.register_blueprint(status_bp)
app.register_blueprint(memory_bp)

if __name__ == "__main__":
    app.run(debug=True)
