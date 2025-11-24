// Enhanced JavaScript for Unit Converter Pro

class UnitConverterApp {
    constructor() {
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupAnimations();
        this.setupKeyboardShortcuts();
        this.setupFormPersistence();
        this.setupTooltips();
        this.setupResponsiveHandlers();
        this.setupViewportFix();
    }

    setupEventListeners() {
        // Form submission with loading state
        const form = document.getElementById('conversionForm');
        if (form) {
            form.addEventListener('submit', this.handleFormSubmit.bind(this));
        }

        // Unit category filtering
        const fromUnitSelect = document.getElementById('from_unit');
        if (fromUnitSelect) {
            fromUnitSelect.addEventListener('change', this.handleUnitCategoryChange.bind(this));
        }

        // Enhanced hover effects
        this.setupHoverEffects();
    }

    handleFormSubmit(event) {
        const submitBtn = event.target.querySelector('button[type="submit"]');
        const originalContent = submitBtn.innerHTML;
        
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Converting...';
        submitBtn.disabled = true;
        submitBtn.classList.add('loading');

        // Re-enable button after a delay if form doesn't submit
        setTimeout(() => {
            if (submitBtn.disabled) {
                submitBtn.innerHTML = originalContent;
                submitBtn.disabled = false;
                submitBtn.classList.remove('loading');
            }
        }, 10000);
    }

