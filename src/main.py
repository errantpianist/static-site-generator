

import os
import shutil
import sys

from generate_pages_recursive import generate_pages_recursive


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
    public_dir = os.path.join(project_root, 'docs')
    content_dir = os.path.join(project_root, 'content')
    template_html = os.path.join(project_root, 'template.html')

    # Get basepath from CLI argument, default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath += "/"

    # Delete docs directory if it exists
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)

    # Copy static files to docs directory
    copy_static(static_dir, public_dir)

    # Recursively generate all pages, passing basepath
    generate_pages_recursive(content_dir, template_html, public_dir, basepath)




if __name__ == "__main__":
    main()
