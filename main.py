from flask import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    #partido=Partido()
    #pais1 = partido.get_pais1()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=4000)
