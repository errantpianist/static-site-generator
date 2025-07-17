
<div align="center">
   <h1>📝 Static Site Generator</h1>
   <p>A simple Python static site generator for Markdown content, with GitHub Pages support and configurable base paths.</p>
</div>


## ✨ Features
- Converts Markdown files to HTML using a template
- Recursively processes content directories
- Copies static assets (CSS, images, etc.)
- Configurable base path for GitHub Pages or local hosting
- Easy deployment to GitHub Pages (output to `docs/`)


## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Git

### Local Development
1. Clone the repository:
   ```sh
   git clone https://github.com/errantpianist/static-site-generator.git
   cd static-site-generator
   ```
2. Build and serve the site locally:
   ```sh
   ./main.sh
   ```
   This will build the site into the `docs/` directory and serve it at [http://localhost:8888](http://localhost:8888).

### Production Build for GitHub Pages
1. Build the site with the correct base path:
   ```sh
   ./build.sh
   ```
   This will generate the site into the `docs/` directory with `/static-site-generator/` as the base path.
2. Commit and push your changes:
   ```sh
   git add .
   git commit -m "Build site for GitHub Pages"
   git push
   ```
3. Configure GitHub Pages in your repo settings:
   - Source: `main` branch
   - Folder: `/docs`
   - Your site will be live at: `https://errantpianist.github.io/static-site-generator/`


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
