#!/usr/bin/env python3
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from flask import Flask, redirect, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def root_redirect():
    """Redirect root to the main application"""
    return redirect('/ai/beat-blender/view/')

@app.route('/ai/beat-blender/view')
def view_redirect():
    """Redirect to the main application"""
    return redirect('/ai/beat-blender/view/')

@app.route('/ai/beat-blender/view/')
def serve_index():
    """Serve the main index.html file"""
    return send_from_directory('.', 'index.html')

@app.route('/ai/beat-blender/view/main')
def serve_main():
    """Serve index.html for main route"""
    return send_from_directory('.', 'index.html')

@app.route('/ai/beat-blender/view/share')
def serve_share():
    """Serve index.html for share route"""
    return send_from_directory('.', 'index.html')

@app.route('/ai/beat-blender/view/share/')
def serve_share_trailing():
    """Serve index.html for share route with trailing slash"""
    return send_from_directory('.', 'index.html')

@app.route('/ai/beat-blender/view/share/<path:subpath>')
def serve_share_subpath(subpath):
    """Serve index.html for any share subpath"""
    return send_from_directory('.', 'index.html')

@app.route('/ai/beat-blender/view/about')
def serve_about():
    """Serve index.html for about route"""
    return send_from_directory('.', 'index.html')

@app.route('/ai/beat-blender/view/assets/<path:filename>')
def serve_assets(filename):
    """Serve static assets"""
    return send_from_directory('assets', filename)

@app.route('/ai/beat-blender/view/third_party/<path:filename>')
def serve_third_party(filename):
    """Serve third party files"""
    return send_from_directory('third_party', filename)

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=8080)
