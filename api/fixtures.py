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

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query_string = self.path.split('?', 1)[1] if '?' in self.path else ''
        query_params = parse_qs(query_string)
        team = query_params.get('team', [None])[0]
        
        if team:
            data, status_code = get_team_fixtures(team)
        else:
            data, status_code = get_all_fixtures()
            
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        self.wfile.write(json.dumps(data).encode())
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