    handleUnitCategoryChange(event) {
        const selectedOption = event.target.options[event.target.selectedIndex];
        const selectedCategory = selectedOption.getAttribute('data-category');
        
        // Animate category transitions
        const categories = document.querySelectorAll('.unit-category');
        categories.forEach((element, index) => {
            const category = element.getAttribute('data-category');
            
            if (selectedCategory && category === selectedCategory) {
                element.style.display = 'block';
                element.style.animation = `fadeIn 0.5s ease-out ${index * 0.1}s both`;
            } else {
                element.style.animation = 'fadeOut 0.3s ease-out';
                setTimeout(() => {
                    element.style.display = 'none';
                }, 300);
            }
        });
        
        // Clear previous selections
        const checkboxes = document.querySelectorAll('input[name="to_units"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
            checkbox.parentElement.classList.remove('selected');
        });
    }

    setupAnimations() {
        // Intersection Observer for scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, observerOptions);

        // Observe all cards and major elements
        document.querySelectorAll('.card, .unit-category, .feature-icon').forEach(el => {
            observer.observe(el);
        });
    }

    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (event) => {
            // Ctrl/Cmd + Enter to submit form
            if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
                const form = document.getElementById('conversionForm');
                if (form && this.validateForm()) {
                    form.submit();
                }
            }
            
            // Escape to clear form
            if (event.key === 'Escape') {
                this.clearForm();
            }
            
            // Ctrl/Cmd + / to focus search
            if ((event.ctrlKey || event.metaKey) && event.key === '/') {
                event.preventDefault();
                const valueInput = document.getElementById('value');
                if (valueInput) {
                    valueInput.focus();
                }
            }
        });
    }

    setupFormPersistence() {
        // Auto-save form data
        const inputs = document.querySelectorAll('#conversionForm input, #conversionForm select');
        inputs.forEach(input => {
            input.addEventListener('change', this.saveFormData.bind(this));
            input.addEventListener('input', this.debounce(this.saveFormData.bind(this), 500));
        });

        // Restore form data on load
        this.restoreFormData();
    }

    setupTooltips() {
        // Initialize Bootstrap tooltips
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(tooltipTriggerEl => {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    setupHoverEffects() {
        // Enhanced hover effects for interactive elements (desktop only)
        if (window.matchMedia('(hover: hover)').matches) {
            const interactiveElements = document.querySelectorAll('.unit-card, .form-check, .btn');
            
            interactiveElements.forEach(element => {
                element.addEventListener('mouseenter', () => {
                    element.style.transform = 'translateY(-2px)';
                });
                
                element.addEventListener('mouseleave', () => {
                    element.style.transform = 'translateY(0)';
                });
            });
        }
        
        // Touch feedback for mobile devices
        if ('ontouchstart' in window) {
            const touchElements = document.querySelectorAll('.btn, .unit-card, .form-check');
            
            touchElements.forEach(element => {
                element.addEventListener('touchstart', () => {
                    element.style.opacity = '0.8';
                });
                
                element.addEventListener('touchend', () => {
                    element.style.opacity = '1';
                });
            });
        }
    }

    validateForm() {
        const value = document.getElementById('value').value;
        const fromUnit = document.getElementById('from_unit').value;
        
        if (!value || isNaN(value)) {
            this.showNotification('Please enter a valid numeric value', 'error');
            return false;
        }
        
        if (!fromUnit) {
            this.showNotification('Please select a source unit', 'error');
            return false;
        }
        
        return true;
    }

    clearForm() {
        const form = document.getElementById('conversionForm');
        if (form) {
            form.reset();
            
            // Hide all unit categories
            document.querySelectorAll('.unit-category').forEach(category => {
                category.style.display = 'none';
            });
            
            // Clear localStorage
            localStorage.removeItem('unitConverterFormData');
            
            this.showNotification('Form cleared', 'info');
        }
    }

    saveFormData() {
        const formData = {
            value: document.getElementById('value')?.value || '',
            from_unit: document.getElementById('from_unit')?.value || '',
            to_units: Array.from(document.querySelectorAll('input[name="to_units"]:checked')).map(cb => cb.value)
        };
        
        localStorage.setItem('unitConverterFormData', JSON.stringify(formData));
    }

    restoreFormData() {
        const savedData = localStorage.getItem('unitConverterFormData');
        if (savedData) {
            try {
                const data = JSON.parse(savedData);
                
                if (data.value) {
                    const valueInput = document.getElementById('value');
                    if (valueInput) valueInput.value = data.value;
                }
                
                if (data.from_unit) {
                    const fromUnitSelect = document.getElementById('from_unit');
                    if (fromUnitSelect) {
                        fromUnitSelect.value = data.from_unit;
                        fromUnitSelect.dispatchEvent(new Event('change'));
                    }
                }
                
                if (data.to_units && data.to_units.length > 0) {
                    setTimeout(() => {
                        data.to_units.forEach(unit => {
                            const checkbox = document.getElementById('to_' + unit);
                            if (checkbox) {
                                checkbox.checked = true;
                                checkbox.parentElement.classList.add('selected');
                            }
                        });
                    }, 100);
                }
            } catch (error) {
                console.error('Error restoring form data:', error);
            }
        }
    }

    showNotification(message, type = 'info') {
        // Create toast notification
        const toastContainer = this.getOrCreateToastContainer();
        const toastId = 'toast-' + Date.now();
        
        const iconClass = type === 'success' ? 'fa-check-circle text-success' : 
                         type === 'error' ? 'fa-exclamation-circle text-danger' : 
                         'fa-info-circle text-info';

        const toastHTML = `
            <div id="${toastId}" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <i class="fas ${iconClass} me-2"></i>
                    <strong class="me-auto">Unit Converter Pro</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast"></button>
                </div>
                <div class="toast-body">
                    ${message}
                </div>
            </div>
        `;

        toastContainer.insertAdjacentHTML('beforeend', toastHTML);
        
        const toastElement = document.getElementById(toastId);
        const toast = new bootstrap.Toast(toastElement, {
            autohide: true,
            delay: 3000
        });
        
        toast.show();
        
        // Clean up after toast is hidden
        toastElement.addEventListener('hidden.bs.toast', () => {
            toastElement.remove();
        });
    }

    getOrCreateToastContainer() {
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
            document.body.appendChild(container);
        }
        return container;
    }

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    setupResponsiveHandlers() {
        // Handle orientation changes
        window.addEventListener('orientationchange', () => {
            setTimeout(() => {
                this.adjustLayoutForOrientation();
            }, 100);
        });

        // Handle window resize
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                this.adjustLayoutForViewport();
            }, 250);
        });

        // Initial adjustment
        this.adjustLayoutForViewport();
    }

    setupViewportFix() {
        // Fix for mobile viewport height issues (especially iOS)
        const setViewportHeight = () => {
            const vh = window.innerHeight * 0.01;
            document.documentElement.style.setProperty('--vh', `${vh}px`);
        };

        setViewportHeight();
        window.addEventListener('resize', setViewportHeight);
        window.addEventListener('orientationchange', setViewportHeight);
    }

    adjustLayoutForOrientation() {
        const isLandscape = window.matchMedia('(orientation: landscape)').matches;
        const isMobile = window.matchMedia('(max-width: 768px)').matches;

        if (isLandscape && isMobile) {
            // Compact mode for mobile landscape
            document.body.classList.add('landscape-mode');
            
            // Reduce padding and margins
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                card.style.marginBottom = '1rem';
            });
        } else {
            document.body.classList.remove('landscape-mode');
            
            // Restore normal spacing
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                card.style.marginBottom = '';
            });
        }
    }

    adjustLayoutForViewport() {
        const viewportWidth = window.innerWidth;
        
        // Adjust font sizes for very small screens
        if (viewportWidth < 360) {
            document.documentElement.style.fontSize = '14px';
        } else if (viewportWidth < 400) {
            document.documentElement.style.fontSize = '15px';
        } else {
            document.documentElement.style.fontSize = '16px';
        }

        // Adjust table display for mobile
        const tables = document.querySelectorAll('.table-responsive');
        tables.forEach(table => {
            if (viewportWidth < 768) {
                table.style.overflowX = 'auto';
                table.style.webkitOverflowScrolling = 'touch';
            }
        });

        // Adjust button groups for mobile
        const buttonGroups = document.querySelectorAll('.btn-group');
        buttonGroups.forEach(group => {
            if (viewportWidth < 576) {
                group.classList.add('btn-group-vertical');
                group.classList.remove('btn-group');
            } else {
                group.classList.add('btn-group');
                group.classList.remove('btn-group-vertical');
            }
        });
    }
}

