#!/usr/bin/env python3
"""
Local development server for Beat Blender
Run this script to start the Flask development server
"""

from main import app

if __name__ == '__main__':
    print("Starting Beat Blender development server...")
    print("Server will be available at: http://localhost:8080")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=8080) 