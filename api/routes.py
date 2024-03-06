from flask import Flask, jsonify
from flask_cors import CORS
from modules.facts import *
from modules.headers import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/randomfact', methods=['GET'])
def return_random_fact():
    check_headers()
    random_fact = get_random_fact()
    print(random_fact)
    return jsonify(random_fact)

@app.route('/factbase', methods=['GET'])
def return_fact_base():
    check_headers()
    all_facts = get_facts()
    response = {
        "count": len(all_facts),
        "facts": all_facts
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
