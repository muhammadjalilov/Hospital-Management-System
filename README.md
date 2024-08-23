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

## Acknowledgments

- **Django**: A high-level Python web framework that encourages rapid development.
- **DRF**: Django REST Framework for building APIs.
- **DRF-SPECTACULAR**: For generating interactive API documentation.

## Contact

For any questions or suggestions, please contact [mjalilov2004@gmail.com].

