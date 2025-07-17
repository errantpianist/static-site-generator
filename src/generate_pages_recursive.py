import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively generate HTML pages for every markdown file in dir_path_content,
    using template_path, and write to dest_dir_path, preserving directory structure.
    """
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)
        if os.path.isdir(entry_path):
            # Recurse into subdirectory
            os.makedirs(dest_entry_path, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, dest_entry_path)
        elif os.path.isfile(entry_path) and entry_path.endswith('.md'):
            # Generate HTML file for markdown
            html_filename = os.path.splitext(entry)[0] + '.html'
            dest_html_path = os.path.join(dest_dir_path, html_filename)
            generate_page(entry_path, template_path, dest_html_path)
