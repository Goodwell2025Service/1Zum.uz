#!/bin/bash

# Development setup script for 1Zum.uz
echo "Setting up 1Zum.uz development environment..."

# Activate virtual environment
source venv/bin/activate

# Install minimal dependencies for development
pip install Django whitenoise django-environ pillow

# Create minimal secrets.json if it doesn't exist
if [ ! -f "secrets.json" ]; then
    echo "Creating secrets.json..."
    cat > secrets.json << EOF
{
    "DJANGO_SECRET_KEY": "django-insecure-local-development-key-not-for-production-use-12345",
    "DATABASE_URL": "sqlite:///db.sqlite3",
    "DJANGO_DEBUG": "True",
    "DATABASE_NAME": "db.sqlite3",
    "DATABASE_USER": "",
    "DATABASE_PASSWORD": "",
    "DATABASE_HOST": "",
    "DATABASE_PORT": "",
    "DJANGO_EMAIL_BACKEND": "django.core.mail.backends.console.EmailBackend",
    "DJANGO_ACCOUNT_ALLOW_REGISTRATION": "True",
    "TELEGRAM_CHAT_ID": "",
    "TELEGRAM_BOT_TOKEN": ""
}
EOF
fi

echo "Setup complete!"
echo "To run the Django server: python manage.py runserver 8000"
echo "To run static files server: python -m http.server 8080 (from birzum/static folder)"
