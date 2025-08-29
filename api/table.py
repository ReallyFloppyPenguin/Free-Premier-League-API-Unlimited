from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

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
        }
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/')
def table():
    try:
        data = get_table()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Export for Vercel
handler = app
