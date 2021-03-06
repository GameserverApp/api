#!/usr/bin/env python3
"""
SteamCMD API global configuration.
"""

# allowed HTTP methods
ALLOWED_METHODS = ["GET", "HEAD", "OPTIONS"]

# allowed api version
ALLOWED_VERSIONS = ["v1"]

# available endpoints
AVAILABLE_ENDPOINTS = ["info", "version"]

# file containing version
VERSION_FILE = ".version"