// Global functions for template usage
window.setExample = function(value, fromUnit, toUnits) {
    const app = window.unitConverterApp;
    
    // Visual feedback
    const valueInput = document.getElementById('value');
    const fromUnitSelect = document.getElementById('from_unit');
    
    if (valueInput && fromUnitSelect) {
        // Animate inputs
        valueInput.style.transform = 'scale(1.05)';
        fromUnitSelect.style.transform = 'scale(1.05)';
        
        setTimeout(() => {
            valueInput.style.transform = 'scale(1)';
            fromUnitSelect.style.transform = 'scale(1)';
        }, 200);
        
        valueInput.value = value;
        fromUnitSelect.value = fromUnit;
        fromUnitSelect.dispatchEvent(new Event('change'));
        
        // Set target units with staggered animation
        setTimeout(() => {
            toUnits.forEach((unit, index) => {
                setTimeout(() => {
                    const checkbox = document.getElementById('to_' + unit);
                    if (checkbox) {
                        checkbox.checked = true;
                        checkbox.parentElement.style.animation = `bounceIn 0.5s ease-out`;
                    }
                }, index * 100);
            });
        }, 300);
        
        // Smooth scroll to form
        document.getElementById('conversionForm').scrollIntoView({
            behavior: 'smooth',
            block: 'center'
        });
        
        app.showNotification(`Example loaded: ${value} ${fromUnit}`, 'success');
    }
};

// API wrapper for external use
window.UnitConverterAPI = class {
    constructor(baseUrl = '') {
        this.baseUrl = baseUrl;
    }

    async convert(value, fromUnit, toUnits = null) {
        try {
            const response = await fetch(`${this.baseUrl}/api/convert`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    value: value,
                    from_unit: fromUnit,
                    to_units: toUnits
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Conversion API error:', error);
            throw error;
        }
    }

    async getUnits() {
        try {
            const response = await fetch(`${this.baseUrl}/api/units`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Units API error:', error);
            throw error;
        }
    }
};

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.unitConverterApp = new UnitConverterApp();
    window.converterAPI = new UnitConverterAPI();
    
    // Add some visual flair
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease-in';
    
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});