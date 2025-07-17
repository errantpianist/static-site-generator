
<div align="center">
   <h1>📝 Static Site Generator</h1>
   <p>A simple Python static site generator for Markdown content, with GitHub Pages support and configurable base paths.</p>
</div>

---

<div align="center">
   <img src="assets/screenshot.png" alt="Site Screenshot" width="600"/>
</div>

---

## ✨ Features
- Converts Markdown files to HTML using a template
- Recursively processes content directories
- Copies static assets (CSS, images, etc.)
- Configurable base path for GitHub Pages or local hosting
- Easy deployment to GitHub Pages (output to `docs/`)



## 🚀 Getting Started

### About the Base Path
Your site can be served from any subdirectory, not just the root. This is important for GitHub Pages, which serves your site from `/REPO_NAME/` by default. The generator uses a `basepath` argument to ensure all links and assets work correctly.

**Local development:** Uses `/` as the base path (site root).

**GitHub Pages:** Uses `/<REPO_NAME>/` as the base path (e.g., `/static-site-generator/`).

You can customize the base path by passing it as the first argument to `main.py`.

### Prerequisites
- Python 3.7+
- Git


### Local Development
1. Clone the repository:
   ```sh
   git clone https://github.com/errantpianist/static-site-generator.git
   cd static-site-generator
   ```
2. Build and serve the site locally (base path is `/`):
   ```sh
   ./main.sh
   ```
   This will build the site into the `docs/` directory and serve it at [http://localhost:8888](http://localhost:8888).


### Production Build for GitHub Pages
1. Build the site for GitHub Pages (base path is your repo name):
   ```sh
   ./build.sh
   # or manually:
   python3 src/main.py "/static-site-generator/"
   ```
   This will generate the site into the `docs/` directory with `/static-site-generator/` as the base path.
   If you change your repo name, update the base path accordingly (e.g., `/my-new-repo/`).
2. Commit and push your changes:
   ```sh
   git add .
   git commit -m "Build site for GitHub Pages"
   git push
   ```
3. Configure GitHub Pages in your repo settings:
   - Source: `main` branch
   - Folder: `/docs`
   - Your site will be live at: `https://YOURNAME.github.io/static-site-generator/`


## 🗂️ Project Structure
```
content/      # Markdown files and folders for your site content
static/       # Static assets (CSS, images, etc.)
docs/         # Generated site output (for GitHub Pages)
src/          # Python source code
main.sh       # Script for local dev build and server
build.sh      # Script for production build (GitHub Pages)
template.html # HTML template for all pages
```


## 🎨 Customization
- Edit `template.html` to change the site layout.
- Add Markdown files to `content/` to create new pages.
- Add images, CSS, etc. to `static/`.


## 🙏 Credits
- Developed by [errantpianist](https://github.com/errantpianist)
- Inspired by the Boot.dev static site generator project


## 📄 License
MIT License
