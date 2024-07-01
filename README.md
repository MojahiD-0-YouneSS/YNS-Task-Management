# Flask Task Manager

## Project Name and Tagline
**Task Manager**
_A simple task management application built with Flask._

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Team](#team)
- [License](#license)

## Introduction
The Task Manager is a web application designed to help users manage their tasks effectively. Users can add, view, edit, complete, and delete tasks with a simple and intuitive interface.

## Installation
Follow these steps to set up the project on your local machine.

### Prerequisites
- Python 3.6+
- pip (Python package installer)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/flask-task-manager.git
    cd flask-task-manager
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```sh
    python app.py
    ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage
- **Add Task**: Navigate to the "Add Task" page, fill out the form, and submit to add a new task.
- **View Tasks**: Navigate to the "View Tasks" page to see a list of all tasks.
- **Edit Task**: Click the "Edit" link next to a task to edit its details.
- **Complete Task**: Click the "Complete" link next to a task to mark it as completed.
- **Delete Task**: Click the "Delete" link next to a task to remove it from the list.

## Features
- Add tasks with name, description, due date, and priority level.
- View all tasks.
- Edit task details.
- Mark tasks as completed.
- Delete tasks.

## Technologies
- **Flask**: A lightweight WSGI web application framework.
- **HTML/CSS**: For the frontend templates.
- **Python**: The programming language used for the backend logic.

### Alternate Technology Choices
1. **Django vs Flask**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. However, for this simple task manager, Flask was chosen for its lightweight and flexible nature.
2. **SQLite vs MySQL**: SQLite is a lightweight database management system. MySQL is more powerful but was not necessary for this small-scale project. SQLite was chosen for simplicity and ease of use.

## Team
- **[Your Name]**: Developer
- **[Team Member Name]**: Role and reason for their role.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

