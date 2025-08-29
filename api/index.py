from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
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

# This is required for Vercel
def handler(request, response):
    return app
