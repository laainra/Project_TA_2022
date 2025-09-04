import os

def create_directory_structure(base_path="."):
    """
    Creates the specified directory structure for the Flask project.

    Args:
        base_path (str): The base directory where the project structure will be created.
                         Defaults to the current directory.
    """
    project_name = "coorporate_app" # Nama proyek sesuai permintaan

    # Define the core directories and their subdirectories
    dirs_to_create = [
        # Root level
        os.path.join(project_name),
        os.path.join(project_name, "migrations"),
        os.path.join(project_name, "instance"),

        # app/ directory
        os.path.join(project_name, "app"),
        os.path.join(project_name, "app", "models"),
        os.path.join(project_name, "app", "controllers"),
        os.path.join(project_name, "app", "routes"),
        os.path.join(project_name, "app", "ai"),
        os.path.join(project_name, "app", "utils"),
        os.path.join(project_name, "app", "templates", "components"),
        os.path.join(project_name, "app", "templates", "admin_panel"),
        os.path.join(project_name, "app", "templates", "employee_panel"),
        os.path.join(project_name, "app", "templates", "superadmin"),
        os.path.join(project_name, "app", "static", "css"), # Add static subdirs
        os.path.join(project_name, "app", "static", "js"),
        os.path.join(project_name, "app", "static", "img"),
        os.path.join(project_name, "app", "static", "trained_models"), # For AI models
        os.path.join(project_name, "app", "static", "haarcascades"), # For Haar Cascade XMLs
    ]

    print(f"Creating project directory '{project_name}' at '{os.path.abspath(base_path)}'...")

    for path in dirs_to_create:
        full_path = os.path.join(base_path, path)
        try:
            os.makedirs(full_path, exist_ok=True)
            print(f"Created: {full_path}")
        except OSError as e:
            print(f"Error creating directory {full_path}: {e}")

    # Create dummy files for essential project structure
    dummy_files = [
        # Root level files
        os.path.join(project_name, "run.py"),
        os.path.join(project_name, "requirements.txt"),
        os.path.join(project_name, "README.md"),
        os.path.join(project_name, ".flaskenv"),
        os.path.join(project_name, ".gitignore"),
        os.path.join(project_name, "instance", "config.py"), # Instance config

        # app/ directory files
        os.path.join(project_name, "app", "__init__.py"),
        
        # Models
        os.path.join(project_name, "app", "models", "__init__.py"),
        os.path.join(project_name, "app", "models", "user.py"),
        os.path.join(project_name, "app", "models", "camera.py"),
        os.path.join(project_name, "app", "models", "presence.py"),

        # Controllers
        os.path.join(project_name, "app", "controllers", "__init__.py"),
        os.path.join(project_name, "app", "controllers", "admin_controller.py"),
        os.path.join(project_name, "app", "controllers", "camera_controller.py"),
        os.path.join(project_name, "app", "controllers", "employee_controller.py"),
        os.path.join(project_name, "app", "controllers", "face_controller.py"),
        os.path.join(project_name, "app", "controllers", "personnel_controller.py"),
        os.path.join(project_name, "app", "controllers", "stream_controller.py"),
        os.path.join(project_name, "app", "controllers", "superadmin_controller.py"),
        os.path.join(project_name, "app", "controllers", "auth_controller.py"),
        os.path.join(project_name, "app", "controllers", "settings_controller.py"),

        # Routes
        os.path.join(project_name, "app", "routes", "__init__.py"),
        os.path.join(project_name, "app", "routes", "admin_routes.py"),
        os.path.join(project_name, "app", "routes", "camera_routes.py"),
        os.path.join(project_name, "app", "routes", "employee_routes.py"),
        os.path.join(project_name, "app", "routes", "face_routes.py"),
        os.path.join(project_name, "app", "routes", "personnel_routes.py"),
        os.path.join(project_name, "app", "routes", "stream_routes.py"),
        os.path.join(project_name, "app", "routes", "superadmin_routes.py"),
        os.path.join(project_name, "app", "routes", "auth_routes.py"),
        os.path.join(project_name, "app", "routes", "settings_routes.py"),

        # AI
        os.path.join(project_name, "app", "ai", "__init__.py"),
        os.path.join(project_name, "app", "ai", "face_recognition.py"),
        os.path.join(project_name, "app", "ai", "gender_classification.py"),
        os.path.join(project_name, "app", "ai", "age_estimation.py"),
        os.path.join(project_name, "app", "ai", "suspicious_activity.py"),
        os.path.join(project_name, "app", "ai", "people_counter.py"),
        os.path.join(project_name, "app", "static", "haarcascades", "haarcascade_frontalface_default.xml"), # Placeholder for cascade
        os.path.join(project_name, "app", "static", "trained_models", "trained_model.yml"), # Placeholder for trained model

        # Utils
        os.path.join(project_name, "app", "utils", "__init__.py"),
        os.path.join(project_name, "app", "utils", "database.py"),
        os.path.join(project_name, "app", "utils", "decorators.py"),
        os.path.join(project_name, "app", "utils", "helpers.py"),

        # Templates (main and components)
        os.path.join(project_name, "app", "templates", "login.html"),
        os.path.join(project_name, "app", "templates", "profile.html"),
        os.path.join(project_name, "app", "templates", "components", "base.html"),
        os.path.join(project_name, "app", "templates", "components", "navbar.html"),
        os.path.join(project_name, "app", "templates", "components", "footer.html"),

        # Templates (admin_panel)
        os.path.join(project_name, "app", "templates", "admin_panel", "dashboard.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "division.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "employees.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "presence.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "presence_cam.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "tracking_cam.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "work_time_report.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "tracking_report.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "camera.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "add_camera.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "edit_camera.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "personnels.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "add_personnel.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "edit_personnel.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "personnel_entries.html"),
        os.path.join(project_name, "app", "templates", "admin_panel", "settings.html"),

        # Templates (employee_panel)
        os.path.join(project_name, "app", "templates", "employee_panel", "dashboard.html"),
        os.path.join(project_name, "app", "templates", "employee_panel", "presence_history.html"),
        os.path.join(project_name, "app", "templates", "employee_panel", "capture.html"),
        os.path.join(project_name, "app", "templates", "employee_panel", "dataset.html"),

        # Templates (superadmin)
        os.path.join(project_name, "app", "templates", "superadmin", "dashboard.html"),
        os.path.join(project_name, "app", "templates", "superadmin", "company_list.html"),
        os.path.join(project_name, "app", "templates", "superadmin", "add_company.html"),
        os.path.join(project_name, "app", "templates", "superadmin", "edit_company.html"),

        # Static files (dummy)
        os.path.join(project_name, "app", "static", "css", "style.css"), # Generic stylesheet
        os.path.join(project_name, "app", "static", "js", "script.js"), # Generic script
    ]

    print("\nCreating dummy files...")
    for file_path in dummy_files:
        full_path = os.path.join(base_path, file_path)
        try:
            # Ensure parent directories exist before creating the file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w') as f:
                # Add basic content to some files for clarity
                if "run.py" in os.path.basename(full_path):
                    f.write("from app import create_app\n\napp = create_app()\n\nif __name__ == '__main__':\n    app.run(debug=True)\n")
                elif "requirements.txt" in os.path.basename(full_path):
                    f.write("Flask\nFlask-SQLAlchemy\nPyMySQL\nFlask-Login\nWerkzeug\npython-dotenv\npandas\nopenpyxl\nopencv-python\nnumpy\n")
                elif ".flaskenv" in os.path.basename(full_path):
                    f.write("FLASK_APP=run.py\nFLASK_ENV=development\n")
                elif ".gitignore" in os.path.basename(full_path):
                    f.write("__pycache__/\n*.pyc\nvenv/\n.env\ninstance/\nmedia/\n")
                elif "__init__.py" in os.path.basename(full_path):
                    f.write("# This file makes the directory a Python package.\n")
                    if os.path.basename(os.path.dirname(full_path)) == "app":
                        f.write("from flask import Flask\nfrom flask_sqlalchemy import SQLAlchemy\nfrom flask_login import LoginManager\n\ndb = SQLAlchemy()\nlogin_manager = LoginManager()\n\ndef create_app():\n    app = Flask(__name__)\n    # Configure app\n    return app\n")
                elif ".html" in os.path.basename(full_path):
                    f.write("\n")
                    if "base.html" in os.path.basename(full_path):
                        f.write("<!DOCTYPE html>\n<html><head><title>{% block title %}{% endblock %}</title></head><body>{% block content %}{% endblock %}</body></html>\n")
                else:
                    f.write(f"# This is a dummy file for {os.path.basename(full_path)}\n")
            print(f"Created file: {full_path}")
        except IOError as e:
            print(f"Error creating file {full_path}: {e}")

    print(f"\nFlask project structure for '{project_name}' created successfully!")
    print(f"Navigate to '{project_name}' directory: cd {project_name}")
    print("Then, start populating the files with your migrated code.")

if __name__ == "__main__":
    create_directory_structure()