import os
from flask import Flask

from routes.panda import realtime

app = Flask(__name__)
app.register_blueprint(realtime)


@app.route("/")
def home():
    return "PANDA'S LIB PYTHON"


if __name__ == "_main_":
    port = int(os.environ.get("PORT", 2000))
    app.run(debug=False, host="0.0.0.0", port=port)
