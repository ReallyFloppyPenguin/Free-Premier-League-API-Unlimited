import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs
import json

def get_all_fixtures():
    try:
        link = "https://onefootball.com/en/competition/premier-league-9/fixtures"
        source = requests.get(link).text
        page = BeautifulSoup(source, "lxml")
        fix = page.find_all("a", class_="MatchCard_matchCard__iOv4G")

        fixtures = []
        for match in fix:
            fixture = match.get_text(separator=" ").strip()
            if fixture:  # Only add non-empty fixtures
                fixtures.append(fixture)

        return {"fixtures": fixtures}, 200
    except Exception as e:
        return {"error": str(e)}, 500

def get_team_fixtures(team):
    try:
        link = "https://onefootball.com/en/competition/premier-league-9/fixtures"
        source = requests.get(link).text
        page = BeautifulSoup(source, "lxml")
        fix = page.find_all("a", class_="MatchCard_matchCard__iOv4G")

        fixtures = []
        for match in fix:
            fixture = match.get_text(separator=" ").strip()
            if fixture:  # Only add non-empty fixtures
                fixtures.append(fixture)

        filtered_fixtures = [fixture for fixture in fixtures if team.lower() in fixture.lower()]

        return {"team_fixtures": filtered_fixtures, "team": team}, 200
    except Exception as e:
        return {"error": str(e)}, 500

def handler(request):
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": ""
        }
    
    if request.method == 'GET':
        # Parse query parameters
        query_string = getattr(request, 'query_string', '') or ''
        query_params = parse_qs(query_string)
        team = query_params.get('team', [None])[0]
        
        if team:
            data, status_code = get_team_fixtures(team)
        else:
            data, status_code = get_all_fixtures()
            
        return {
            "statusCode": status_code,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(data)
        }
    else:
        return {
            "statusCode": 405,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Method not allowed"})
        }
