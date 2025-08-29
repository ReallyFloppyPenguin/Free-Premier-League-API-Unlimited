 import requests
from bs4 import BeautifulSoup
from googlesearch import search
from urllib.parse import unquote
import json

def get_player_stats(player_name):
    try:
        # Use Google search to find the player's stats page
        query = f"{player_name} premier league.com stats"
        search_results = list(search(query, num_results=5))
        if search_results:
            res = search_results[0]
        else:
            return {"error": "No search results found for the query."}, 404

        # Adjust the URL to point to the stats page
        if "stats" in res:
            res = res.replace('stats', 'overview')
        sta = res.replace('overview', 'stats')

        # Fetch the stats page
        source = requests.get(sta).text
        page = BeautifulSoup(source, "lxml")

        # Extract player details
        name_elem = page.find("div", class_="player-header__name t-colour")
        name = name_elem.text.strip() if name_elem else "Unknown"
        
        position_label = page.find("div", class_="player-overview__label", string="Position")
        position = position_label.find_next_sibling("div", class_="player-overview__info").text.strip() if position_label else "Unknown"

        # Extract club information
        club = "No longer part of EPL"
        if "Club" in page.text:
            club_info = page.find_all("div", class_="info")
            if len(club_info) > 0:
                club = club_info[0].text.strip()
            if len(club_info) > 1:
                position = club_info[1].text.strip()

        # Extract detailed stats
        detailed_stats = {}
        stat_elements = page.find_all("div", class_="player-stats__stat-value")
        for stat in stat_elements:
            stat_title = stat.text.split("\n")[0].strip()
            stat_container = stat.find("span", class_="allStatContainer")
            if stat_container:
                stat_value = stat_container.text.strip()
                detailed_stats[stat_title] = stat_value

        # Extract personal details
        source2 = requests.get(res).text
        page2 = BeautifulSoup(source2, "lxml")
        personal_details = page2.find("div", class_="player-info__details-list")

        nationality = "Unknown"
        dob = "Unknown"
        height = "Unknown"

        if personal_details:
            # Extract nationality
            nationality_elem = personal_details.find("span", class_="player-info__player-country")
            nationality = nationality_elem.text.strip() if nationality_elem else "Unknown"

            # Extract Date of Birth and Height
            dob_info = personal_details.find_all("div", class_="player-info__col")
            for info in dob_info:
                label_elem = info.find("div", class_="player-info__label")
                info_elem = info.find("div", class_="player-info__info")
                if label_elem and info_elem:
                    label = label_elem.text.strip()
                    if label == "Date of Birth":
                        dob = info_elem.text.strip()
                    elif label == "Height":
                        height = info_elem.text.strip()

        # Return the player details
        return {
            "name": name,
            "position": position,
            "club": club,
            "key_stats": detailed_stats,
            "nationality": nationality,
            "date_of_birth": dob,
            "height": height
        }, 200

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
        # Extract player name from the URL path
        path = getattr(request, 'path', '') or getattr(request, 'url', {}).get('pathname', '')
        player_name = path.split('/')[-1] if path else None
        
        if not player_name or player_name == '[player_name]':
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({"error": "Player name is required"})
            }
            
        # URL decode the player name
        player_name = unquote(player_name)
        
        data, status_code = get_player_stats(player_name)
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
