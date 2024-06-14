# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html


from datetime import datetime
import subprocess

current_year = datetime.now().year
organization_name = "pyOpenSci"
# -- Project information -----------------------------------------------------

project = "pyOpenSci Python Package Guide"
copyright = f"{current_year}, {organization_name}"
author = "pyOpenSci Community"

# Get the latest Git tag - there might be a prettier way to do this but...
try:
    release_value = (
        subprocess.check_output(["git", "describe", "--tags"])
        .decode("utf-8")
        .strip()
    )
    release_value = release_value[:4]
except subprocess.CalledProcessError:
    release_value = "0.1"  # Default value in case there's no tag

# Update the release value
release = release_value


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx.ext.todo",
]

# colon fence for card support in md
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 3

# Suppress as we have includes that don't need to start at h1
suppress_warnings = ["myst.header"]

# For generating sitemap
html_baseurl = "https://www.pyopensci.org/software-peer-review/"
sitemap_url_scheme = "{link}"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_title = "Software Peer Review Guide"
html_logo = "_static/logo.png"
html_static_path = ["_static"]
html_js_files = ["matomo.js"]

# Theme options
html_theme_options = {
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "https://www.pyopensci.org/images/favicon.ico",
        },
    ],
    "announcement": "<p><a href='https://www.github.com/pyopensci/software-submission/'>Submit Your Python Package for Peer Review!</a></p>",
    "external_links": [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/python-package-guide",
            "name": "Python Packaging Guide",
        },
        {
            "url": "https://pyopensci.org/handbook",
            "name": "Handbook",
        },
    ],
    "icon_links": [
        {
            "name": "Mastodon",
            "url": "https://fosstodon.org/@pyOpenSci",
            "icon": "fa-brands fa-mastodon",
        },
    ],
    "logo": {
        "text": "Peer Review Guide",
        "image_dark": "logo-dark-mode.png",
        "image_light": "logo-light-mode.png",
        "alt_text": "pyOpenSci Software Peer Review Guide. The pyOpenSci logo is a purple flower with pyOpenSci under it. The o in open sci is the center of the flower",
    },
    "header_links_before_dropdown": 4,
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "github_url": "https://github.com/pyOpenSci/software-peer-review",
    "footer_start": ["copyright"],
    "footer_end": [],
}

# html_theme_options["analytics"] = {
#     "google_analytics_id": "UA-141260825-1",
# }

html_context = {
    "github_user": "pyopensci",
    "github_repo": "software-peer-review",
    "github_version": "main",
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
    ".nox",
    "README.md",
]


# -- Options for HTML output -------------------------------------------------


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["pyos.css"]
