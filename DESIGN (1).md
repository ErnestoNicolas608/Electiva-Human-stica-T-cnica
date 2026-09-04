---
name: NetChecker Operations
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#b9ccb2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#84967e'
  outline-variant: '#3b4b37'
  surface-tint: '#00e639'
  primary: '#ebffe2'
  on-primary: '#003907'
  primary-container: '#00ff41'
  on-primary-container: '#007117'
  inverse-primary: '#006e16'
  secondary: '#a6e6ff'
  on-secondary: '#003543'
  secondary-container: '#14d1ff'
  on-secondary-container: '#00566b'
  tertiary: '#fff7f6'
  on-tertiary: '#690006'
  tertiary-container: '#ffd2cd'
  on-tertiary-container: '#c40015'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#72ff70'
  primary-fixed-dim: '#00e639'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#00530e'
  secondary-fixed: '#b7eaff'
  secondary-fixed-dim: '#4cd6ff'
  on-secondary-fixed: '#001f28'
  on-secondary-fixed-variant: '#004e60'
  tertiary-fixed: '#ffdad6'
  tertiary-fixed-dim: '#ffb4ab'
  on-tertiary-fixed: '#410002'
  on-tertiary-fixed-variant: '#93000c'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: JetBrains Mono
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -1px
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.5px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 1px
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max: 1440px
---

## Brand & Style
The design system is engineered for high-stakes network monitoring and cybersecurity oversight. It evokes the atmosphere of a professional Network Operations Center (NOC) through a "Cyber-Tech" aesthetic. The visual narrative balances institutional authority with high-performance technical precision.

The style utilizes **Glassmorphism** and **Modern Minimalism** to manage high data density without overwhelming the operator. Surfaces are deep and atmospheric, using semi-transparent layers to create a sense of digital depth. The emotional response is one of calm control, clarity, and rapid technical insight.

## Colors
The palette is rooted in a "Pure Black" environment to maximize contrast and reduce eye strain during long monitoring sessions. 

- **Primary (Neon Green):** Reserved for "Healthy" status, successful pings, and active system uplinks.
- **Secondary (Electric Blue):** Used for data visualization, information callouts, and neutral network traffic.
- **Tertiary (Alert Red):** Specifically for critical breaches, downed nodes, or unauthorized access attempts.
- **Neutral:** A scale of deep grays and blacks used to establish hierarchy through surface luminance rather than color.

## Typography
The typography strategy employs a dual-font system to separate narrative content from technical data.

- **JetBrains Mono** is the "Technical Voice," used for headlines, status labels, and all numerical data. It ensures that IP addresses and log timestamps remain perfectly legible and aligned.
- **Inter** is the "Functional Voice," used for body text, descriptions, and tooltips to provide a modern, highly readable interface for long-form reports.

Always use Monospaced variants for data tables to prevent "jumping" characters when values update in real-time.

## Layout & Spacing
This design system utilizes a **Fluid Grid** model based on a 4px baseline shift. 

- **Dashboard Layout:** A 12-column grid on desktop, transitioning to a single column on mobile. 
- **Density:** High-density spacing is preferred. Use 8px (2 units) for internal component spacing and 16px (4 units) for gaps between major layout modules.
- **The "Grid" Layer:** A subtle 32px repeating square grid pattern should be visible in the background canvas at 3% opacity to reinforce the "Engineering" feel.

## Elevation & Depth
Depth is expressed through **translucency and luminosity** rather than traditional drop shadows.

1.  **Canvas:** The base layer (#050505) with the subtle grid pattern.
2.  **Panels:** Semi-transparent surfaces (80% opacity) with a `20px` backdrop blur. This creates the "Glassmorphism" effect.
3.  **Borders:** Instead of shadows, use 1px solid borders. For inactive elements, use `rgba(255, 255, 255, 0.1)`. 
4.  **Glow:** Active or Critical states use a `0px 0px 12px` outer glow (drop shadow with 0 spread) matching the status color (Green/Blue/Red) at 40% opacity.

## Shapes
Shapes in this design system are "Soft" but disciplined. A 4px (`rounded`) base radius is used for cards and buttons to maintain a professional, hardware-like appearance. 

Avoid "Pill" shapes for functional buttons; keep them rectangular with subtle rounding to match the geometric nature of network diagrams and technical schematics.

## Components
- **Buttons:** Primary buttons use a solid Neon Green fill with black text. Secondary buttons use a transparent background with a 1px Neon Green border.
- **Status Chips:** Small, monospaced text indicators with a leading "indicator dot." The dot should have a CSS `pulse` animation if the status is "Live."
- **Data Cards:** Cards must feature a "Header" section with a 1px bottom border. Include a "Terminal" style header (e.g., `> STATS_01`) in the top-left corner.
- **Input Fields:** Ghost-style inputs with a 1px bottom border only. On focus, the border glows Neon Green.
- **Minimalist Charts:** Sparklines and area charts should use a single stroke color (Electric Blue) with a subtle gradient fill (10% opacity) beneath the line. No grid lines inside the charts—only the data points.
- **Alert Banner:** A high-contrast strip using the Tertiary Red, utilizing a "Caution" diagonal stripe pattern on the far left edge.