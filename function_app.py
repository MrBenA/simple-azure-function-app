import azure.functions as func
import logging
import json
from datetime import datetime

app = func.FunctionApp()

@app.route(route="health", auth_level=func.AuthLevel.ANONYMOUS)
def health(req: func.HttpRequest) -> func.HttpResponse:
    """Simple health check endpoint"""
    logging.info('Health check requested')
    
    health_data = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }
    
    return func.HttpResponse(
        json.dumps(health_data),
        status_code=200,
        mimetype="application/json"
    )

@app.route(route="test", auth_level=func.AuthLevel.ANONYMOUS)
def test(req: func.HttpRequest) -> func.HttpResponse:
    """Simple test endpoint"""
    logging.info('Test endpoint requested')
    
    return func.HttpResponse(
        "Hello from Azure Functions! This is a simple test endpoint.",
        status_code=200
    )

@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    """Hello world endpoint with optional name parameter"""
    logging.info('Hello endpoint requested')
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name') if req_body else None
    
    if name:
        response_text = f"Hello, {name}! Welcome to Azure Functions."
    else:
        response_text = "Hello, World! Welcome to Azure Functions. Pass a 'name' parameter to personalize this message."
    
    return func.HttpResponse(
        response_text,
        status_code=200
    )