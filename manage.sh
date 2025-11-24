#!/bin/bash
# Management script for Unit Converter Pro

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  Unit Converter Pro Manager${NC}"
    echo -e "${BLUE}================================${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Command functions
cmd_install() {
    print_info "Installing dependencies..."
    pip install -r requirements.txt
    pip install -e .
    print_success "Installation complete!"
}

cmd_dev() {
    print_info "Starting development server..."
    cd web_app
    python app.py
}

cmd_prod() {
    print_info "Starting production server..."
    cd web_app
    gunicorn app:app \
        --workers 4 \
        --worker-class uvicorn.workers.UvicornWorker \
        --bind 0.0.0.0:5000 \
        --access-logfile - \
        --error-logfile -
}

cmd_test() {
    print_info "Running tests..."
    python -m pytest tests/ -v --cov=unit_converter --cov-report=html
    print_success "Tests complete! Coverage report: htmlcov/index.html"
}

cmd_test_quick() {
    print_info "Running quick tests..."
    python -m pytest tests/ -v
    print_success "Tests complete!"
}

cmd_clean() {
    print_info "Cleaning project..."
    
    # Remove Python cache
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type f -name "*.pyo" -delete 2>/dev/null || true
    
    # Remove build artifacts
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    rm -rf build/ dist/ 2>/dev/null || true
    
    # Remove test artifacts
    find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
    rm -rf htmlcov/ .coverage 2>/dev/null || true
    
    # Remove logs
    find . -type f -name "*.log" -delete 2>/dev/null || true
    
    print_success "Project cleaned!"
}

cmd_format() {
    print_info "Formatting code with black..."
    black unit_converter/ web_app/ tests/
    print_success "Code formatted!"
}

cmd_lint() {
    print_info "Linting code with flake8..."
    flake8 unit_converter/ web_app/ tests/ --max-line-length=100 --extend-ignore=E203,W503
    print_success "Linting complete!"
}

cmd_docker_build() {
    print_info "Building Docker image..."
    docker build -t unit-converter-pro .
    print_success "Docker image built!"
}

cmd_docker_run() {
    print_info "Running Docker container..."
    docker run -p 5000:5000 unit-converter-pro
}

cmd_docker_stop() {
    print_info "Stopping Docker containers..."
    docker stop $(docker ps -q --filter ancestor=unit-converter-pro) 2>/dev/null || true
    print_success "Docker containers stopped!"
}

cmd_deploy_check() {
    print_info "Checking deployment readiness..."
    
    # Check required files
    files=("requirements.txt" "Procfile" "render.yaml" "runtime.txt" "Dockerfile")
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            print_success "$file exists"
        else
            print_error "$file missing"
        fi
    done
    
    # Check if tests pass
    print_info "Running tests..."
    if python -m pytest tests/ -q; then
        print_success "All tests pass"
    else
        print_error "Tests failed"
        return 1
    fi
    
    print_success "Project is ready for deployment!"
}

cmd_help() {
    print_header
    echo "Usage: ./manage.sh [command]"
    echo ""
    echo "Commands:"
    echo "  install       Install dependencies"
    echo "  dev           Start development server"
    echo "  prod          Start production server"
    echo "  test          Run tests with coverage"
    echo "  test-quick    Run tests without coverage"
    echo "  clean         Clean cache and build files"
    echo "  format        Format code with black"
    echo "  lint          Lint code with flake8"
    echo "  docker-build  Build Docker image"
    echo "  docker-run    Run Docker container"
    echo "  docker-stop   Stop Docker containers"
    echo "  deploy-check  Check if ready for deployment"
    echo "  help          Show this help message"
    echo ""
    echo "Examples:"
    echo "  ./manage.sh install      # Install dependencies"
    echo "  ./manage.sh dev          # Start dev server"
    echo "  ./manage.sh test         # Run tests"
    echo "  ./manage.sh clean        # Clean project"
    echo ""
}

# Main script
print_header

case "${1:-help}" in
    install)
        cmd_install
        ;;
    dev)
        cmd_dev
        ;;
    prod)
        cmd_prod
        ;;
    test)
        cmd_test
        ;;
    test-quick)
        cmd_test_quick
        ;;
    clean)
        cmd_clean
        ;;
    format)
        cmd_format
        ;;
    lint)
        cmd_lint
        ;;
    docker-build)
        cmd_docker_build
        ;;
    docker-run)
        cmd_docker_run
        ;;
    docker-stop)
        cmd_docker_stop
        ;;
    deploy-check)
        cmd_deploy_check
        ;;
    help|--help|-h)
        cmd_help
        ;;
    *)
        print_error "Unknown command: $1"
        echo ""
        cmd_help
        exit 1
        ;;
esac
