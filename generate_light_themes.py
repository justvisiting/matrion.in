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
        open(filename, 'w').write(new_html)
        print(f"Created {filename}")

    updates1 = {
        "background": "#FAFAFA",
        "surface": "#FFFFFF",
        "surface-container": "#F5F5F5",
        "surface-container-lowest": "#FFFFFF",
        "on-background": "#111111",
        "on-surface": "#111111",
        "on-surface-variant": "#555555",
        "stroke-subtle": "rgba(0,0,0,0.1)",
        "surface-glass": "rgba(0,0,0,0.03)",
        "primary-fixed-dim": "#007A85",
        "on-primary-fixed": "#FFFFFF",
        "surface-container-highest": "#EAEAEA",
        "surface-container-low": "#FAFAFA",
        "outline": "#D1D5DB"
    }

    updates2 = {
        "background": "#F7F5F0",
        "surface": "#FFFFFF",
        "surface-container": "#EBE7DF",
        "surface-container-lowest": "#FFFFFF",
        "on-background": "#1E232A",
        "on-surface": "#1E232A",
        "on-surface-variant": "#6E757F",
        "stroke-subtle": "rgba(0,0,0,0.12)",
        "surface-glass": "rgba(0,0,0,0.03)", 
        "primary-fixed-dim": "#0D2B52",
        "on-primary-fixed": "#FFFFFF",
        "surface-container-highest": "#DCD7CC",
        "surface-container-low": "#F7F5F0",
        "outline": "#C8C2B3"
    }

    updates3 = {
        "background": "#F0F4F8",
        "surface": "#FFFFFF",
        "surface-container": "#E1E8EF",
        "surface-container-lowest": "#FFFFFF",
        "on-background": "#0F172A",
        "on-surface": "#0F172A",
        "on-surface-variant": "#475569",
        "stroke-subtle": "rgba(15, 23, 42, 0.1)",
        "surface-glass": "rgba(255, 255, 255, 0.4)",
        "primary-fixed-dim": "#4F46E5",
        "on-primary-fixed": "#FFFFFF",
        "surface-container-highest": "#CBD5E1",
        "surface-container-low": "#F0F4F8",
        "outline": "#94A3B8"
    }

    make_version("v7-light-1.html", updates1)
    make_version("v7-light-2.html", updates2)
    make_version("v7-light-3.html", updates3)

except Exception as e:
    print(f"Error: {e}")
