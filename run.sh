#!/bin/bash
# Quick Start Script for Plant Disease Fuzzy Diagnosis System

echo "🌿 Starting Plant Disease Fuzzy Diagnosis System..."
echo "=================================================="
echo ""

# Navigate to project directory
cd "/home/hasan-faisal/university/5th semester/krr/project"

# Check if dependencies are installed
echo "Checking dependencies..."
python -c "import skfuzzy, gradio, matplotlib, numpy" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed"
else
    echo "❌ Missing dependencies. Installing..."
    uv pip install -r requirements.txt
fi

echo ""
echo "🚀 Launching application..."
echo "=================================================="
echo ""
echo "📍 Application will be available at:"
echo "   http://127.0.0.1:7860"
echo ""
echo "Press Ctrl+C to stop the application"
echo "=================================================="
echo ""

# Launch the application
python main.py
