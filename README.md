# Django TodoList Web Application

## Overview

This is a web-based task management application built with Django framework. The application provides a comprehensive todolist system with task categorization, status tracking, and an intuitive user interface for managing personal and professional tasks.

## Project Context

This application was developed as a demonstration project for testing deployment procedures to Amazon EC2 instances in the Cloud Computing course at Masters level. The repository is publicly accessible as it was forked from another repository for educational purposes, specifically to practice cloud deployment workflows and infrastructure management.

## Features

- **Task Management**: Create, read, update, and delete tasks with detailed information
- **Category System**: Organize tasks into custom categories for better organization
- **Status Tracking**: Track task progress through multiple states:
  - Todo: Tasks that need to be started
  - Ongoing: Tasks currently in progress
  - Done: Completed tasks
  - Abandoned: Tasks that were discontinued
- **Due Date Management**: Set and track task deadlines with timezone support (Asia/Jakarta)
- **Dynamic UI**: Interactive interface with real-time updates using HTMX
- **Admin Panel**: Django administration interface for advanced management

## Technology Stack

### Backend
- **Python**: Programming language
- **Django 4.2.26**: Web framework
- **SQLite**: Database system
- **Gunicorn 21.2.0**: WSGI HTTP Server

### Frontend
- **HTML/CSS**: Structure and styling
- **Bootstrap**: Responsive design framework
- **Font Awesome**: Icon library
- **HTMX**: Dynamic HTML updates
- **Django Widget Tweaks**: Form rendering utilities

### Deployment
- **WhiteNoise**: Static file serving
- **Gunicorn**: Production web server
- **systemd**: Service management on Linux

## Installation

### Prerequisites
- Python 3.x installed
- pip (Python package installer)
- Virtual environment (recommended)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Kasuletrevor/Django-TodoList-Web.git
cd Django-TodoList-Web
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the application at `http://localhost:8000`

## Deployment to AWS EC2

This application includes automated deployment scripts specifically designed for AWS EC2 instances.

### Deployment Files
- **userdata.sh**: EC2 user data script for initial setup
- **scripts/instance_os_dependencies.sh**: Installs system-level dependencies
- **scripts/python_dependencies.sh**: Installs Python packages
- **scripts/gunicorn.sh**: Configures Gunicorn as a systemd service
- **scripts/start_app.sh**: Application startup script

### EC2 Deployment Steps

1. Launch an EC2 instance (Ubuntu recommended)
2. Use the provided `userdata.sh` as user data during instance creation, or run it manually:
```bash
chmod +x userdata.sh
./userdata.sh
```

The script will automatically:
- Clone the repository
- Install all dependencies
- Configure Gunicorn service
- Start the application

3. Configure security groups to allow HTTP/HTTPS traffic
4. Access the application via the EC2 instance's public IP or DNS

## Project Structure

```
Django-TodoList-Web/
├── AuroraTech/          # Django project settings
│   ├── settings.py      # Application configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── todolist/            # Main application
│   ├── models.py        # Database models (Task, Category, Status)
│   ├── views.py         # Application views and logic
│   ├── forms.py         # Form definitions
│   └── admin.py         # Admin interface configuration
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── staticfiles/         # Collected static files for production
├── scripts/             # Deployment automation scripts
├── gunicorn/            # Gunicorn configuration
├── requirements.txt     # Python dependencies
└── manage.py            # Django management script
```

## Database Schema

### Task Model
- title: Task name
- description: Detailed task information
- due_date: Task deadline
- category_id: Foreign key to Category
- status_id: Foreign key to Status

### Category Model
- name: Category name
- description: Category description

### Status Model
- name: Status name (Todo, Ongoing, Done, Abandoned)
- description: Status description

## Configuration

### Settings
The application settings can be modified in `AuroraTech/settings.py`:
- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Configure for your domain
- **SECRET_KEY**: Change to a secure random key in production
- **TIME_ZONE**: Currently set to 'Asia/Jakarta'

### Security Considerations
- The current SECRET_KEY is for development only
- DEBUG mode should be disabled in production
- Configure proper ALLOWED_HOSTS in production
- Implement proper database security measures
- Use environment variables for sensitive configuration

## Usage

### Managing Tasks
1. Navigate to the task list page
2. Click "Add Task" to create a new task
3. Fill in task details (title, description, category, status, due date)
4. Tasks are organized by status columns
5. Edit or delete tasks using the action buttons

### Managing Categories
1. Navigate to the categories page
2. Create custom categories to organize tasks
3. Assign categories when creating or editing tasks

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Admin Panel
Visit `http://localhost:8000/admin` and login with superuser credentials

## Contributing

As this is an educational project, contributions should align with the learning objectives of cloud deployment and Django web development.

## License

This project is available for educational purposes.

## Acknowledgments

This repository was forked from an original todolist application and adapted for cloud computing deployment exercises in the Masters program.
