import glob, re

# HTML to replace in root .html files
old_text = r'We engineer highly efficient\s+workflows and API integrations that replace tedious manual\s+tasks\. By intelligently connecting your disparate systems, we\s+dramatically accelerate your operational speed\.'
new_text = "We transform fragmented operations into intelligent, seamlessly connected ecosystems. The result is faster execution, greater operational efficiency, and a business that moves with the speed and precision that today's market demands."

html_files = glob.glob('*.html')
for file in html_files:
    try:
        content = open(file, 'r').read()
        content = re.sub(old_text, new_text, content)
        open(file, 'w').write(content)
        print(f"Updated {file}")
    except Exception as e:
        print(f"Error updating {file}: {e}")

# Update brochure.html
brochure_path = 'collateral/brochure.html'
try:
    content = open(brochure_path, 'r').read()
    old_brochure_text = r'Engineering workflows and API integrations to replace manual bottlenecks and accelerate delivery\.'
    new_brochure_text = "Transforming fragmented operations into intelligent, connected ecosystems for faster execution and efficiency."
    content = re.sub(old_brochure_text, new_brochure_text, content)
    open(brochure_path, 'w').write(content)
    print(f"Updated {brochure_path}")
except Exception as e:
    print(f"Error updating brochure: {e}")

