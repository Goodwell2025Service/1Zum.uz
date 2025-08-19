#!/bin/bash

# 1ZUM.uz Complete Development Setup Script
# This script sets up the full Django development environment

echo "🚀 Setting up 1ZUM.uz Full Django Development Environment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project directory
PROJECT_DIR="/Users/admino/Documents/PROJECTS/Goodwell 1ZUM/1Zum.uz"
cd "$PROJECT_DIR"

echo -e "${BLUE}📂 Working in: $PROJECT_DIR${NC}"

# 1. Activate virtual environment
echo -e "${YELLOW}🔧 Activating virtual environment...${NC}"
source venv/bin/activate

# 2. Install all required packages
echo -e "${YELLOW}📦 Installing Django dependencies...${NC}"
pip install --upgrade pip

# Core Django packages
pip install Django==4.2.0
pip install django-environ
pip install django-model-utils
pip install django-allauth
pip install django-crispy-forms
pip install django-cors-headers
pip install whitenoise
pip install Pillow

# Additional packages for full functionality
pip install django-ckeditor
pip install django-mptt
pip install sorl-thumbnail
pip install django-hijack
pip install django-hijack-admin
pip install django-modeltranslation
pip install django-mathfilters
pip install django-filter
pip install django-rosetta
pip install redis
pip install hiredis
pip install python-slugify
pip install pytz

echo -e "${GREEN}✅ Dependencies installed!${NC}"

# 3. Database setup
echo -e "${YELLOW}🗄️ Setting up database...${NC}"
DJANGO_SETTINGS_MODULE=config.settings.simple python manage.py migrate

echo -e "${GREEN}✅ Database migrations completed!${NC}"

# 4. Create superuser (optional)
echo -e "${YELLOW}👤 Creating superuser...${NC}"
echo "You can create a superuser account to access Django admin"
echo "Run manually: python manage.py createsuperuser"

# 5. Collect static files
echo -e "${YELLOW}📁 Collecting static files...${NC}"
DJANGO_SETTINGS_MODULE=config.settings.simple python manage.py collectstatic --noinput

echo -e "${GREEN}✅ Static files collected!${NC}"

# 6. Build frontend assets
echo -e "${YELLOW}🎨 Building frontend assets...${NC}"
pnpm install
pnpm run build:ci

echo -e "${GREEN}✅ Frontend assets built!${NC}"

echo -e "${GREEN}🎉 Setup complete!${NC}"
echo ""
echo -e "${BLUE}🌐 To start the development server:${NC}"
echo "cd $PROJECT_DIR"
echo "source venv/bin/activate"
echo "DJANGO_SETTINGS_MODULE=config.settings.simple python manage.py runserver 8000"
echo ""
echo -e "${BLUE}📖 Then visit: http://localhost:8000${NC}"
echo ""
echo -e "${BLUE}🔧 To create admin user:${NC}"
echo "python manage.py createsuperuser"
echo ""
echo -e "${BLUE}🛠️ Admin panel: http://localhost:8000/admin${NC}"
