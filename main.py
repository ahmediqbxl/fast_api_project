from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sample

app = FastAPI(
    title="FastAPI Boilerplate",
    description="A boilerplate FastAPI application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(sample.router)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Boilerplate"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 