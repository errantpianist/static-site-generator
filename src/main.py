
import os
import shutil

from generate_page import generate_page


def copy_static(src, dst):
    """Recursively copy all files and directories from src to dst, logging each file copied."""
    if not os.path.exists(src):
        print(f"Source directory {src} does not exist.")
        return
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_static(s, d)
        else:
            shutil.copy(s, d)
            print(f"Copied: {d}")

def main():
    # Determine project root (one level up from this file)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    static_dir = os.path.join(project_root, 'static')
    public_dir = os.path.join(project_root, 'public')
    content_md = os.path.join(project_root, 'content', 'index.md')
    template_html = os.path.join(project_root, 'template.html')
    dest_html = os.path.join(public_dir, 'index.html')

    # Delete public directory if it exists
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    # Copy static files to public directory
    copy_static(static_dir, public_dir)

    # Generate the main page
    generate_page(content_md, template_html, dest_html)




if __name__ == "__main__":
    main()
