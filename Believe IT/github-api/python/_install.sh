#!/usr/bin/env bash

# Create virtual env and install dependencies
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
