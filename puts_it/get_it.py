import flask as f
from get_image import get
app = f.Flask(__name__)

@app.route("/", methods=["POST","GET"])
def indexHandle():
    get.delay(f.request.args.get('uri'))
    return "hello"
if __name__ == "__main__":
    app.run(debug=True)
