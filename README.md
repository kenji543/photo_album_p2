# Photo Album Management System

A Django-based photo album manager built for production deployment on Render with Cloudinary image storage.

## Features

- Django Class-Based Views for album and photo CRUD
- Role-based access control using Django authentication
- PostgreSQL-ready database configuration via `DATABASE_URL`
- Cloudinary media storage integration for production
- Simple UI with album galleries, upload flow, and admin permissions

## Setup

1. Create a Python virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and populate secrets.
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DATABASE_URL`
- `CLOUDINARY_URL`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

## Deployment on Render

1. Connect the repository to Render.
2. Set the environment to `python`.
3. Set the build command to `pip install -r requirements.txt`.
4. Set the start command to `gunicorn photo_album_project.wsgi`.
5. Set all required environment variables securely in Render.

## Notes

- Local media storage is only used in development when Cloudinary is not configured.
- Production uses `django-cloudinary-storage` with Cloudinary as the remote storage provider.
