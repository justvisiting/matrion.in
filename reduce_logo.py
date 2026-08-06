import glob, re

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        content = content.replace('class="h-24 w-auto rounded-sm"', 'class="h-16 w-auto rounded-sm"')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

