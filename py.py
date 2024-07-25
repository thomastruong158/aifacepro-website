from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))

# List of pages to render
pages = ['index.html', 'about.html', 'privacy-policy.html', 'terms-of-use.html']

# Get the current year
current_year = datetime.now().year

# Render each page
for page in pages:
    template = env.get_template(page)
    output = template.render(current_year=current_year)
    
    # Create the dist directory if it doesn't exist
    os.makedirs('dist', exist_ok=True)
    
    # Write to file
    with open(f'dist/{page}', 'w') as f:
        f.write(output)

print("All pages rendered successfully!")