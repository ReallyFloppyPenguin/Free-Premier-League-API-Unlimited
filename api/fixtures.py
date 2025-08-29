from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

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

        return {"fixtures": fixtures}
    except Exception as e:
        return {"error": str(e)}

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

        return {"team_fixtures": filtered_fixtures, "team": team}
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def fixtures():
    try:
        team = request.args.get('team')
        
        if team:
            data = get_team_fixtures(team)
        else:
            data = get_all_fixtures()
            
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Export for Vercel
handler = app
