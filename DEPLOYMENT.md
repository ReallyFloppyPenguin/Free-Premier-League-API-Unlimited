# Vercel Deployment Guide

## Quick Deployment

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy to Vercel**
   ```bash
   vercel
   ```
   Follow the prompts:
   - Link to existing project or create new
   - Choose framework: Other
   - Build command: (leave empty)
   - Output directory: (leave empty)

3. **Your API is live!**
   After deployment, you'll get a URL like: `https://premier-league-api-xyz.vercel.app`

## API Endpoints

- **GET /** - API documentation
- **GET /api/players/[player_name]** - Player statistics
- **GET /api/fixtures** - All Premier League fixtures
- **GET /api/fixtures?team=[team_name]** - Team-specific fixtures
- **GET /api/table** - Premier League table

## Example Usage

```bash
# Get player stats
curl https://your-domain.vercel.app/api/players/ronaldo

# Get all fixtures
curl https://your-domain.vercel.app/api/fixtures

# Get Arsenal fixtures
curl https://your-domain.vercel.app/api/fixtures?team=arsenal

# Get league table
curl https://your-domain.vercel.app/api/table
```

## Features

- ✅ Serverless functions for optimal performance
- ✅ CORS enabled for frontend integration
- ✅ Error handling and validation
- ✅ Auto-scaling with Vercel
- ✅ Zero server maintenance

## Environment Variables

No environment variables required. The API scrapes data from public sources.

## Limitations

- Google Search API has rate limits
- Web scraping depends on target site structure
- Some endpoints may be slower due to external API calls

## Troubleshooting

If deployment fails:
1. Check `vercel.json` syntax
2. Ensure all dependencies are in `requirements.txt`
3. Verify Python function signatures match Vercel requirements
