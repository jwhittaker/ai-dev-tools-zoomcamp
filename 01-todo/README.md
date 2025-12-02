# Django Todo App

A simple, functional Todo application built with Python and Django.

## Features

- **Create Todo**: Add new tasks easily with an optional due date.
- **List Todos**: View all your tasks in one place, sorted by creation date.
- **Update Todo**: Mark tasks as completed, edit titles, or change due dates.
- **Delete Todo**: Remove tasks you no longer need.
- **Resolve Todo**: Quickly mark tasks as completed directly from the list.
- **Responsive Design**: Clean and modern UI using Vanilla CSS.
- **Tested**: Comprehensive unit tests for models and views.

## Prerequisites

- Python 3.x
- Git

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/todo-django.git
    cd todo-django
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

## Usage

1. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Open your browser:**
    Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the app.

## Testing

To run the automated tests:

```bash
python manage.py test
```

## Project Structure

- `config/`: Project configuration settings.
- `todo/`: Main application logic (Models, Views, Templates).
- `db.sqlite3`: SQLite database file (local development).
- `manage.py`: Django's command-line utility.

## License

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
