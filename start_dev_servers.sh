#!/bin/bash

# Quick development server script for 1Zum.uz

echo "🚀 Starting development servers for 1Zum.uz..."

# Function to start servers in background
start_server() {
    local dir=$1
    local port=$2
    local name=$3
    
    echo "📂 Starting $name server on port $port..."
    cd "$dir" && python3 -m http.server $port &
    echo "✅ $name server started at http://localhost:$port"
}

# Get the project directory
PROJECT_DIR="/Users/admino/Documents/PROJECTS/Goodwell 1ZUM/1Zum.uz"

# Start servers
start_server "$PROJECT_DIR/birzum/templates" 8080 "Templates"
start_server "$PROJECT_DIR/birzum/static" 9000 "Static Assets"

echo ""
echo "🌐 Your servers are now running:"
echo "📄 Templates: http://localhost:8080"
echo "🎨 Static Assets: http://localhost:9000"
echo "🌍 Your existing site: http://localhost:3000/en"
echo ""
echo "📝 To stop all servers, run: pkill -f 'python3 -m http.server'"
echo ""

# Keep script running
wait
