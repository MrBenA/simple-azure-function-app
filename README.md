# Simple Azure Function App

A minimal Azure Function App project using Python v2 programming model, designed for deployment via Azure Portal's GitHub integration.

## Features

- **Health Check Endpoint** (`/health`) - JSON health status
- **Test Endpoint** (`/test`) - Basic connectivity test  
- **Hello World Endpoint** (`/hello`) - Personalized greeting with optional name parameter

## Quick Start

### Deploy to Azure
1. Create Azure Function App in portal (Python 3.11, Consumption plan)
2. Configure GitHub deployment source pointing to this repository
3. Test endpoints at `https://your-app.azurewebsites.net/health`

### Local Development
```bash
pip install -r requirements.txt
func start
```

Then test at `http://localhost:7071/health`

## Project Structure

```
├── function_app.py    # Main function definitions
├── host.json         # Azure Functions configuration
├── requirements.txt  # Python dependencies
├── README.md        # This file
└── CLAUDE.md        # Claude Code guidance
```

## Configuration

- **Runtime**: Python 3.11
- **Functions Version**: ~4
- **Authentication**: Anonymous (for simplicity)
- **Deployment**: Azure Portal GitHub integration

## Endpoints

- `GET /health` - Health check with JSON response
- `GET /test` - Simple test message
- `GET /hello?name=YourName` - Personalized greeting

## Documentation

See [CLAUDE.md](CLAUDE.md) for comprehensive setup instructions, troubleshooting, and development guidelines.

## Support

This is a simplified demonstration project. For production use, consider adding:
- Authentication and authorization
- Error handling and validation
- Monitoring and logging
- Infrastructure as Code
- CI/CD pipelines