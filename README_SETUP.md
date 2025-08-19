# 🚀 1ZUM.uz - Complete Setup & Deployment Guide

## 📋 Quick Setup Options

### Option 1: Local Demo (Already Working) ✅
```bash
# Templates + Assets servers
http://localhost:8080/demo.html  # Full working demo
http://localhost:9000           # Static assets
```

### Option 2: Full Django Development 🔧
```bash
cd "/Users/admino/Documents/PROJECTS/Goodwell 1ZUM/1Zum.uz"
./setup_full_django.sh
```

### Option 3: Amplify Deployment 🌐
```bash
cd "/Users/admino/Documents/PROJECTS/Goodwell 1ZUM/1Zum.uz"
./prepare_deployment.sh
git commit -m "Fix Amplify deployment issues"
git push origin main
```

## 🏗️ Full Django Local Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- pnpm installed

### Steps
1. **Run Setup Script:**
   ```bash
   ./setup_full_django.sh
   ```

2. **Manual Installation (if script fails):**
   ```bash
   source venv/bin/activate
   pip install Django django-environ django-model-utils
   pip install django-allauth django-crispy-forms
   pip install django-ckeditor django-mptt sorl-thumbnail
   pip install whitenoise Pillow python-slugify
   ```

3. **Database Setup:**
   ```bash
   DJANGO_SETTINGS_MODULE=config.settings.simple python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Build Assets:**
   ```bash
   pnpm install
   pnpm run build
   ```

5. **Start Server:**
   ```bash
   DJANGO_SETTINGS_MODULE=config.settings.simple python manage.py runserver 8000
   ```

### 🌐 Access Points
- **Frontend:** http://localhost:8000
- **Admin:** http://localhost:8000/admin
- **API:** http://localhost:8000/api/ (if available)

## 🚀 AWS Amplify Deployment

### Files Already Configured ✅
- ✅ `amplify.yml` - Build configuration
- ✅ `gulpfile.js` - Fixed image compression issues
- ✅ `package.json` - Build scripts
- ✅ `.pnpmrc` - Package management
- ✅ Production settings

### Deployment Steps

1. **Prepare for Deployment:**
   ```bash
   ./prepare_deployment.sh
   ```

2. **Commit Changes:**
   ```bash
   git add .
   git commit -m "🚀 Fix Amplify deployment and add local development setup

   - Fix image compression failing in CI environments
   - Add improved CI detection for AWS Amplify
   - Create amplify.yml build configuration
   - Add .pnpmrc for binary dependency handling
   - Create comprehensive demo pages
   - Add simplified Django settings for development
   - Fix gulpfile.js build process
   - Add development setup scripts"
   ```

3. **Push to GitHub:**
   ```bash
   git push origin main
   ```

4. **Deploy on Amplify:**
   - Go to AWS Amplify Console
   - Connect your GitHub repository
   - Amplify will automatically use `amplify.yml`
   - Build process will use `pnpm run build:ci`

### Build Configuration
```yaml
# amplify.yml (already created)
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - pnpm install --frozen-lockfile
    build:
      commands:
        - pnpm run build:ci
  artifacts:
    baseDirectory: birzum/static
    files:
      - '**/*'
```

## 🔧 Key Fixes Made

### 1. Image Compression Issues
- Fixed binary dependencies (`jpegtran-bin`, `optipng-bin`)
- Added CI environment detection
- Created CI-specific build task

### 2. Build Process
- Enhanced `gulpfile.js` with error handling
- Added `.pnpmrc` for package management
- Created production-ready build scripts

### 3. Demo Pages
- Created complete working demo pages
- Added interactive components
- Proper asset loading from localhost:9000

### 4. Django Configuration
- Added simplified settings for development
- Fixed model issues
- Added production-ready settings

## 🌐 Server Status

### Current Running Servers
- `localhost:3000/en` - Your existing site ✅
- `localhost:8080` - 1ZUM.uz demo ✅
- `localhost:9000` - Static assets ✅

### URLs to Test
- [Homepage Demo](http://localhost:8080/demo.html)
- [Products Page](http://localhost:8080/products.html)
- [Blog Page](http://localhost:8080/blog.html)
- [Static Assets](http://localhost:9000)

## 🎯 Next Steps

### For Local Development
1. Run `./setup_full_django.sh`
2. Create superuser: `python manage.py createsuperuser`
3. Start development: `python manage.py runserver 8000`

### For Production Deployment
1. Run `./prepare_deployment.sh`
2. Commit and push changes
3. Deploy on AWS Amplify
4. Monitor build process

## 🐛 Troubleshooting

### Build Fails
- Check Node.js version (18+)
- Clear cache: `pnpm cache clean`
- Reinstall: `rm -rf node_modules && pnpm install`

### Django Issues
- Check Python version (3.11+)
- Activate virtual environment: `source venv/bin/activate`
- Install missing packages manually

### Amplify Deployment
- Check build logs in Amplify console
- Verify `amplify.yml` configuration
- Ensure all files are committed to Git

## 📞 Support

If you encounter issues:
1. Check error logs
2. Verify all prerequisites are installed
3. Try manual installation steps
4. Check GitHub repository for updates

---

**Ready to deploy! 🚀** The project is now configured for both local development and successful AWS Amplify deployment.
