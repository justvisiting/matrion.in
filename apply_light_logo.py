import glob

light_files = ['v7.html', 'v7-light-2.html', 'v7-light-4.html', 'index.html']

for file in light_files:
    try:
        content = open(file, 'r').read()
        content = content.replace('src="assets/matrion-logo-v1.jpeg"', 'src="assets/matrion-light-transparent.png"')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

