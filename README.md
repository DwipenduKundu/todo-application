# Todo Application

A web-based Todo Management Application built with **Python and Django**. It allows users to manage their daily tasks, organize their work, and keep track of their progress.

## Features

- User registration and login
- Password reset through email
- Add tasks
- see status
- actions : delete or mark as complete task
- Secure user authentication
- Django Admin Panel for administration
- PostgreSQL database support
- Responsive web interface

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Page structure |
| CSS3 | Styling |
| JavaScript | Frontend interactions |
| SQLite | Local development database |
| PostgreSQL | Production database |
| Gunicorn | Production WSGI server |
| WhiteNoise | Static file serving |
| Render | Cloud deployment |
| Git & GitHub | Version control |

## Project Structure

```text
TodoApplication/
│
├── TodoProject/
│   ├──__init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── TodoApp/
│   ├── migrations/
│   ├── templates/
│   │   └──todoapp
│   │       ├──login.html
│   │       ├──register.html
│   │       ├──todo.html
│   │       ├──password_reset.html
│   │       ├──password_reset_done.html
│   │       ├──password_reset_confirm.html
│   │       ├──password_reset_complete.html
│   │       ├──password_reset_email.html
│   │       └──password_reset_subject.txt
│   │   
│   ├── static/
│   │   └──todoapp
│   │       └──css
│   │           └──todo.css
│   │
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── app.py
│   └── admin.py
│
├── manage.py
├── requirements.txt
├── build.sh
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DwipenduKundu/todo-application.git
cd todo-application
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
```

Activate it on Linux or macOS:

```bash
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```bash
touch .env
code .env
```

Then configure the required settings:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

For production, configure the appropriate environment variables securely through your hosting provider.

Never commit your `.env` file or expose passwords, secret keys, or database credentials.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Deployment

This application is configured for deployment using **Render**.

### 🔗 Project Links

- 🌐 **Live Application:** [Open Todo Application](https://todo-application-87ru.onrender.com)
- 💻 **GitHub Repository:** [View Source Code](https://github.com/DwipenduKundu/todo-application)
- 🔐 **Admin Panel:** [Django Admin](https://todo-application-87ru.onrender.com/admin/)

Production configuration includes:

- PostgreSQL database
- Gunicorn application server
- WhiteNoise for static files
- Environment-based configuration
- Django database migrations
- Static file collection


## Future Improvements

- Task descriptions and due dates
- Task priority management
- Task search and filtering
- Task categories and labels
- Dashboard with task statistics
- Task reminders and notifications
- Improved mobile responsiveness

## Author

**Dwipendu Kundu**

GitHub: [DwipenduKundu](https://github.com/DwipenduKundu)

---

If you find this project useful, feel free to explore the repository and share your feedback.

**Developed with Python and Django.**