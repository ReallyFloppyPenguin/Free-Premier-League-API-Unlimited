from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        response_data = {
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
        }
        
        self.wfile.write(json.dumps(response_data).encode())
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
