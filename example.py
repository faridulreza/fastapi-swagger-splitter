"""
Example usage of fastapi-swagger-splitter
"""
from fastapi import FastAPI
from fastapi_swagger_splitter import setup_swagger_splitter

# Create FastAPI app
app = FastAPI(
    title="Example API",
    description="An example API using fastapi-swagger-splitter",
    version="1.0.0",
    docs_url=None,  # Disable default docs
    openapi_url="/openapi.json",
)

# Setup custom Swagger UI
setup_swagger_splitter(app, swagger_path="/docs")


@app.get("/", tags=["General"])
async def root():
    """Root endpoint"""
    return {"message": "Hello World"}


@app.get("/users", tags=["Users"])
async def get_users():
    """Get all users"""
    return {"users": []}


@app.post("/users", tags=["Users"])
async def create_user():
    """Create a new user"""
    return {"message": "User created"}


@app.get("/posts", tags=["Posts"])
async def get_posts():
    """Get all posts"""
    return {"posts": []}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
