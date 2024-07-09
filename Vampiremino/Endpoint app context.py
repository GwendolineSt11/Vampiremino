from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/interactions/', methods=['GET'])
def interactions():
    return jsonify({"message": "Hello, this is the interaction endpoint!"})


if __name__ == "__main__":
    app.run(debug=True)
