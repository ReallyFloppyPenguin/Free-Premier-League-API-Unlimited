import requests
from bs4 import BeautifulSoup
import json

def get_table():
    try:
        link = "https://onefootball.com/en/competition/premier-league-9/table"
        source = requests.get(link).text
        page = BeautifulSoup(source, "lxml")

        # Find all rows in the standings table
        rows = page.find_all("li", class_="Standing_standings__row__5sdZG")

        # Initialize the table
        headers = ["Position", "Team", "Played", "Wins", "Draws", "Losses", "Goal Difference", "Points"]
        
        # Store data as objects for better API response
        teams = []

        # Extract data for each row
        for row in rows:
            position_elem = row.find("div", class_="Standing_standings__cell__5Kd0W")
            team_elem = row.find("p", class_="Standing_standings__teamName__psv61")
            stats = row.find_all("div", class_="Standing_standings__cell__5Kd0W")

            if position_elem and team_elem and len(stats) >= 7:
                team_data = {
                    "position": position_elem.text.strip(),
                    "team": team_elem.text.strip(),
                    "played": stats[2].text.strip(),
                    "wins": stats[3].text.strip(),
                    "draws": stats[4].text.strip(),
                    "losses": stats[5].text.strip(),
                    "goal_difference": stats[6].text.strip(),
                    "points": stats[7].text.strip()
                }
                teams.append(team_data)

        # Return both table format and structured data
        return {
            "table_headers": headers,
            "teams": teams,
            "total_teams": len(teams)
        }, 200
    except Exception as e:
        return {"error": str(e)}, 500

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data, status_code = get_table()
        
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
