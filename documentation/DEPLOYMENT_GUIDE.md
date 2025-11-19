# Deployment Guide & Production Setup

## 🚀 Deployment Overview

This guide covers multiple deployment strategies for the Unit Converter Pro application, from local development to production cloud deployment. The application is designed to be deployment-ready with Docker support, environment configuration, and scalability considerations.

## 🏗️ Deployment Architecture

### Application Components
```
┌─────────────────────────────────────────────────────────────┐
│                    Load Balancer                            │
│                   (Nginx/CloudFlare)                       │
├─────────────────────────────────────────────────────────────┤
│                FastAPI Application                         │
│              (Multiple Instances)                          │
├─────────────────────────────────────────────────────────────┤
│                Static File Server                          │
│                (CDN/Nginx)                                 │
├─────────────────────────────────────────────────────────────┤
│                 Monitoring & Logging                       │
│              (Prometheus/Grafana)                          │
└─────────────────────────────────────────────────────────────┘
```

### Deployment Environments
- **Development**: Local development with hot reload
- **Staging**: Testing environment with production-like setup
- **Production**: High-availability deployment with monitoring

## 🐳 Docker Deployment

### Dockerfile
```dockerfile
# Multi-stage build for optimized production image
FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app

# Set working directory
WORKDIR /app

# Copy Python dependencies from builder stage
COPY --from=builder /root/.local /home/app/.local

# Copy application code
COPY . .

# Install the unit converter library
RUN pip install --no-cache-dir -e .

# Change ownership to app user
RUN chown -R app:app /app

# Switch to non-root user
USER app

# Add local Python packages to PATH
ENV PATH=/home/app/.local/bin:$PATH

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/categories || exit 1

# Start command
CMD ["uvicorn", "web_app.app:app", "--host", "0.0.0.0", "--port", "5000"]
```

### Docker Compose (Development)
```yaml
# docker-compose.yml
version: '3.8'

services:
  unit-converter:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DEBUG=true
      - HOST=0.0.0.0
      - PORT=5000
    volumes:
      - .:/app
    command: uvicorn web_app.app:app --host 0.0.0.0 --port 5000 --reload
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/api/categories"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - unit-converter
```

### Docker Compose (Production)
```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  unit-converter:
    build: 
      context: .
      dockerfile: Dockerfile
    environment:
      - DEBUG=false
      - HOST=0.0.0.0
      - PORT=5000
      - WORKERS=4
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/api/categories"]
      interval: 30s
      timeout: 10s
      retries: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.prod.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - unit-converter
    deploy:
      resources:
        limits:
          cpus: '0.25'
          memory: 128M

  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
```

### Build and Run Commands
```bash
# Build Docker image
docker build -t unit-converter-pro .

# Run development environment
docker-compose up -d

# Run production environment
docker-compose -f docker-compose.prod.yml up -d

# Scale application
docker-compose -f docker-compose.prod.yml up -d --scale unit-converter=5

# View logs
docker-compose logs -f unit-converter

# Stop services
docker-compose down
```

## ☁️ Cloud Deployment

### AWS Deployment (ECS)

#### Task Definition
```json
{
  "family": "unit-converter-pro",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
  "containerDefinitions": [
    {
      "name": "unit-converter",
      "image": "your-account.dkr.ecr.region.amazonaws.com/unit-converter-pro:latest",
      "portMappings": [
        {
          "containerPort": 5000,
          "protocol": "tcp"
        }
      ],
      "environment": [
        {
          "name": "DEBUG",
          "value": "false"
        },
        {
          "name": "HOST",
          "value": "0.0.0.0"
        },
        {
          "name": "PORT",
          "value": "5000"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/unit-converter-pro",
          "awslogs-region": "us-west-2",
          "awslogs-stream-prefix": "ecs"
        }
      },
      "healthCheck": {
        "command": [
          "CMD-SHELL",
          "curl -f http://localhost:5000/api/categories || exit 1"
        ],
        "interval": 30,
        "timeout": 5,
        "retries": 3,
        "startPeriod": 60
      }
    }
  ]
}
```

#### Service Configuration
```json
{
  "serviceName": "unit-converter-pro",
  "cluster": "production",
  "taskDefinition": "unit-converter-pro:1",
  "desiredCount": 3,
  "launchType": "FARGATE",
  "networkConfiguration": {
    "awsvpcConfiguration": {
      "subnets": ["subnet-12345", "subnet-67890"],
      "securityGroups": ["sg-abcdef"],
      "assignPublicIp": "ENABLED"
    }
  },
  "loadBalancers": [
    {
      "targetGroupArn": "arn:aws:elasticloadbalancing:region:account:targetgroup/unit-converter/1234567890",
      "containerName": "unit-converter",
      "containerPort": 5000
    }
  ]
}
```

### Google Cloud Platform (Cloud Run)

#### Deployment Configuration
```yaml
# cloudrun.yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: unit-converter-pro
  annotations:
    run.googleapis.com/ingress: all
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/maxScale: "10"
        run.googleapis.com/cpu-throttling: "false"
    spec:
      containerConcurrency: 100
      containers:
      - image: gcr.io/project-id/unit-converter-pro:latest
        ports:
        - containerPort: 5000
        env:
        - name: DEBUG
          value: "false"
        - name: HOST
          value: "0.0.0.0"
        - name: PORT
          value: "5000"
        resources:
          limits:
            cpu: "1"
            memory: "512Mi"
        livenessProbe:
          httpGet:
            path: /api/categories
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 30
```

