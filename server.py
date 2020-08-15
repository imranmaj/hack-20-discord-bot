from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run():
    content = request.json["content"]
    return str(eval(content))

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)