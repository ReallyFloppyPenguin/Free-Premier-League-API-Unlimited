<h1>Premier League API 2.0</h1>
	<p>This is an unofficial Premier League API client for pulling player stats, fixtures, tables, and results data from the Premier League. The API is built using Flask, and the data is scraped from the Premier League website.</p>

>We have hosted it onto vercel here (

<p>Thank to https://github.com/tarun7r for the original code</p>

<h2>API Endpoints</h2>

<p>The application provides the following API endpoints:</p>
<h3>GET  /players/{player_name}</h3>
<p>This endpoint retrieves information about a Premier League player with the given name. The player name should be provided as a URL parameter.</p>
<p>The API returns a JSON object with the following structure:</p>
<pre><code>[
        {
          'name': name, 
          'position': position, 
          'club': club, 
          'Nationality': nationality, 
          'Date of Birth': dob,
          'height':height,
          'key_stats': all_stats
          }
]</code></pre>


<h3>GET /table</h3>
<p>The JSON object contains an array of strings, where each string represents a team's position, name, number of games played, wins, draws, losses, goal difference, and total points.</p>
<p>The API returns a JSON object with the following structure:</p>
<pre><code>[
      "Position",
      "Team",
      "Played",
      "Wins",
      "Draws",
      "Losses",
      "Goal Difference",
      "Points"
    ]</code></pre>

<h3>GET /fixtures/{team_name}</h3>
<p>This endpoint retrieves information about the next Three Premier League fixtures of the team. The team name should be provided as a URL parameter.</p>
<p>The API returns a JSON object with the following structure:</p>
<pre><code>[ { "Team A vs Team B DD/MM/YYYY HH:MM", "Team A vs Team C DD/MM/YYYY HH:MM", "Team A vs Team D DD/MM/YYYY HH:MM"} ] </code></pre>

<h2>Setup Details</h2>

### Local Development
Follow the following instructions to run the application locally:
<li>Clone the repository</li>
<li>Open the terminal, navigate to the folder where your clone of this repository is located and type:
  
  `$ pip install -r requirements.txt` </li>

<li> Type $ python main.py in the terminal and the script will run for as long as you let it. </li>

### Vercel Deployment (Recommended)
This API is now optimized for Vercel serverless deployment:

<li>Install Vercel CLI: `npm install -g vercel`</li>
<li>Clone the repository and navigate to the project folder</li>
<li>Run `vercel` in the terminal and follow the prompts</li>
<li>Your API will be deployed to a Vercel URL (e.g., https://your-project.vercel.app)</li>

### API Endpoints (Vercel)
Once deployed on Vercel, use these endpoints:
- `GET /api/players/{player_name}` - Get player statistics
- `GET /api/fixtures` - Get all fixtures  
- `GET /api/fixtures?team={team_name}` - Get fixtures for specific team
- `GET /api/table` - Get Premier League table
- `GET /` - API documentation and welcome message



<H2>Individual PLayer PL Stats</H2> 
<ul>
  <li>Example: Stats of Cristiano Ronaldo | One can use the common name of the Players as well to retrive the data</li>
  <br> <img src="assets/player_stats.png"><br>
</ul>
 <H2>Premier League Table</H2> 
<ul>
  <li>Current Premier League Table</li>
  <br> <img src="assets/table.png"><br>
 </ul>
 <H2>Premier League Fixtures </H2> 
<ul>
  <li>Fixtures of the Next three weeks </li>
  <br> <img src="assets/fixtures.png"> <br>
 </ul>
<H2>Update 🚀 </H2>
The API has been enhanced with new features and improvements:
<ul>
  <li>✨ Optimized the code for better performance.</li>
  <li>🔄 Rebased and updated to ensure compatibility with the latest dependencies.</li>
</ul>
You can also search player stats using the player's reference image ( Face Recognition ) as well - <a href=https://github.com/tarun7r/Premier-League-Face-Recognition>Repo</a> 📸

<H2>Disclaimer</H2>
This project is created solely for learning and educational purposes. It is not intended for production-level use or commercial applications
