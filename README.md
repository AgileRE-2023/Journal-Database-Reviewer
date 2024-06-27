# Journal Database Reviewer

Journal Database Reviewer is a Django project for managing and reviewing journal databases.

You can refer to this [User Guide](https://drive.google.com/file/d/1C1ZLIWkBTLIFC2VH31341BiJNBIf2JO9/view?usp=sharing) as a guide on how to use this application

> [!IMPORTANT]
> You can only do the scrapping from network that has affiliate with SCOPUS

## Setup Instructions

### 1. Create Virtual Env using python

Install your python venv package first

```bash
    pip install virtualenv
```

Then, create your virtual env with

```bash
    python -m venv venv
```

To activate the virtual env use

- In powershell

```bash
    venv/Scripts/Activate.ps1
```

- In powershell

```bash
    venv/Scripts/Activate.bat
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Journal-Database-Reviewer.git
cd Journal-Database-Reviewer
```

### 3. Install Dependencies

```bash
pip install -r path/to/requirements.txt
```

### 4. Configure `settings.py`

Edit the `settings.py` file to configure the MySQL database and Tailwind CSS settings using `django-tailwind`.

```python
# settings.py

# Database Configuration for MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # Set to the address of your MySQL server
        'PORT': '3306',       # Set to the port of your MySQL server
    }
}

# Django Tailwind Configuration
INSTALLED_APPS = [
    # ...
    'tailwind',
    # ...
]

TAILWIND_APP_NAME = 'yourapp'  # Replace 'yourapp' with the name of your Django-tailwind app
```

For more instruction about django-tailwind installations:
https://django-tailwind.readthedocs.io/en/latest/installation.html

Replace `'your_database_name'`, `'your_database_user'`, and `'your_database_password'` with your MySQL database name, user, and password.

### 5. Configure Django Tailwind

Add the following lines to your `settings.py` to configure `django-tailwind`:

```python
# settings.py

# Django Tailwind Configuration
TAILWIND_APP_NAME = 'yourapp'  # Replace 'yourapp' with the name of your Django app

# Optional: Customize Tailwind CSS settings
TAILWIND_SETTINGS = {
    'ACCENTS': {
        'blue': '#0000FF',
        # Add more custom accent colors if needed
    },
    # Add more custom Tailwind CSS settings if needed
}
```

### 6. Config Your Elsevier API Key

You need to get the Elsevier API Key [here](https://dev.elsevier.com/apikey/create)

Then, you can put the API Key in the .env file with key

```bash
    SCOPUS_API_KEY=<YOUR_KEY>
```

### 7. Migrate the Database

Run the following commands to apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run the Django Server

Start the Django development server:

```bash
python manage.py runserver
```

The development server will be accessible at [http://localhost:8000/](http://localhost:8000/).

Make sure to adjust the MySQL connection settings according to your MySQL setup. Additionally, ensure that you have the necessary permissions to create and manage databases.
