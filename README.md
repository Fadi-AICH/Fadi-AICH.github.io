# Portfolio Fadix

Cybersecurity portfolio built with Jekyll — write-ups, certifications roadmap, and admin CMS.


## Project Structure

```
├── _config.yml              # Jekyll configuration
├── _data/
│   └── certifications.yml   # 15-course roadmap data
├── _includes/
│   ├── sidebar.html         # Chirpy-style sidebar
│   ├── toc.html             # Table of contents
│   ├── trending-tags.html   # Trending tags widget
│   └── netlify-identity.html
├── _layouts/
│   ├── default.html         # Base layout
│   ├── home.html            # Home page with card list
│   ├── post.html            # Write-up layout with TOC
│   ├── page.html            # Static pages
│   └── certifications.html  # Certification grid + progress bar
├── _posts/                  # Write-ups and notes (Markdown)
├── _sass/                   # (optional SCSS partials)
├── admin/
│   ├── index.html           # Decap CMS entry point
│   └── config.yml           # CMS collections config
├── assets/
│   ├── css/style.css        # Full Chirpy-inspired theme
│   ├── js/main.js           # Sidebar toggle + dark/light mode
│   └── img/                 # Images (fadix.jpg goes here)
├── certifications/
│   └── index.html           # Certifications roadmap page
├── index.html               # Home
├── categories.html
├── tags.html
├── archives.html
├── about.md
└── Gemfile
```
