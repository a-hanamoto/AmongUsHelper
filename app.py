from flask import Flask, render_template, request
from main import infer

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    amongus_str, res = "", ""
    if request.method == "POST" and "amongus_str" in request.form:
        amongus_str = request.form.get("amongus_str")
        res = infer(amongus_str)
    return render_template("inference.html", amongus_str=amongus_str, res=res)


if __name__ == "__main__":
    app.run(port=4009)
