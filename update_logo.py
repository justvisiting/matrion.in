import glob, re

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        content = content.replace('src="logo-dark.jpg"', 'src="assets/matrion-logo-v1.jpeg"')
        content = content.replace('src="assets/logo-true-transparent.png"', 'src="assets/matrion-logo-v1.jpeg"')
        # Also just in case they were updated differently
        content = content.replace('src="logo.png"', 'src="assets/matrion-logo-v1.jpeg"')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

