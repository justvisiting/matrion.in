import glob, re

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        # Double the logo height
        content = content.replace('class="h-12 w-auto rounded-sm"', 'class="h-24 w-auto rounded-sm"')
        # Update header to not crop the logo
        content = content.replace('h-[72px]', 'min-h-[72px]')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

