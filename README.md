# <img src="images/logo/logo.png" width=40 /> pyOpenSci Guidebook

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/contributing-guide?color=purple&display_name=tag&style=plastic)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7101778.svg)](https://doi.org/10.5281/zenodo.7101778)

![deploy-book](https://github.com/pyOpenSci/contributing-guide/actions/workflows/book.yml/badge.svg)  [![CircleCI Book Preview](https://circleci.com/gh/pyOpenSci/contributing-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/contributing-guide) 

https://pyopensci.org/contributing-guide/

pyOpenSci's guide for developing, reviewing, and maintaining packages.

## Automated build and publishing

Whenever a pull request is opened or changes are pushed to any branch of the base repository, the book is built (separately) by both GitHub Actions and CircleCI. 

### Why both GitHub Actions and CircleCI?

- GitHub Actions is the main build tool. In addition to building whenever a pull request is opened from a fork, it handles publishing the book when changes are made to the main branch (e.g. once the pull request is merged). When that happens, it pushes the built html files to the gh-pages branch, which publishes the book to the [website](https://pyopensci.org/contributing-guide/).
- CircleCI's build is redundant, but it offers an easier way of viewing the built html in browser WITHOUT merging the changes to main or downloading files. See [How do you preview the book](https://github.com/pyopensci/contributing-guide/#how-do-you-preview-the-book) below for details. 

### How do you preview the website?
*Note*: If you are working on a fork, you'll have to open a pull request to the base repository to preview the website. 
- *(Recommended)* Via the artifact redirector workflow: When viewing the checks in a pull request, click "Details" next to the "Click to preview rendered book" to be automatically taken to the CircleCI index.html preview. This is performed using the [circleci-artifacts-redirector-action workflow](https://github.com/larsoner/circleci-artifacts-redirector-action).
- Via CircleCI: Go to the CircleCI job and select the "Artifacts" tab. Click on "index.html" to preview the built book.
- Via GitHub Actions alone: GitHub Actions also saves the built html files for preview, but you have to download and unzip the files to your local computer. Go to your deploy-book build in the [Actions tab](https://github.com/pyOpenSci/contributing-guide/actions). Then select "book-html" in the "Artifacts" pane near the bottom of the page. After downloading, unzip the book-html.zip file into a separate directory and open "index.html" from the directory with the unzipped files. The book should open in your web browser.

## How to build the guide locally

The pyOpenSci guidebook is written using [Jupyter Books](https://github.com/executablebooks/jupyter-book).

To build the guide locally, take the following steps:

* Clone this repository:

  ```
  git clone https://github.com/pyOpenSci/contributing-guide
  ```
* Install Jupyter Book

  ```
  pip install -U jupyter-book

  ```
* Build the guide

  ```
  # Cd to the repo if you are not already in it!
  $ cd contributing-guide
  # Build the book locally!
  $ jupyter-book build .
  ```

  To clean out old pages of your book:

  ```
  $ jupyter-book clean .
  ```

## Contributing to this guide

We welcome and issues and pull-requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/contributing-guide/issues/new/choose).
