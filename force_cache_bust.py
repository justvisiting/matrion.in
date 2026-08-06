import glob, re

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        content = content.replace('src="assets/matrion-light-transparent.png"', 'src="assets/matrion-light-transparent.png?v=2"')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

