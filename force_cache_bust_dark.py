import glob, re

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        content = content.replace('src="assets/matrion-dark.jpeg"', 'src="assets/matrion-dark.jpeg?v=3"')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

