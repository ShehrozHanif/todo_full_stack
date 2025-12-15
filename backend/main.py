"""
Phase II Backend — FastAPI Application Entry Point

Spec Reference: Repository Structure (Mandatory)
Plan Reference: Core Components -> Application Lifecycle
"""
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.db.db import create_db_and_tables
from app.routes.auth import router as auth_router
from app.routes.tasks import router as tasks_router

app = FastAPI(
    title="Todo Full-Stack API",
    description="Phase II - Full-Stack Web Todo Application",
    version="2.0.0",
)

# CORS configuration for frontend communication
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Consistent error response format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.on_event("startup")
def on_startup():
    """Initialize database tables on startup."""
    create_db_and_tables()


@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Todo Full-Stack API v2.0.0"}


@app.get("/health")
def health_check():
    """Health check for deployment verification."""
    return {"status": "healthy"}


# Register routers
app.include_router(auth_router)
app.include_router(tasks_router)
