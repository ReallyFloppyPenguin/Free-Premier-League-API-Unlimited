import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs

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

def handler(request, response):
    # Set CORS headers
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    
    if request.method == 'OPTIONS':
        return ''
    
    if request.method == 'GET':
        # Parse query parameters
        query_params = parse_qs(request.url.query) if request.url.query else {}
        team = query_params.get('team', [None])[0]
        
        if team:
            data, status_code = get_team_fixtures(team)
        else:
            data, status_code = get_all_fixtures()
            
        response.status_code = status_code
        return data
    else:
        response.status_code = 405
        return {"error": "Method not allowed"}
