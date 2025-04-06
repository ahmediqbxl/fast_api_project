# FastAPI Boilerplate

A boilerplate FastAPI application with basic structure and sample endpoints.

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

## Sample Endpoints

- GET / - Welcome message
- GET /health - Health check
- GET /samples - List all samples
- POST /samples - Create a new sample
- GET /samples/{id} - Get a specific sample
- PUT /samples/{id} - Update a sample
- DELETE /samples/{id} - Delete a sample 
