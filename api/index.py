import json

def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        "body": json.dumps({
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
    }
