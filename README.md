# <img src="images/logo/logo.png" width=40 /> pyOpenSci Guidebook



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7101778.svg)](https://doi.org/10.5281/zenodo.7101778)

![Deploy Book](https://github.com/pyOpenSci/contributing-guide/actions/workflows/book.yml/badge.svg)

https://pyopensci.org/contributing-guide/

pyOpenSci's guide for developing, reviewing, and maintaining packages.

## Automated GitHub Actions Build

GitHub Actions automatically builds the Jupyter book whenever changes are pushed to GitHub. This lets you view any changes you made without building locally and without affecting the contributing guide website.

* If the changes are pushed to a branch other than main, you can view the html as an "artifact" of the GitHub Actions build:

1. Go to https://github.com/pyOpenSci/contributing-guide/actions to view recent builds.
2. Locate your build. You can use the search field at the top of the page to filter by author (actor:), branch (branch:), and more.
3. Once you click on your build, select "book-html" in the "Artifacts" near the bottom of the page. If your build was unsuccessful, this won't appear. You can view the issues with the build by clicking on the "deploy-book" job, which will have a red x next to it.
4. Unzip the book-html.zip file into a separate directory.
5. Open "index.html" from the directory with the unzipped files. The book should open in your web browser.


* When changes are merged into main, the book contents are pushed to the special branch "gh-pages", which updates the website: https://www.pyopensci.org/contributing-guide.

** This is done automatically by a [custom GitHub Action written by peaceiris](https://github.com/peaceiris/actions-gh-pages). 

** Before merging changes into main sure to check that the contents of the book appear correct by downloading the html artifact from the GitHub Actions branch build (described above) and/or by building locally (described below).

## Build the guide locally

The pyOpenSci guidebook is written using [Jupyter Books](https://github.com/executablebooks/jupyter-book).

To build the guide locally, take the following steps:

* Clone this repository:

  ```
  git clone https://github.com/pyOpenSci/contributing-guide
  ```
* Install Jupyter Book

  ```
  pip install -U jupyter-book

  OR

  $ cd contributing-guide
  $ pip install -U -r  requirements.txt

  ```
* Build the guide

  ```
  # Cd to the repo if you are not already in it!
  $ cd contributing-guide
  # Build the book locally!
  $ jupyter-book build .
  ```

* To view the guide:

  Open \_build/html/index.html

*  To clean out old pages of your book:

  ```
  $ jupyter-book clean .
  ```


## Contributing to this guide

We welcome and issues and pull-requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/contributing-guide/issues/new/choose).
