# Migration from webapp2 to Flask

This project has been migrated from the old webapp2 framework to modern Flask.

## Changes Made

### 1. Main Application (`main.py`)
- **Before**: Used webapp2.RequestHandler with a simple redirect class
- **After**: Modern Flask application with proper route decorators
- **Benefits**: 
  - Python 3 compatibility
  - Better error handling
  - More maintainable code structure
  - Built-in development server

### 2. Dependencies (`requirements.txt`)
- **Before**: `webapp2==3.0.0b1`
- **After**: `Flask==3.0.0`, `Werkzeug==3.0.1`
- **Benefits**: 
  - Active maintenance and security updates
  - Better performance
  - Modern Python ecosystem

### 3. App Engine Configuration (`app.yaml`)
- **Before**: `runtime: python27`
- **After**: `runtime: python311`
- **Benefits**:
  - Python 3.11 features and performance
  - Long-term support
  - Better security

## Running the Application

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python run_local.py
# or
python main.py
```

### Google App Engine
```bash
# Deploy to App Engine
gcloud app deploy
```

## Key Features Preserved

1. **URL Routing**: All original routes are preserved
2. **Static File Serving**: Assets and third-party files are served correctly
3. **Redirects**: Root and view redirects work as before
4. **App Engine Compatibility**: Works with Google App Engine Python 3 runtime

## New Features

1. **Development Server**: Built-in Flask development server with auto-reload
2. **Better Error Handling**: Flask provides better error pages and debugging
3. **Modern Python**: Full Python 3.11 compatibility
4. **Extensible**: Easy to add new routes and functionality

## Migration Benefits

- **Security**: Modern dependencies with regular security updates
- **Performance**: Better performance with Python 3.11
- **Maintainability**: Cleaner, more readable code
- **Future-proof**: Active development and community support 