#!/bin/bash

echo "Starting MCS Manager..."

# Step 1: Install Backend Dependencies
echo "Installing backend dependencies..."
cd backend || exit
pip install --user -r requirements.txt

# Step 2: Start Flask Backend
echo "Starting Flask backend..."
python3 app.py &  # <-- Changed to python3

# Step 3: Start Frontend (if using React/Vue)
if [ -d "../frontend" ]; then
    echo "Installing frontend dependencies..."
    cd ../frontend || exit
    if command -v npm &> /dev/null; then  # Check if npm exists
        npm install
        echo "Starting frontend..."
        npm start &
    else
        echo "⚠️  npm not found! Skipping frontend."
    fi
fi

# Step 4: Start Desktop App (if needed)
if [ -f "../desktop/desktop.py" ]; then
    echo "Starting desktop app..."
    cd ../desktop || exit
    python3 desktop.py &  # <-- Changed to python3
fi

echo "All services started!"
wait  # Keep script running
