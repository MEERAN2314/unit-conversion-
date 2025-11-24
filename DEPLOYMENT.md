# Deployment Guide for Unit Converter Pro

## Render Deployment (Recommended)

### Prerequisites
- GitHub account
- Render account (free tier available)
- Git repository with your code

### Step 1: Prepare Your Repository

Ensure these files are in your repository root:
- `requirements.txt` - Python dependencies
- `render.yaml` - Render configuration
- `Procfile` - Process configuration
- `runtime.txt` - Python version

### Step 2: Deploy to Render

#### Option A: Using render.yaml (Automatic)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New" → "Blueprint"
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml` and configure everything
6. Click "Apply" to deploy

#### Option B: Manual Setup

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: unit-converter-pro
   - **Environment**: Python 3
   - **Region**: Oregon (or closest to you)
   - **Branch**: main
   - **Build Command**: `pip install -r requirements.txt && pip install -e .`
   - **Start Command**: `cd web_app && gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`
   - **Plan**: Free
5. Add Environment Variables:
   - `PYTHON_VERSION`: 3.11.0
6. Click "Create Web Service"

### Step 3: Verify Deployment

Once deployed, Render will provide a URL like: `https://unit-converter-pro.onrender.com`

Test these endpoints:
- `https://your-app.onrender.com/` - Web interface
- `https://your-app.onrender.com/health` - Health check
- `https://your-app.onrender.com/docs` - API documentation

### Important Notes

- **Free Tier**: Render free tier spins down after 15 minutes of inactivity
- **Cold Starts**: First request after spin-down may take 30-60 seconds
- **Health Checks**: The `/health` endpoint keeps your service monitored
- **Logs**: View logs in Render dashboard for debugging

## Alternative Deployment Options

### Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create unit-converter-pro`
4. Deploy: `git push heroku main`

### Railway

1. Go to [Railway](https://railway.app/)
2. Click "New Project" → "Deploy from GitHub"
3. Select your repository
4. Railway auto-detects Python and deploys

### Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t unit-converter-pro .

# Run container
docker run -p 5000:5000 unit-converter-pro
```

### VPS Deployment (DigitalOcean, AWS, etc.)

```bash
# SSH into your server
ssh user@your-server-ip

# Clone repository
git clone https://github.com/yourusername/unit-converter-pro.git
cd unit-converter-pro

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Run with gunicorn
cd web_app
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000
```

## Environment Variables

Configure these in your deployment platform:

- `PORT` - Port number (auto-set by most platforms)
- `PYTHON_VERSION` - Python version (3.11.0 recommended)
- `DEBUG` - Set to "false" in production

## Performance Optimization

### For Production:

1. **Workers**: Adjust based on CPU cores
   ```bash
   gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
   ```

2. **Caching**: Enable Redis for caching conversions
3. **CDN**: Use Cloudflare for static assets
4. **Monitoring**: Set up Sentry for error tracking

## Troubleshooting

### Issue: App won't start
- Check logs in Render dashboard
- Verify all dependencies in requirements.txt
- Ensure Python version matches runtime.txt

### Issue: 502 Bad Gateway
- Check if PORT environment variable is set
- Verify gunicorn is binding to 0.0.0.0:$PORT

### Issue: Slow cold starts
- Upgrade to paid tier for always-on service
- Implement health check pinging service

## Monitoring

### Health Check Endpoint
```bash
curl https://your-app.onrender.com/health
```

Expected response:
```json
{"status": "healthy", "version": "2.0.0"}
```

### API Documentation
Access interactive API docs at:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Scaling

### Horizontal Scaling
- Increase worker count in start command
- Use load balancer for multiple instances

### Vertical Scaling
- Upgrade Render plan for more resources
- Optimize Pint registry initialization

## Security

- CORS is configured for all origins (adjust in production)
- No authentication required (add if needed)
- HTTPS enabled by default on Render
- Rate limiting recommended for production

## Cost Estimation

### Render Free Tier
- ✅ 750 hours/month free
- ✅ Automatic HTTPS
- ✅ Custom domains
- ⚠️ Spins down after inactivity

### Render Starter ($7/month)
- ✅ Always on
- ✅ Faster builds
- ✅ More resources

## Support

For deployment issues:
- Check Render documentation: https://render.com/docs
- Review application logs
- Test locally first: `python web_app/app.py`
