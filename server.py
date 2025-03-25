from flask import Flask, request, jsonify
from model import ai_resolve
from nlp_processor import extract_domain

app = Flask(__name__)

@app.route("/resolve", methods=["GET"])
def resolve():
    query = request.args.get("query")
    domain = extract_domain(query)

    if not domain:
        return jsonify({"error": "Could not understand query"}), 400

    result = ai_resolve(domain)
    return jsonify({"query": query, "domain": domain, "result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
