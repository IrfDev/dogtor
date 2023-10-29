#!/bin/bash

echo "Installing $1 package"
source ./.venv/bin/activate
echo "Venv activated on current process"
pip install $1
echo "Pip package installed"
pip freeze > requirements.txt
echo "Requirements file updated"
