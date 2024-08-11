# ToDo List App

This ToDo List App is a simple web application developed with Django, enabling users to manage their daily tasks efficiently. The app supports adding, editing, viewing, and deleting tasks.

## Features

- **Add Tasks:** Users can add new tasks to their list.
- **View Tasks:** Display all added tasks in a well-organized list.
- **Edit Tasks:** Update details of existing tasks.
- **Delete Tasks:** Remove tasks that are no longer needed.

## Technologies

- **Backend:** Django
- **Database:** SQLite

## Local Installation

Follow these steps to install and run the app locally on your computer:

1. **Prerequisites:**
   Ensure Python and Django are installed on your system. Visit [Python's website](https://www.python.org/downloads/) and [Django's website](https://www.djangoproject.com/download/) for installation instructions.

2. **Clone the repository:**
   git clone https://github.com/xyzsniperr/ToDo-List.git
   cd ToDo-List

    Set up and activate a virtual environment:

    python -m venv venv
    source venv/bin/activate  # Or venv\Scripts\activate.bat on Windows

Install dependencies:

pip install -r requirements.txt

Initialize the database:

python manage.py makemigrations
python manage.py migrate

Start the development server:

    python manage.py runserver

    Visit http://127.0.0.1:8000 in your web browser to use the app.

This app is licensed under the MIT License. See the LICENSE file for details.
