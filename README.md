# MindCare Burundi

![image](https://github.com/user-attachments/assets/3185023a-261d-44c0-a634-da654600586d)


# MindCare - Mental Health Support Platform

## Overview
MindCare is a comprehensive mental health platform designed to support users in managing their well-being. It offers educational resources, access to professional support, and self-assessment quizzes. The platform enables users to take quizzes to evaluate their mental health, schedule appointments with mental health professionals, and explore curated content related to mental wellness. MindCare aims to provide a safe and accessible space for individuals to gain insights into their mental health and seek guidance when needed.

## Features
- **Personalized Mental Health Dashboard** – Users can track their mental well-being, set personal goals, and access relevant resources.
- **Book Appointment** – Schedule sessions with licensed mental health professionals for personalized support.
- **Mental Health Quizzes** – Quizzes about mental health organize in each category
- **Mental health support space** – Join a safe and moderated community where users can share experiences, seek advice, and provide support to others.
- **Contact** – Provides crisis intervention information and direct contact with professional helplines.
- **Mental Health Ressource Center** – Provides curated content to promote well-being and positive mental habits.
  
# Link to the video demo of MindCare App.

https://youtu.be/sWvQSMP69EI

# Link to the deployed version of MindCare App

https://mindcare-burundi.onrender.com

# Screenshots of the app interface can be found this the **designs folder** of this repository

https://github.com/Ericanshimir/MindCare-Burundi/tree/main/MindCare/designs

# Tech Stack

**Backend:**

1. Python (Django Framework)

2. SQLite (Lightweight Database)

3. Gunicorn (WSGI Server for production)

4. Deployed on Render

**Frontend:**

1. HTML (Page structure)

2. CSS (Styling)

3. JavaScript (Interactivity)

# Running MindCare-Burundi on Render

# 1. Deploy Backend on Render

1. Log in to Render.

2. Click "New Web Service" and connect your GitHub repository.

3. Select Django Backend Repository and choose a branch (main).

4. Set the build and start commands:
```bash
Build Command: pip install -r requirements.txt
Start Command: gunicorn eyt.wsgi:application
```
**Configure environment variables in Render Dashboard → Environment:**

1. DATABASE_URL
2. SECRET_KEY
3. DEBUG → False

Click **"Deploy"** and wait for it to finish.

# 2. Deploy Frontend

1. Since the frontend is built with HTML, CSS, and JavaScript, you can:

2. Use GitHub Pages (for free hosting).

3. Upload the files to Render Static Site.

4. Deploy on any web server (e.g., Apache, Nginx).

**To deploy on Render Static Site:**

1. Go to Render.

2. Click **"New Static Site"**.

3. Select the frontend folder in your repository.

4. **Configure:**
```bash
Build Command: None (as it's static)
Publish Directory: frontend/
```
5. Click **Deploy** and copy the link.

# Usage

Visit the deployed app https://mindcare-burundi.onrender.com.

**Sign Up/Login:** Create an account or log in.

**Access training materials:** Read mental health articles and guides.

**Engage in Discussions:** Join community forums.

**Take Self-Assessment quizzes:** Evaluate your mental wellness.

**Consult Professionals:** Book appointments with experts.


# Steps to Run the App Locally

**1. Clone the Repository**
   ```sh
   https://github.com/Ericanshimir/MindCare-Burundi.git
   cd MindCare
   ```
**2. Install dependencies**
```bash
 pip install -r requirements.txt
```
**3. Create a Virtual Environment and Activate It**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
**4. Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
**5. Apply Migrations**
   ```sh
  python manage.py makemigrations
  python manage.py migrate
   ```
**6. Create Superuser (For Admin Access)**
```sh
python manage.py createsuperuser
```
**7. Run the Application**
   ```sh
  python manage.py runserver
   ```
**8. Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

### **Project Structure**


### **Project Structure**

| **Directory/File**        | **Description** |
|---------------------------|--------------------------------------------------|
| `MindCare-Burundi/`       | Main project repository |
| `MindCare/`               | Main Django project folder (settings, URLs, WSGI) |
| `MindCare/chat/`          | Chat-related functionalities |
| `MindCare/designs/`       | Design-related files |
| `MindCare/env/`           | Environment-related configurations |
| `MindCare/eyt/`           | Project-specific logic and settings |
| `MindCare/eyt/__init__.py`| Initializes the `eyt` package |
| `MindCare/eyt/settings.py`| Django settings file |
| `MindCare/eyt/urls.py`    | URL configurations |
| `MindCare/eyt/wsgi.py`    | WSGI entry point for the project |
| `MindCare/eyt/vercel.json`| Deployment configuration for Vercel |
| `git-filter-repo/`        | Git-related filters (if applicable) |
| `locale/`                 | Localization files for translations |
| `media/`                  | Uploaded media files |
| `media/books/`            | Book-related media |
| `media/professionals/`    | Media for professionals |
| `media/Video/`            | Uploaded video files |
| `media/videos/`           | Additional video files |
| `myapp/`                  | Django application module |
| `myapp/__pycache__/`      | Compiled Python files |
| `myapp/locale/`           | Localization files for translations |
| `myapp/migrations/`       | Database migration files |
| `myapp/templates/`        | Template files for the project |
| `myapp/templates/myapp/`  | Templates for the core application |
| `myapp/templates/professionals/` | Templates for professionals section |
| `myapp/templates/about.html` | About page template |
| `static/`                 | Static files such as CSS and JavaScript |
| `static/assets/`          | Assets for styling and functionality |
| `static/css/`             | CSS stylesheets |
| `static/style.css`        | Main stylesheet file |
| `staticfiles/`            | Additional static files |
| `staticfiles/admin/`      | Static files for admin panel |
| `staticfiles/assets/`     | Extra assets |
| `staticfiles/css/`        | Extra stylesheets |
| `staticfiles/style.css`   | Extra stylesheet file |
| `venv/`                   | Virtual environment directory |
| `.gitignore`              | Git ignore file for ignoring unnecessary files |
| `backup.sql`              | Backup of the database |
| `db.sqlite3`              | SQLite database file |
| `manage.py`               | Django management script |
| `mindcare_schema.dbml`    | Database schema file (for documentation or modeling) |
| `render.yaml`             | Render deployment configuration |
| `requirements.txt`        | Python dependencies list |
| `schema.sql`              | SQL schema file |
| `.env`                    | Environment variables (not included in Git) |
| `README.md`               | Project documentation |

## Contribution
To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to your branch: `git push origin feature-branch-name`.
5. Open a Pull Request.

## Contact
For any inquiries, suggestions, or feedback, feel free to open an issue on GitHub or contact us via email at e.nshimirim@alustudent.com.
