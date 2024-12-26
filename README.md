
# FlavorFusion 🌟  
A user-friendly platform for food enthusiasts to share and explore recipes with detailed descriptions and photos. Create, browse, and get inspired by a world of flavors!  

## Features 🚀  
- **Add Recipes**: Users can upload their own recipes with titles, descriptions, and images.  
- **Explore Recipes**: Discover a wide variety of recipes shared by other users in the recipes section.  
- **Search Functionality**: Quickly find recipes using keywords.  
- **Update and Delete Recipes**: Manage your own recipes with ease.  
- **Secure Authentication**: Login and registration ensure a personalized experience.  

## Tech Stack 💻  
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Django  
- **Database**: SQLite/MySQL  
- **Authentication**: Django’s built-in user model  

## Installation Guide 🔧  
Follow these steps to set up the project locally:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/FlavorFusion.git
   ```  

2. Navigate to the project directory:  
   ```bash
   cd FlavorFusion
   ```  

3. Create a virtual environment and activate it:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```  

4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

5. Run database migrations:  
   ```bash
   python manage.py migrate
   ```  

6. Start the development server:  
   ```bash
   python manage.py runserver
   ```  

7. Access the website: Open your browser and navigate to `http://127.0.0.1:8000/`.  

## Usage 🥘  
1. Register an account or log in to start adding your recipes.  
2. Upload a recipe by providing a name, description, and photo.  
3. Browse and search for recipes in the "Recipes" section.  
4. Update or delete your recipes as needed.  

