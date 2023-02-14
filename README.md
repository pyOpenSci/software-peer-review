# <img src="images/logo/logo.png" width=40 /> pyOpenSci Peer Review Guide
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-10-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/peer-review-guide?color=purple&display_name=tag&style=plastic)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7101778.svg)](https://doi.org/10.5281/zenodo.7101778)
![deploy-book](https://github.com/pyOpenSci/peer-review-guide/actions/workflows/build-book.yml/badge.svg)  [![CircleCI Book Preview](https://circleci.com/gh/pyOpenSci/peer-review-guide.svg?style=svg)](https://circleci.com/gh/pyOpenSci/peer-review-guide)

https://www.pyopensci.org/peer-review-guide/

pyOpenSci's guide for developing, reviewing, and maintaining packages.


## Contributing to this guide

We welcome issues and pull requests to improve the content of this guide.
If you'd like to see an improvement, please [open an issue](https://github.com/pyOpenSci/peer-review-guide/issues/).

To submit a Pull Request with changes:
1. Create a fork of this repo to make changes.
2. After making changes, build the book locally from your fork to preview the changes to make sure they appear as expected (see [How to build the guide locally](https://github.com/pyopensci/peer-review-guide/#how-to-build-the-guide-locally) below)
3. When satisfied, push the changes back to GitHub and open a pull request from your fork to the main branch of this repo.
4. The Continuous Integration processes will build the book and let you and the PR reviewer(s) preview it in your browser (see [Automated build and publishing](https://github.com/pyopensci/peer-review-guide/#automated-build-and-publishing) below).
5. The reviewer of the PR may request modifications.
6. Once satisfied, the reviewer will merge your pull request! Thanks for your contribution!

## How to build the guide locally

The pyOpenSci guidebook is written using [Jupyter Book](https://github.com/executablebooks/jupyter-book).

To build the guide locally, take the following steps:

* Clone this repository (or clone your fork by replacing "pyOpenSci" with your GitHub username):

  ```
  git clone https://github.com/pyOpenSci/peer-review-guide
  ```

To build, follow these steps:

1. Install `nox`

```console
pip install nox
```
2. Build the documentation:

```console
nox -s docs
```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs-live
```

* To view your built book:

Navigate to _build/html/ on your local clone of the repo and open "index.html".


## Automated build and publishing

Whenever a pull request is opened or changes are pushed to any branch of the base repository, the book is built (separately) by both GitHub Actions and CircleCI.

### Why both GitHub Actions and CircleCI?

- GitHub Actions is the main build tool. In addition to building whenever a pull request is opened from a fork, it handles publishing the book when changes are made to the main branch (e.g. once the pull request is merged). When that happens, it pushes the built html files to the gh-pages branch, which publishes the book to the [website](https://pyopensci.org/peer-review-guide/).
- CircleCI's build is redundant, but it offers an easier way of viewing the built html in browser WITHOUT merging the changes to main or downloading files. See [How do you preview the the guide from a Pull Request](https://github.com/pyopensci/peer-review-guide/#how-do-you-preview-the-guide-from-a-pull-request) below for details.

### How do you preview the guide from a Pull Request?
- *(Recommended)* Via the artifact redirector workflow: When viewing the checks in a pull request, click "Details" next to the "Click to preview rendered book" to be automatically taken to the CircleCI index.html preview. This is performed using the [circleci-artifacts-redirector-action workflow](https://github.com/larsoner/circleci-artifacts-redirector-action). See the gif below for a demonstration.
- Via CircleCI: Go to the CircleCI job and select the "Artifacts" tab. Click on "index.html" to preview the built book.
- Via GitHub Actions alone: GitHub Actions also saves the built html files for preview, but you have to download and unzip the files to your local computer. Go to your deploy-book build in the [Actions tab](https://github.com/pyOpenSci/peer-review-guide/actions). Then select "book-html" in the "Artifacts" pane near the bottom of the page. After downloading, unzip the book-html.zip file into a separate directory and open "index.html" from the directory with the unzipped files. The book should open in your web browser.

![preview_book2](https://user-images.githubusercontent.com/24379590/196472186-ef2c8602-893f-4465-b551-cbecd53cafd9.gif)


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://tomaugspurger.github.io"><img src="https://avatars.githubusercontent.com/u/1312546?v=4?s=100" width="100px;" alt="Tom Augspurger"/><br /><sub><b>Tom Augspurger</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=TomAugspurger" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3ATomAugspurger" title="Reviewed Pull Requests">👀</a> <a href="#design-TomAugspurger" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://arianesasso.me"><img src="https://avatars.githubusercontent.com/u/3659681?v=4?s=100" width="100px;" alt="Ariane Sasso"/><br /><sub><b>Ariane Sasso</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=arianesasso" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aarianesasso" title="Reviewed Pull Requests">👀</a> <a href="#design-arianesasso" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rabernat"><img src="https://avatars.githubusercontent.com/u/1197350?v=4?s=100" width="100px;" alt="Ryan Abernathey"/><br /><sub><b>Ryan Abernathey</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=rabernat" title="Code">💻</a> <a href="#design-rabernat" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Arabernat" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://nicholdav.info/"><img src="https://avatars.githubusercontent.com/u/11934090?v=4?s=100" width="100px;" alt="David Nicholson"/><br /><sub><b>David Nicholson</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=NickleDave" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3ANickleDave" title="Reviewed Pull Requests">👀</a> <a href="#design-NickleDave" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mentat.za.net"><img src="https://avatars.githubusercontent.com/u/45071?v=4?s=100" width="100px;" alt="Stefan van der Walt"/><br /><sub><b>Stefan van der Walt</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=stefanv" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Astefanv" title="Reviewed Pull Requests">👀</a> <a href="#design-stefanv" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://fosstodon.org/@eriknw"><img src="https://avatars.githubusercontent.com/u/2058401?v=4?s=100" width="100px;" alt="Erik Welch"/><br /><sub><b>Erik Welch</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=eriknw" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aeriknw" title="Reviewed Pull Requests">👀</a> <a href="#design-eriknw" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://batalex.github.io"><img src="https://avatars.githubusercontent.com/u/11004857?v=4?s=100" width="100px;" alt="Alex Batisse"/><br /><sub><b>Alex Batisse</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=batalex" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Abatalex" title="Reviewed Pull Requests">👀</a> <a href="#design-batalex" title="Design">🎨</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://orcid.org/0000-0003-2843-6044"><img src="https://avatars.githubusercontent.com/u/1662261?v=4?s=100" width="100px;" alt="Chiara Marmo"/><br /><sub><b>Chiara Marmo</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=cmarmo" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Acmarmo" title="Reviewed Pull Requests">👀</a> <a href="#design-cmarmo" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yuvipanda"><img src="https://avatars.githubusercontent.com/u/30430?v=4?s=100" width="100px;" alt="Yuvi Panda"/><br /><sub><b>Yuvi Panda</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=yuvipanda" title="Code">💻</a> <a href="#design-yuvipanda" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ayuvipanda" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://cosmicbboy.github.io/"><img src="https://avatars.githubusercontent.com/u/2816689?v=4?s=100" width="100px;" alt="Niels Bantilan"/><br /><sub><b>Niels Bantilan</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AcosmicBboy" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=cosmicBboy" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
