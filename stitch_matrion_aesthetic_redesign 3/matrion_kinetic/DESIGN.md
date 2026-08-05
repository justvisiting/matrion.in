---
name: Matrion Kinetic
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1c1b1d'
  surface-container: '#201f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e5e1e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e1e4'
  inverse-on-surface: '#313032'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#ffb59a'
  on-secondary: '#5a1b00'
  secondary-container: '#ff5e07'
  on-secondary-container: '#531900'
  tertiary: '#fff5de'
  on-tertiary: '#3b2f00'
  tertiary-container: '#fed639'
  on-tertiary-container: '#715d00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#802a00'
  tertiary-fixed: '#ffe179'
  tertiary-fixed-dim: '#eac324'
  on-tertiary-fixed: '#231b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#131315'
  on-background: '#e5e1e4'
  surface-variant: '#353437'
  surface-charcoal: '#121214'
  surface-glass: rgba(255, 255, 255, 0.03)
  ink-bone: '#FCFAF6'
  stroke-subtle: rgba(255, 255, 255, 0.1)
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 84px
    letterSpacing: -0.02em
  display-xl-mobile:
    fontFamily: Playfair Display
    fontSize: 44px
    fontWeight: '700'
    lineHeight: 52px
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style
The design system for Matrion is built on the narrative of "Sophisticated Precision." It positions the brand as an authoritative leader in enterprise AI consultancy, blending the intellectual heritage of traditional consulting with the high-velocity engineering of modern AI.

The aesthetic follows a **Sophisticated Tech** movement—a fusion of Minimalism and Glassmorphism. It prioritizes clarity through generous whitespace and a rigorous grid, while using translucent "glass" surfaces to represent the transparency of AI models. The visual tone is elite, technical, and forward-thinking, designed to instill confidence in C-suite stakeholders while respecting the sensibilities of technical architects.

## Colors
This design system utilizes a **Dark Mode First** philosophy to emphasize the "Digital Cyan" and "Innovation Orange" accents. 

- **Primary (Digital Cyan):** Used for primary actions, data visualizations, and highlighting "intelligent" system states.
- **Secondary (Innovation Orange):** Reserved for high-impact alerts, strategic calls to action, and human-centric touchpoints.
- **Neutral (Charcoal & Bone):** The foundation is built on deep, desaturated charcoals (`#0A0A0C`) to ensure high contrast for the `#FCFAF6` typography.
- **Gradients:** Subtle linear gradients (135°) from Primary to a deeper shade of blue are used to indicate movement and "active processing" in AI components.

## Typography
The typography strategy creates a tension between tradition and technology. 
- **Headlines:** Use *Playfair Display* to convey established authority and expertise. Tracking should be tightened in larger sizes for a bespoke, editorial feel.
- **Body:** *Geist* provides a clean, geometric utility that feels engineered and highly legible in dense technical documentation.
- **Metadata:** *JetBrains Mono* is used for code snippets, technical labels, and system status indicators to reinforce the consultancy’s engineering DNA.

## Layout & Spacing
The layout follows a **12-column fixed grid** on desktop with a heavy emphasis on asymmetrical balance. 
- **Whitespace:** Use an 8px base-unit. Sections should be separated by massive vertical padding (e.g., 128px or 160px) to signify premium positioning.
- **Breakpoints:** 
    - Desktop: 1200px+ (12 columns)
    - Tablet: 768px - 1199px (8 columns)
    - Mobile: <767px (4 columns)
- **Rhythm:** Elements should align to a strict baseline grid to ensure "engineering excellence" is felt in the alignment of every component.

## Elevation & Depth
Depth is created through **Glassmorphism** rather than traditional shadows.
- **Surface Strategy:** Use a tiered system where the background is the darkest layer. Floating panels (cards, modals) use a semi-transparent blur (Backdrop Filter: blur 20px) and a 1px solid border at 10% white opacity to define edges.
- **Active Elevation:** When a component is interacted with, it should gain a subtle "Inner Glow" using the Primary Cyan at low opacity rather than a drop shadow.
- **Gradients:** Use mesh gradients in the background—very large, soft-focus blobs of Cyan and Orange—to create a sense of atmospheric depth behind the glass panels.

## Shapes
The shape language is **Soft (0.25rem)**. 
While the industry often leans into hyper-rounded "pill" shapes, this design system uses subtle radius corners to maintain a professional, architectural feel. 
- **Buttons:** Small radius (4px) for a sharp, precise look.
- **Cards:** 8px radius for container surfaces.
- **Accents:** Use 45-degree chamfered corners for technical labels or "terminal" style UI elements to evoke hardware engineering.

## Components
- **Primary Buttons:** High-contrast Digital Cyan backgrounds with black text. No border. On hover, apply a 4px glow effect in the same hue.
- **Glass Cards:** Background: `rgba(255, 255, 255, 0.03)`, Border: `1px solid rgba(255, 255, 255, 0.1)`, Backdrop-blur: `16px`.
- **Inputs:** Ghost-style inputs with only a bottom border (1px). Focus state triggers the bottom border to transition to Cyan with a "loading" pulse animation.
- **Chips:** Monospaced text inside a 1px bordered box with a subtle background tint.
- **Data Visualization:** Use thin line weights (1px) and avoid fills. If fills are necessary, use 10% opacity gradients.
- **AI "Pulse" Indicator:** A small, 8px circular component using the Primary Cyan with a concentric rings animation to indicate active background processing.