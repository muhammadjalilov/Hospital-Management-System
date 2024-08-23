# Hospital Management System

This project is a study-based Hospital Management System built with Django. It provides functionality for managing hospital operations, including patient records, staff management, and appointment scheduling.

## Features

- **User Authentication**: Secure login and registration with JWT authentication.
- **Patient Management**: Add, update, and view patient details.
- **Doctor Management**: Add, update, and view doctor details.
- **Appointment Scheduling**: Manage patient appointments.
- ***etc..***

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/muhammadjalilov/Hospital-Management-System
    cd hospital-management-system
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser** (optional):
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```


## Dependencies

The project uses the following packages:

- `asgiref==3.8.1`
- `attrs==24.2.0`
- `certifi==2024.7.4`
- `cffi==1.17.0`
- `charset-normalizer==3.3.2`
- `cryptography==43.0.0`
- `defusedxml==0.8.0rc2`
- `Django==5.1`
- `django-crontab==0.7.1`
- `django-extensions==3.2.3`
- `django-phonenumber-field==8.0.0`
- `django-templated-mail==1.1.1`
- `djangorestframework==3.15.2`
- `djangorestframework-simplejwt==5.3.1`
- `djoser==2.2.3`
- `drf-spectacular==0.27.2`
- `idna==3.7`
- `inflection==0.5.1`
- `jsonschema==4.23.0`
- `jsonschema-specifications==2023.12.1`
- `oauthlib==3.2.2`
- `packaging==24.1`
- `phonenumbers==8.13.43`
- `pillow==10.4.0`
- `pycparser==2.22`
- `PyJWT==2.9.0`
- `python3-openid==3.2.0`
- `pytz==2024.1`
- `PyYAML==6.0.2`
- `referencing==0.35.1`
- `requests==2.32.3`
- `requests-oauthlib==2.0.0`
- `rpds-py==0.20.0`
- `social-auth-app-django==5.4.2`
- `social-auth-core==4.5.4`
- `sqlparse==0.5.1`
- `typing_extensions==4.12.2`
- `uritemplate==4.1.1`
- `urllib3==2.2.2`


## Acknowledgments

- **Django**: A high-level Python web framework that encourages rapid development.
- **DRF**: Django REST Framework for building APIs.
- **DRF-SPECTACULAR**: For generating interactive API documentation.

## Contact

For any questions or suggestions, please contact [mjalilov2004@gmail.com].

