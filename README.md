# FastAPI Boilerplate

A boilerplate FastAPI application with basic structure and sample endpoints, including NBA API integration.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

The application will be available at http://localhost:8000

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
.
├── app/
│   ├── models/         # Pydantic models
│   └── routers/        # API routers
├── main.py            # Main application file
└── requirements.txt   # Project dependencies
```

## Available Endpoints

### Sample Endpoints
- GET / - Welcome message
- GET /health - Health check
- GET /samples - List all samples
- POST /samples - Create a new sample
- GET /samples/{id} - Get a specific sample
- PUT /samples/{id} - Update a sample
- DELETE /samples/{id} - Delete a sample

### NBA API Endpoints
- GET /nba/players - Get all NBA players
- GET /nba/teams - Get all NBA teams
- GET /nba/player/{player_id}/career - Get career stats for a specific player
- GET /nba/player/{player_id}/info - Get basic information for a specific player

## Testing the API

1. Start the application as described in the Setup section.

2. Access the Swagger UI at http://localhost:8000/docs to interact with the API endpoints.

3. Example API calls:

```bash
# Get all NBA players
curl http://localhost:8000/nba/players

# Get all NBA teams
curl http://localhost:8000/nba/teams

# Get player career stats (replace {player_id} with actual ID)
curl http://localhost:8000/nba/player/{player_id}/career

# Get player information (replace {player_id} with actual ID)
curl http://localhost:8000/nba/player/{player_id}/info
```

Note: Player IDs can be found in the response from the `/nba/players` endpoint. 
