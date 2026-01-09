
# LibraryProject

**Objective:** Gain familiarity with Django by setting up a Django development environment and creating a basic Django project. This README documents initial setup steps and the default project structure.

**Prerequisites:**
- Python installed (3.8+ recommended).
- Latest `pip` available.

**Install Django**
Run the following to install Django:

```bash
pip install django
```

**Create the Django project**
Create a new project named `LibraryProject`:

```bash
django-admin startproject LibraryProject
```

This creates the project directory structure with default files such as `manage.py`, the inner `LibraryProject/` package, and default settings.

**Run the development server**
Navigate into the project directory and run the development server:

```bash
cd LibraryProject
python manage.py runserver
```