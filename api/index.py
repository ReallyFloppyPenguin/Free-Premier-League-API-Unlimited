from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({
        "message": "Hey there! Welcome to the Premier League API 2.0",
        "endpoints": {
            "/api/players/<player_name>": "Get player statistics",
            "/api/fixtures": "Get all fixtures", 
            "/api/fixtures?team=<team_name>": "Get fixtures for specific team",
            "/api/table": "Get Premier League table"
        },
        "usage": "Use the endpoints above to get Premier League data",
        "example_urls": [
            "/api/players/ronaldo",
            "/api/fixtures",
            "/api/fixtures?team=arsenal",
            "/api/table"
        ]
    })

# Export for Vercel
handler = app
