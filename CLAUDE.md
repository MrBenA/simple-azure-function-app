# CLAUDE.md - Simple Azure Function App

This file provides guidance to Claude Code (claude.ai/code) when working with this simplified Azure Function App project.

## Project Overview

This is a simplified Azure Function App project that demonstrates the Python v2 programming model with basic HTTP-triggered functions. The project is designed to be deployed via Azure Portal's GitHub integration rather than complex CI/CD pipelines.

**Key Design Principles:**
- **Simplicity First**: Minimal configuration, basic authentication
- **Portal-based Deployment**: Uses Azure Portal's built-in GitHub deployment
- **Easy Debugging**: Clear separation of concerns, comprehensive logging
- **Foundation for Growth**: Can be extended with more complex features later

## Project Structure

```
simple-function-app/
├── function_app.py          # Main function definitions (Python v2 model)
├── host.json               # Azure Functions host configuration
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── CLAUDE.md              # This file - Claude Code guidance
└── .gitignore             # Git ignore patterns
```

## Functions Included

### 1. Health Check (`/health`)
- **Purpose**: Simple health monitoring endpoint
- **Method**: GET
- **Response**: JSON with status, timestamp, and version
- **Auth**: Anonymous access
- **Example**: `GET https://your-app.azurewebsites.net/health`

### 2. Test Endpoint (`/test`)
- **Purpose**: Basic connectivity test
- **Method**: GET
- **Response**: Plain text confirmation message
- **Auth**: Anonymous access
- **Example**: `GET https://your-app.azurewebsites.net/test`

### 3. Hello World (`/hello`)
- **Purpose**: Demonstrates parameter handling
- **Method**: GET/POST
- **Parameters**: `name` (optional, via query string or JSON body)
- **Response**: Personalized greeting
- **Auth**: Anonymous access
- **Examples**: 
  - `GET https://your-app.azurewebsites.net/hello`
  - `GET https://your-app.azurewebsites.net/hello?name=Alice`

## Azure Portal Setup Instructions

### Step 1: Create Function App
1. **Navigate to Azure Portal** → Create a resource → Function App
2. **Basic Configuration**:
   - **Subscription**: Your Azure subscription
   - **Resource Group**: Create new or select existing
   - **Function App Name**: Choose a unique name (e.g., `simple-func-app-[your-initials]`)
   - **Runtime Stack**: Python
   - **Version**: 3.11
   - **Region**: Choose your preferred region

3. **Hosting Configuration**:
   - **Plan Type**: Consumption (Serverless)
   - **Storage Account**: Create new or use existing

4. **Review + Create** → Wait for deployment to complete

### Step 2: Configure GitHub Deployment
1. **Go to your Function App** → Deployment → Deployment Center
2. **Source**: GitHub
3. **Organization**: Your GitHub username
4. **Repository**: Select the repository created for this project
5. **Branch**: main
6. **Build Provider**: App Service Build Service
7. **Save** → Azure will automatically deploy from GitHub

### Step 3: Configure App Settings
1. **Go to Configuration** → Application Settings
2. **Verify these settings exist**:
   - `FUNCTIONS_WORKER_RUNTIME` = `python`
   - `FUNCTIONS_EXTENSION_VERSION` = `~4`
   - `AzureWebJobsStorage` = (automatically configured)
   - `WEBSITE_RUN_FROM_PACKAGE` = `1` (if using package deployment)

### Step 4: Test the Deployment
1. **Wait for deployment** to complete (check Deployment Center logs)
2. **Test endpoints**:
   - Health: `https://your-app.azurewebsites.net/health`
   - Test: `https://your-app.azurewebsites.net/test`
   - Hello: `https://your-app.azurewebsites.net/hello?name=YourName`

## Local Development

### Prerequisites
- Python 3.11
- Azure Functions Core Tools
- Azure CLI (optional, for deployment)

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
func start
```

### Testing Locally
- Health: `http://localhost:7071/health`
- Test: `http://localhost:7071/test`
- Hello: `http://localhost:7071/hello?name=Test`

## Troubleshooting

### Common Issues

**1. Functions Not Appearing**
- Check Azure Portal → Function App → Functions
- Verify deployment completed successfully
- Check Application Insights logs for startup errors

**2. Endpoints Not Responding**
- Verify function app is running (Overview → Status)
- Check function logs in Azure Portal
- Ensure correct URL format: `https://your-app.azurewebsites.net/function-name`

**3. Deployment Failures**
- Check Deployment Center logs
- Verify repository permissions
- Ensure all required files are in repository root

### Log Locations
- **Azure Portal**: Function App → Monitor → Logs
- **Application Insights**: Function App → Application Insights
- **Deployment Logs**: Function App → Deployment Center → Logs

## Development Guidelines

### Adding New Functions
1. Add new function to `function_app.py` using `@app.route()` decorator
2. Follow naming conventions: lowercase with hyphens
3. Include logging and error handling
4. Test locally before deploying

### Code Standards
- Use type hints where appropriate
- Include docstrings for all functions
- Follow PEP 8 style guidelines
- Add appropriate logging statements

### Security Considerations
- Currently uses anonymous authentication for simplicity
- For production, consider implementing proper authentication
- Validate input parameters
- Use HTTPS endpoints only

## Future Enhancements

This simplified setup can be extended with:
- Authentication and authorization
- Database integration
- External API calls
- Timer-triggered functions
- Queue-triggered functions
- Infrastructure as Code (Bicep/ARM templates)
- CI/CD pipelines
- Monitoring and alerting

## Comparison with Complex Setup

**This Simple Approach**:
- ✅ Quick to set up and deploy
- ✅ Easy to debug and troubleshoot
- ✅ Uses Azure's built-in deployment
- ✅ Minimal configuration required

**Complex IaC Approach**:
- ⚠️ More setup complexity
- ⚠️ Requires understanding of Bicep/ARM
- ✅ Better for production environments
- ✅ Supports managed identity and advanced features

## Support and Maintenance

- **Primary Focus**: Keep it simple and working
- **Updates**: Minimal - only when necessary
- **Extensions**: Add complexity incrementally
- **Documentation**: Keep this file updated with any changes

---

**Last Updated**: 2025-07-17
**Status**: Active Development
**Next Steps**: Create GitHub repository and test Azure Portal deployment