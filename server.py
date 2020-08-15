from flask import Flask, request, abort
import sys
from io import StringIO

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run():
    content = request.json["content"]
    output = StringIO()
    sys.stdout = output
    eval(content)
    return output.getvalue()

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)