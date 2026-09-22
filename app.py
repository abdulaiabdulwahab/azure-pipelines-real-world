from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Azure Pipelines API",
        "status": "running"
    })


@app.route("/health")
def health():
    """
    Health endpoint.

    Deployment systems and monitoring tools can use this
    endpoint to determine whether the application is alive.
    """
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)