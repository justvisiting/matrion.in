import re

new_links = """<span
                                                class="font-label-mono text-label-mono text-on-surface-variant uppercase tracking-widest mb-2">Themes</span>
                                        <a class="text-on-surface-variant hover:text-primary transition-all"
                                                href="index.html">1. Crisp</a>
                                        <a class="text-on-surface-variant hover:text-primary transition-all"
                                                href="v7-dark.html">2. Dark</a>
                                        <a class="text-on-surface-variant hover:text-primary transition-all"
                                                href="v7-light-2.html">3. Warm</a>
                                        <a class="text-on-surface-variant hover:text-primary transition-all"
                                                href="v7-light-4.html">4. Ocean</a>"""

for f in ['v7.html', 'v7-dark.html', 'v7-light-2.html', 'v7-light-4.html']:
    try:
        content = open(f).read()
        content = re.sub(r'<span\s+class="font-label-mono text-label-mono text-on-surface-variant uppercase tracking-widest mb-2">Themes</span>.*?4\. Ocean</a>', new_links, content, flags=re.DOTALL)
        open(f, 'w').write(content)
        print("Updated " + f)
    except Exception as e:
        print(f"Error in {f}: {e}")
