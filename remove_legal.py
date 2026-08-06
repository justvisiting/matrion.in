import glob, re

legal_regex = r'<div class="flex flex-col gap-4">\s*<span\s*class="font-label-mono text-label-mono text-on-surface-variant uppercase tracking-widest mb-2">Legal</span>\s*<a class="text-on-surface-variant hover:text-primary transition-all"\s*href="#">Privacy Policy</a>\s*<a class="text-on-surface-variant hover:text-primary transition-all"\s*href="#">Terms of Service</a>\s*</div>'

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        content = re.sub(legal_regex, '', content, flags=re.DOTALL)
        content = content.replace('sm:grid-cols-4', 'sm:grid-cols-3')
        content = content.replace('sm:grid-cols-5', 'sm:grid-cols-4')
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

