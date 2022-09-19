# <img src="images/logo/logo.png" width=40 /> pyOpenSci Guidebook
[![CircleCI](https://circleci.com/gh/pyOpenSci/contributing-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/contributing-guide)

https://pyopensci.org/contributing-guide/

pyOpenSci's guide for developing, reviewing, and maintaining packages.

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
