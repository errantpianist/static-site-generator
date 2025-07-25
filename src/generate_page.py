
import os
import re
from extractor import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read markdown
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown = f.read()
    # Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    # Convert markdown to HTML
    html_content = markdown_to_html_node(markdown).to_html()
    # Extract title
    title = extract_title(markdown)
    # Replace placeholders
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    # Replace all href and src attributes that start with / to use the basepath
    # This covers href="/..., src="/..., href='/..., src='/... (double and single quotes)
    page = re.sub(r'(href|src)=(["\"])\/', r'\1=\2' + basepath, page)
    # Ensure dest directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    # Write output
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(page)
