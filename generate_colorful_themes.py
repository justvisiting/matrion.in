import json, re

try:
    text = open('v7.html').read()
    text = text.replace('<html class="dark"', '<html class="light"')

    match = re.search(r'("colors":\s*)(\{.*?\})(\s*,\s*"borderRadius")', text, re.DOTALL)
    colors_str = match.group(2)
    colors = json.loads(colors_str)

    def make_version(filename, updates):
        new_colors = dict(colors)
        new_colors.update(updates)
        new_colors_str = json.dumps(new_colors, indent=48).replace("}", "                                        }")
        new_html = text[:match.start(2)] + new_colors_str + text[match.end(2):]
        # Ensure light themes use the dark logo so it's visible
        new_html = new_html.replace('assets/logo-true-transparent.png', 'logo-dark.jpg')
        open(filename, 'w').write(new_html)
        print(f"Created {filename}")

    # Colorful 1: Ocean Blue
    updates4 = {
        "background": "#F0F9FF",  # Sky 50
        "surface": "#FFFFFF",
        "surface-container": "#E0F2FE", # Sky 100
        "surface-container-lowest": "#FFFFFF",
        "on-background": "#082F49", # Sky 900
        "on-surface": "#082F49",
        "on-surface-variant": "#0369A1", # Sky 700
        "stroke-subtle": "rgba(2, 132, 199, 0.2)",
        "surface-glass": "rgba(255,255,255,0.7)",
        "primary-fixed-dim": "#0284C7", # Sky 600
        "on-primary-fixed": "#FFFFFF",
        "surface-container-highest": "#BAE6FD",
        "surface-container-low": "#F0F9FF",
        "outline": "#7DD3FC"
    }

    # Colorful 2: Mint / Emerald
    updates5 = {
        "background": "#ECFDF5", # Emerald 50
        "surface": "#FFFFFF",
        "surface-container": "#D1FAE5", # Emerald 100
        "surface-container-lowest": "#FFFFFF",
        "on-background": "#022C22", # Emerald 900
        "on-surface": "#022C22",
        "on-surface-variant": "#047857", # Emerald 700
        "stroke-subtle": "rgba(5, 150, 105, 0.2)",
        "surface-glass": "rgba(255,255,255,0.7)", 
        "primary-fixed-dim": "#059669", # Emerald 600
        "on-primary-fixed": "#FFFFFF",
        "surface-container-highest": "#A7F3D0",
        "surface-container-low": "#ECFDF5",
        "outline": "#6EE7B7"
    }

    # Colorful 3: Cyber Violet
    updates6 = {
        "background": "#FAF5FF", # Purple 50
        "surface": "#FFFFFF",
        "surface-container": "#F3E8FF", # Purple 100
        "surface-container-lowest": "#FFFFFF",
        "on-background": "#3B0764", # Purple 900
        "on-surface": "#3B0764",
        "on-surface-variant": "#7E22CE", # Purple 700
        "stroke-subtle": "rgba(147, 51, 234, 0.2)",
        "surface-glass": "rgba(255, 255, 255, 0.7)",
        "primary-fixed-dim": "#9333EA", # Purple 600
        "on-primary-fixed": "#FFFFFF",
        "surface-container-highest": "#E9D5FF",
        "surface-container-low": "#FAF5FF",
        "outline": "#D8B4FE"
    }

    make_version("v7-light-4.html", updates4)
    make_version("v7-light-5.html", updates5)
    make_version("v7-light-6.html", updates6)

except Exception as e:
    print(f"Error: {e}")
