# Responsive Design Quick Reference

A quick reference guide for developers working with the responsive features of Unit Converter Pro.

## 📐 Breakpoints

```css
/* Extra Small Devices (Phones) */
@media (max-width: 576px) { }

/* Small Devices (Large Phones) */
@media (min-width: 576px) and (max-width: 768px) { }

/* Medium Devices (Tablets) */
@media (min-width: 768px) and (max-width: 992px) { }

/* Large Devices (Small Desktops) */
@media (min-width: 992px) and (max-width: 1200px) { }

/* Extra Large Devices (Desktops) */
@media (min-width: 1200px) { }
```

## 🎯 Touch Target Sizes

```css
/* Minimum touch target size */
.btn, .form-control, .nav-link {
    min-height: 44px;
    min-width: 44px;
}
```

## 📱 Common Responsive Patterns

### Stacking on Mobile

```html
<!-- Desktop: Side by side | Mobile: Stacked -->
<div class="row">
    <div class="col-12 col-md-6">Left</div>
    <div class="col-12 col-md-6">Right</div>
</div>
```

### Hiding Elements

```html
<!-- Hide on mobile, show on desktop -->
<div class="d-none d-md-block">Desktop only</div>

<!-- Show on mobile, hide on desktop -->
<div class="d-block d-md-none">Mobile only</div>
```

### Responsive Spacing

```html
<!-- Small gap on mobile, large on desktop -->
<div class="d-flex gap-2 gap-md-4">
    <button>Button 1</button>
    <button>Button 2</button>
</div>
```

## 🎨 Responsive Typography

```css
/* Fluid typography */
h1 {
    font-size: clamp(1.5rem, 5vw, 2.5rem);
}

/* Responsive font sizes */
@media (max-width: 576px) {
    body { font-size: 14px; }
}

@media (min-width: 576px) {
    body { font-size: 16px; }
}
```

## 📊 Grid Layouts

### Auto-Fit Grid

```css
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
}
```

### Responsive Columns

```html
<!-- 1 col mobile, 2 col tablet, 3 col desktop -->
<div class="row g-3">
    <div class="col-12 col-sm-6 col-lg-4">Card 1</div>
    <div class="col-12 col-sm-6 col-lg-4">Card 2</div>
    <div class="col-12 col-sm-6 col-lg-4">Card 3</div>
</div>
```

## 🖱️ Touch vs Hover

```css
/* Hover effects only on devices that support hover */
@media (hover: hover) {
    .btn:hover {
        transform: translateY(-2px);
    }
}

/* Touch feedback for touch devices */
@media (hover: none) {
    .btn:active {
        opacity: 0.8;
    }
}
```

## 📐 Viewport Units

```css
/* Full viewport height (with iOS fix) */
.full-height {
    height: 100vh;
    height: calc(var(--vh, 1vh) * 100);
}

/* Fluid width */
.container {
    width: min(90vw, 1200px);
}
```

## 🎯 Common Media Queries

### Orientation

```css
/* Portrait mode */
@media (orientation: portrait) {
    .content { flex-direction: column; }
}

/* Landscape mode */
@media (orientation: landscape) {
    .content { flex-direction: row; }
}
```

### Device Pixel Ratio

```css
/* High DPI screens */
@media (-webkit-min-device-pixel-ratio: 2),
       (min-resolution: 192dpi) {
    body {
        -webkit-font-smoothing: antialiased;
    }
}
```

### Reduced Motion

```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

## 🔧 JavaScript Helpers

### Detect Mobile

```javascript
const isMobile = window.matchMedia('(max-width: 768px)').matches;
```

### Detect Touch Device

```javascript
const isTouchDevice = 'ontouchstart' in window;
```

### Viewport Dimensions

```javascript
const viewportWidth = window.innerWidth;
const viewportHeight = window.innerHeight;
```

### Orientation

```javascript
const isLandscape = window.matchMedia('(orientation: landscape)').matches;
```

### Listen for Resize

```javascript
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        // Your code here
    }, 250);
});
```

### Listen for Orientation Change

```javascript
window.addEventListener('orientationchange', () => {
    setTimeout(() => {
        // Your code here
    }, 100);
});
```

## 📱 iOS Specific

### Prevent Zoom on Input

```css
input, select, textarea {
    font-size: 16px; /* Prevents iOS zoom */
}
```

### Safe Area Insets

```css
body {
    padding-left: env(safe-area-inset-left);
    padding-right: env(safe-area-inset-right);
}
```

### Viewport Height Fix

```javascript
// Fix iOS viewport height
const setVH = () => {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
};

setVH();
window.addEventListener('resize', setVH);
```

## 🎨 Bootstrap 5 Classes

### Display

```html
<!-- Responsive display utilities -->
<div class="d-none d-sm-block">Hidden on XS</div>
<div class="d-block d-md-none">Visible only on mobile</div>
```

### Flexbox

```html
<!-- Stack on mobile, row on desktop -->
<div class="d-flex flex-column flex-md-row">
    <div>Item 1</div>
    <div>Item 2</div>
</div>
```

### Spacing

```html
<!-- Responsive margins -->
<div class="mb-3 mb-md-5">Content</div>

<!-- Responsive padding -->
<div class="p-2 p-md-4">Content</div>
```

### Text Alignment

```html
<!-- Center on mobile, left on desktop -->
<div class="text-center text-md-start">Text</div>
```

## 🔍 Testing Tools

### Browser DevTools

```
Chrome:   F12 → Toggle device toolbar (Ctrl+Shift+M)
Firefox:  Ctrl+Shift+M (Responsive Design Mode)
Safari:   Develop → Enter Responsive Design Mode
Edge:     F12 → Toggle device emulation (Ctrl+Shift+M)
```

### Common Test Sizes

```
iPhone SE:        320 x 568
iPhone 12:        390 x 844
iPhone 12 Pro Max: 428 x 926
iPad Mini:        768 x 1024
iPad Pro:         1024 x 1366
Desktop:          1920 x 1080
```

## ✅ Checklist

### Before Deployment

- [ ] Test on iPhone (Safari)
- [ ] Test on Android (Chrome)
- [ ] Test on iPad
- [ ] Test portrait and landscape
- [ ] Verify touch targets ≥ 44px
- [ ] Check text readability
- [ ] Verify no horizontal scroll
- [ ] Test keyboard navigation
- [ ] Check color contrast
- [ ] Test with screen reader
- [ ] Verify print layout
- [ ] Test on slow connection

## 📚 Resources

- [MDN Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Can I Use](https://caniuse.com/)
- [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/)
- [Material Design](https://material.io/design)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

## 🆘 Common Issues

### Issue: iOS Zoom on Input Focus
**Solution**: Set input font-size to 16px or larger

### Issue: Viewport Height on iOS
**Solution**: Use CSS custom property with JS fix

### Issue: Horizontal Scroll
**Solution**: Add `overflow-x: hidden` to body

### Issue: Touch Targets Too Small
**Solution**: Ensure min-height and min-width of 44px

### Issue: Hover Effects on Touch
**Solution**: Use `@media (hover: hover)` query

---

**Quick Reference Version**: 2.0.0  
**Last Updated**: November 2025  
**For**: Unit Converter Pro
