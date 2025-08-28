# FastAPI Portfolio Backend

## Overview
This portfolio now includes a FastAPI backend that provides REST API endpoints for managing recommendations, skills, and projects data.

## Features
- **Modern UI/UX**: Updated with gradient backgrounds, smooth animations, hover effects, and responsive design
- **FastAPI Backend**: RESTful API with automatic documentation
- **Data Persistence**: JSON file-based data storage for simplicity
- **CORS Support**: Configured for frontend-backend communication
- **Form Validation**: Client-side validation with visual feedback

## API Endpoints

### Recommendations
- `GET /api/recommendations` - Get all recommendations
- `POST /api/recommendations` - Add a new recommendation

### Skills
- `GET /api/skills` - Get all skills with proficiency levels

### Projects
- `GET /api/projects` - Get all projects

### Contact
- `POST /api/contact` - Handle contact form submissions

## Installation & Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the FastAPI server:
```bash
python main.py
```

3. Access the portfolio:
- Portfolio: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative API Docs: http://localhost:8000/redoc

## Data Storage
Data is stored in JSON files in the `data/` directory:
- `data/recommendations.json` - User recommendations
- `data/skills.json` - Skills and proficiency levels
- `data/projects.json` - Portfolio projects

## UI/UX Improvements
- Modern gradient backgrounds
- Smooth hover animations and transitions
- Responsive grid layouts for skills
- Enhanced typography and spacing
- Professional card-based design
- Form validation with visual feedback
- Smooth scrolling navigation

## Technology Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: FastAPI, Python 3.12+
- **Data Storage**: JSON files
- **Styling**: Modern CSS with gradients and animations