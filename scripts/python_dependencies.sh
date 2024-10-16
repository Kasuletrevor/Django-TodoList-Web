#!/usr/bin/env bash
set -e

PROJECT_MAIN_DIR_NAME="Django-TodoList-Web"

# Validate variables
if [ -z "$PROJECT_MAIN_DIR_NAME" ]; then
    echo "Error: PROJECT_MAIN_DIR_NAME is not set. Please set it to your project directory name." >&2
    exit 1
fi

# Change ownership to ubuntu user
sudo chown -R ubuntu:ubuntu "/home/ubuntu/$PROJECT_MAIN_DIR_NAME"

# Update package list and install python3-venv
sudo apt update -y
sudo apt install python3-venv -y

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv" 
# Activate virtual environment
echo "Activating virtual environment..."
source "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/venv/bin/activate"

# Install dependencies
echo "Installing Python dependencies..."
pip install -r "/home/ubuntu/$PROJECT_MAIN_DIR_NAME/requirements.txt"

echo "Dependencies installed successfully."
