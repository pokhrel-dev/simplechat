"""
Minimal Flask launcher for quick VS Code runs.

How to use:
- In VS Code open repository root.
- Run this configuration via the Run view, or:
    python application/single_app/run_minimal.py

This file intentionally avoids importing the full app stack.
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['VERSION'] = os.getenv('VERSION', '0.0.0')

@app.route('/')
def index():
    return jsonify({
        "message": "SimpleChat minimal app running",
        "version": app.config['VERSION']
    })

@app.route('/healthz')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    # Use 0.0.0.0 so VS Code and external containers can reach it
    app.run(host='0.0.0.0', port=port, debug=True)
