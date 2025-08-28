from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from datetime import datetime

app = FastAPI(title="German Chavarro Portfolio API", version="1.0.0")

# CORS middleware to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class Skill(BaseModel):
    name: str
    years_experience: int
    level: int  # 1-100 for progress bar
    icon: Optional[str] = None

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    image: Optional[str] = None
    demo_url: Optional[str] = None
    repo_url: Optional[str] = None

class Recommendation(BaseModel):
    id: Optional[int] = None
    name: str
    message: str
    created_at: Optional[str] = None

class ContactMessage(BaseModel):
    name: str
    email: str
    message: str

# Data storage files
DATA_DIR = "data"
SKILLS_FILE = os.path.join(DATA_DIR, "skills.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
RECOMMENDATIONS_FILE = os.path.join(DATA_DIR, "recommendations.json")

# Create data directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize data files with sample data if they don't exist
def initialize_data():
    if not os.path.exists(SKILLS_FILE):
        skills = [
            {"name": "Python", "years_experience": 10, "level": 95, "icon": "fab fa-python"},
            {"name": "JavaScript", "years_experience": 2, "level": 70, "icon": "fab fa-js-square"},
            {"name": "HTML5", "years_experience": 2, "level": 80, "icon": "fab fa-html5"},
            {"name": "CSS", "years_experience": 2, "level": 75, "icon": "fab fa-css3-alt"},
            {"name": "Vue.js", "years_experience": 2, "level": 70, "icon": "fab fa-vuejs"},
            {"name": "Java", "years_experience": 1, "level": 60, "icon": "fab fa-java"},
            {"name": "C++", "years_experience": 2, "level": 65, "icon": "fas fa-code"}
        ]
        with open(SKILLS_FILE, 'w') as f:
            json.dump(skills, f, indent=2)
    
    if not os.path.exists(PROJECTS_FILE):
        projects = [
            {
                "title": "Chatbot",
                "description": "Developed a secure website integrated with chatbot for an automobile client using HTML, CSS, JavaScript and IBM Watson Assistant",
                "technologies": ["HTML", "CSS", "JavaScript", "IBM Watson Assistant"],
                "image": None,
                "demo_url": None,
                "repo_url": None
            },
            {
                "title": "Sentiment Analyzer",
                "description": "Developed and deployed a sentiment analyzer for the box reviews section of an eCommerce platform using IBM NLU",
                "technologies": ["Python", "IBM NLU", "Machine Learning"],
                "image": None,
                "demo_url": None,
                "repo_url": None
            },
            {
                "title": "Fashion Website",
                "description": "Created a styled multi-page website for a new player in the fashion industry and integrated it with a shopping cart, using stripe for payment gateway",
                "technologies": ["HTML", "CSS", "JavaScript", "Stripe API"],
                "image": None,
                "demo_url": None,
                "repo_url": None
            }
        ]
        with open(PROJECTS_FILE, 'w') as f:
            json.dump(projects, f, indent=2)
    
    if not os.path.exists(RECOMMENDATIONS_FILE):
        recommendations = [
            {
                "id": 1,
                "name": "Previous Colleague",
                "message": "German is a very quick learner and quickly grasps key concepts of Web development. He got a great attitude & he is an excellent team player. He has a curious mind and asks the right question. He takes initiative within a team and has potentials to lead the team.",
                "created_at": "2023-01-15T10:30:00"
            },
            {
                "id": 2,
                "name": "Former Manager",
                "message": "Working with German has been an awesome experience. He is highly knowledgable and always goes the extra step to make sure everything is right. For any future projects that need his expertise I would definitely want to work with him again.",
                "created_at": "2023-02-20T14:15:00"
            },
            {
                "id": 3,
                "name": "Client",
                "message": "I had worked along with German during the initial phase of our venture which needed Web development. He is a committed resource who has in depth knowledge about the domain. He will be an asset for any organisation!",
                "created_at": "2023-03-10T09:45:00"
            }
        ]
        with open(RECOMMENDATIONS_FILE, 'w') as f:
            json.dump(recommendations, f, indent=2)

initialize_data()

# Helper functions
def load_json_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_json_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

# API endpoints
@app.get("/api/")
async def api_root():
    return {"message": "German Chavarro Portfolio API", "version": "1.0.0"}

@app.get("/api/skills", response_model=List[Skill])
async def get_skills():
    """Get all skills"""
    return load_json_data(SKILLS_FILE)

@app.get("/api/projects", response_model=List[Project])
async def get_projects():
    """Get all projects"""
    return load_json_data(PROJECTS_FILE)

@app.get("/api/recommendations", response_model=List[Recommendation])
async def get_recommendations():
    """Get all recommendations"""
    return load_json_data(RECOMMENDATIONS_FILE)

@app.post("/api/recommendations", response_model=Recommendation)
async def create_recommendation(recommendation: Recommendation):
    """Create a new recommendation"""
    recommendations = load_json_data(RECOMMENDATIONS_FILE)
    
    # Generate new ID
    new_id = max([r.get("id", 0) for r in recommendations], default=0) + 1
    
    # Create new recommendation
    new_recommendation = {
        "id": new_id,
        "name": recommendation.name,
        "message": recommendation.message,
        "created_at": datetime.now().isoformat()
    }
    
    recommendations.append(new_recommendation)
    save_json_data(RECOMMENDATIONS_FILE, recommendations)
    
    return new_recommendation

@app.post("/api/contact")
async def create_contact_message(contact: ContactMessage):
    """Handle contact form submission"""
    # In a real application, you might send an email or save to database
    print(f"New contact message from {contact.name} ({contact.email}): {contact.message}")
    return {"message": "Contact message received successfully"}

# Serve static files (CSS, JS, images, etc.)
@app.get("/script.js")
async def serve_script():
    return FileResponse("script.js", media_type="application/javascript")

@app.get("/style.css") 
async def serve_style():
    return FileResponse("style.css", media_type="text/css")

@app.get("/images/{file_path:path}")
async def serve_images(file_path: str):
    return FileResponse(f"images/{file_path}")

@app.get("/icons/{file_path:path}")
async def serve_icons(file_path: str):
    return FileResponse(f"icons/{file_path}")

# Serve the main HTML file at root
@app.get("/")
async def serve_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)