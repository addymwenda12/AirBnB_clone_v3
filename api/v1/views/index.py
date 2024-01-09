#!/usr/bin/python3
"""Creates a route on app_views"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON response for status"""
    return jsonify({"status": "OK"})
