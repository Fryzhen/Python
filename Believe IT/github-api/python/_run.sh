#!/usr/bin/env bash

# Load virtual env
source .venv/bin/activate

# Start server
export FLASK_APP=main
flask run