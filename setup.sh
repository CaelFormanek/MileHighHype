#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# 1. Set up a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# 2. Upgrade pip
echo "Upgrading pip..."
source venv/bin/activate
pip install --upgrade pip

# 3. Install required packages from requirements.txt
if [ -f requirements.txt ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
else
    echo "No requirements.txt file found, skipping package installation."
fi

# 4. Keep the environment activated for the user's shell session
echo "Setup complete! Your virtual environment is now active."
echo "To deactivate it, run 'deactivate'."
