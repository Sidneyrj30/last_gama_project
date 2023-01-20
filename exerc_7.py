from flask import Flask, request

app = Flask(__name__)

# curl -X POST 'http://localhost:5000/soma'-H 'Content-Type: application/json' -d '{"x": 1, "y": 2}'

@app.route('/soma', methods=["POST"])
def operacao():
    response = request.json
    return {"resposta": response["x"] + response["y"]} 

if __name__ == "__main__":
    app.run(debug=True)