#### Deployment Commands
```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/project-id/unit-converter-pro

# Deploy to Cloud Run
gcloud run deploy unit-converter-pro \
  --image gcr.io/project-id/unit-converter-pro:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 5000 \
  --memory 512Mi \
  --cpu 1 \
  --max-instances 10
```

### Heroku Deployment

#### Procfile
```
web: uvicorn web_app.app:app --host 0.0.0.0 --port $PORT
```

#### Runtime Configuration
```
# runtime.txt
python-3.11.0
```

#### Deployment Commands
```bash
# Login to Heroku
heroku login

# Create application
heroku create unit-converter-pro

# Set environment variables
heroku config:set DEBUG=false
heroku config:set HOST=0.0.0.0

# Deploy
git push heroku main

# Scale application
heroku ps:scale web=2

# View logs
heroku logs --tail
```

## 🔧 Environment Configuration

### Environment Variables
```bash
# Application Configuration
DEBUG=false                    # Enable/disable debug mode
HOST=0.0.0.0                  # Server host
PORT=5000                     # Server port
WORKERS=4                     # Number of worker processes

# Security Configuration
SECRET_KEY=your-secret-key    # Application secret key
ALLOWED_HOSTS=your-domain.com # Allowed hosts

# Monitoring Configuration
LOG_LEVEL=info                # Logging level
METRICS_ENABLED=true          # Enable metrics collection

# Performance Configuration
MAX_CONNECTIONS=1000          # Maximum connections
TIMEOUT=30                    # Request timeout
```

### Configuration Management
```python
# config.py
import os
from typing import List

class Settings:
    # Server Configuration
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "5000"))
    WORKERS: int = int(os.getenv("WORKERS", "1"))
    
    # Security Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key")
    ALLOWED_HOSTS: List[str] = os.getenv("ALLOWED_HOSTS", "").split(",")
    
    # Performance Configuration
    MAX_CONNECTIONS: int = int(os.getenv("MAX_CONNECTIONS", "1000"))
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30"))
    
    # Monitoring Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")
    METRICS_ENABLED: bool = os.getenv("METRICS_ENABLED", "false").lower() == "true"

settings = Settings()
```

## 📊 Monitoring & Observability

### Health Check Endpoint
```python
@app.get("/health")
async def health_check():
    """Health check endpoint for load balancers."""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "uptime": time.time() - start_time
    }

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint."""
    return Response(
        content=generate_latest(),
        media_type="text/plain"
    )
```

### Logging Configuration
```python
import logging
import sys

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)

logger = logging.getLogger(__name__)
```

### Prometheus Metrics
```python
from prometheus_client import Counter, Histogram, generate_latest

# Metrics
REQUEST_COUNT = Counter('requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('request_duration_seconds', 'Request duration')
CONVERSION_COUNT = Counter('conversions_total', 'Total conversions', ['from_unit', 'to_unit'])

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    # Record metrics
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()
    
    REQUEST_DURATION.observe(time.time() - start_time)
    
    return response
```

## 🔒 Security Configuration

### SSL/TLS Configuration (Nginx)
```nginx
server {
    listen 443 ssl http2;
    server_name your-domain.com;
    
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;
    
    location / {
        proxy_pass http://unit-converter:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Security Headers
```python
@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    
    return response
```

## 🚀 Performance Optimization

### Production Server Configuration
```bash
# Start with Gunicorn for production
gunicorn web_app.app:app \
  --worker-class uvicorn.workers.UvicornWorker \
  --workers 4 \
  --bind 0.0.0.0:5000 \
  --timeout 30 \
  --keep-alive 2 \
  --max-requests 1000 \
  --max-requests-jitter 100
```

### Caching Strategy
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_unit_info_cached(unit_symbol: str):
    """Cached unit information lookup."""
    return converter.get_unit_info(unit_symbol)

# Redis caching for API responses
import redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.middleware("http")
async def cache_middleware(request: Request, call_next):
    if request.method == "GET":
        cache_key = f"cache:{request.url}"
        cached_response = redis_client.get(cache_key)
        
        if cached_response:
            return Response(content=cached_response)
    
    response = await call_next(request)
    
    if request.method == "GET" and response.status_code == 200:
        redis_client.setex(cache_key, 3600, response.body)
    
    return response
```

## 📋 Deployment Checklist

### Pre-Deployment
- [ ] All tests passing
- [ ] Code coverage >90%
- [ ] Security scan completed
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Environment variables configured
- [ ] SSL certificates installed
- [ ] Monitoring configured

### Post-Deployment
- [ ] Health checks passing
- [ ] Metrics collection working
- [ ] Logs being generated
- [ ] Performance monitoring active
- [ ] Error tracking configured
- [ ] Backup strategy implemented
- [ ] Rollback plan tested

This deployment guide provides comprehensive coverage for deploying Unit Converter Pro in various environments with proper monitoring, security, and performance considerations.