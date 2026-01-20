# <img src="https://www.pyopensci.org/software-peer-review/_static/logo-dark-mode.png" width=200 /> pyOpenSci Peer Review Guide
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-47-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/peer-review-guide?color=purple&display_name=tag&style=plastic)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7641670.svg)](https://doi.org/10.5281/zenodo.7101777)
![deploy-book](https://github.com/pyOpenSci/peer-review-guide/actions/workflows/build-book.yml/badge.svg) [![CircleCI](https://circleci.com/gh/pyOpenSci/software-peer-review.svg?style=svg)](https://app.circleci.com/pipelines/github/pyOpenSci/software-peer-review)

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
      <td align="center" valign="top" width="16.66%"><a href="https://tomaugspurger.github.io"><img src="https://avatars.githubusercontent.com/u/1312546?v=4?s=100" width="100px;" alt="Tom Augspurger"/><br /><sub><b>Tom Augspurger</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=TomAugspurger" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3ATomAugspurger" title="Reviewed Pull Requests">👀</a> <a href="#design-TomAugspurger" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://arianesasso.me"><img src="https://avatars.githubusercontent.com/u/3659681?v=4?s=100" width="100px;" alt="Ariane Sasso"/><br /><sub><b>Ariane Sasso</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=arianesasso" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aarianesasso" title="Reviewed Pull Requests">👀</a> <a href="#design-arianesasso" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/rabernat"><img src="https://avatars.githubusercontent.com/u/1197350?v=4?s=100" width="100px;" alt="Ryan Abernathey"/><br /><sub><b>Ryan Abernathey</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=rabernat" title="Code">💻</a> <a href="#design-rabernat" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Arabernat" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://nicholdav.info/"><img src="https://avatars.githubusercontent.com/u/11934090?v=4?s=100" width="100px;" alt="David Nicholson"/><br /><sub><b>David Nicholson</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=NickleDave" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3ANickleDave" title="Reviewed Pull Requests">👀</a> <a href="#design-NickleDave" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://mentat.za.net"><img src="https://avatars.githubusercontent.com/u/45071?v=4?s=100" width="100px;" alt="Stefan van der Walt"/><br /><sub><b>Stefan van der Walt</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=stefanv" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Astefanv" title="Reviewed Pull Requests">👀</a> <a href="#design-stefanv" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://fosstodon.org/@eriknw"><img src="https://avatars.githubusercontent.com/u/2058401?v=4?s=100" width="100px;" alt="Erik Welch"/><br /><sub><b>Erik Welch</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=eriknw" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aeriknw" title="Reviewed Pull Requests">👀</a> <a href="#design-eriknw" title="Design">🎨</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="http://batalex.github.io"><img src="https://avatars.githubusercontent.com/u/11004857?v=4?s=100" width="100px;" alt="Alex Batisse"/><br /><sub><b>Alex Batisse</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=batalex" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Abatalex" title="Reviewed Pull Requests">👀</a> <a href="#design-batalex" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://orcid.org/0000-0003-2843-6044"><img src="https://avatars.githubusercontent.com/u/1662261?v=4?s=100" width="100px;" alt="Chiara Marmo"/><br /><sub><b>Chiara Marmo</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=cmarmo" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Acmarmo" title="Reviewed Pull Requests">👀</a> <a href="#design-cmarmo" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/yuvipanda"><img src="https://avatars.githubusercontent.com/u/30430?v=4?s=100" width="100px;" alt="Yuvi Panda"/><br /><sub><b>Yuvi Panda</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=yuvipanda" title="Code">💻</a> <a href="#design-yuvipanda" title="Design">🎨</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ayuvipanda" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://cosmicbboy.github.io/"><img src="https://avatars.githubusercontent.com/u/2816689?v=4?s=100" width="100px;" alt="Niels Bantilan"/><br /><sub><b>Niels Bantilan</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=cosmicBboy" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AcosmicBboy" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://hachyderm.io/web/@willingc"><img src="https://avatars.githubusercontent.com/u/2680980?v=4?s=100" width="100px;" alt="Carol Willing"/><br /><sub><b>Carol Willing</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Awillingc" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=willingc" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://chrisholdgraf.com"><img src="https://avatars.githubusercontent.com/u/1839645?v=4?s=100" width="100px;" alt="Chris Holdgraf"/><br /><sub><b>Chris Holdgraf</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Acholdgraf" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=choldgraf" title="Code">💻</a> <a href="#design-choldgraf" title="Design">🎨</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://www.gawbul.io"><img src="https://avatars.githubusercontent.com/u/321291?v=4?s=100" width="100px;" alt="Steve Moss"/><br /><sub><b>Steve Moss</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Agawbul" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=gawbul" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/xmnlab"><img src="https://avatars.githubusercontent.com/u/5209757?v=4?s=100" width="100px;" alt="Ivan Ogasawara"/><br /><sub><b>Ivan Ogasawara</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Axmnlab" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=xmnlab" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/kysolvik"><img src="https://avatars.githubusercontent.com/u/24379590?v=4?s=100" width="100px;" alt="Kylen Solvik"/><br /><sub><b>Kylen Solvik</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Akysolvik" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=kysolvik" title="Code">💻</a> <a href="#design-kysolvik" title="Design">🎨</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://matthew.dynevor.org"><img src="https://avatars.githubusercontent.com/u/67612?v=4?s=100" width="100px;" alt="Matthew Brett"/><br /><sub><b>Matthew Brett</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Amatthew-brett" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=matthew-brett" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://zehuachen.com"><img src="https://avatars.githubusercontent.com/u/6276623?v=4?s=100" width="100px;" alt="Zehua Chen"/><br /><sub><b>Zehua Chen</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AReventonC" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=ReventonC" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/sumit-158"><img src="https://avatars.githubusercontent.com/u/96618001?v=4?s=100" width="100px;" alt="Sumit Kashyap"/><br /><sub><b>Sumit Kashyap</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=sumit-158" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Asumit-158" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/consideRatio"><img src="https://avatars.githubusercontent.com/u/3837114?v=4?s=100" width="100px;" alt="Erik Sundell"/><br /><sub><b>Erik Sundell</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AconsideRatio" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=consideRatio" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://mbjoseph.github.io"><img src="https://avatars.githubusercontent.com/u/2664564?v=4?s=100" width="100px;" alt="Max Joseph"/><br /><sub><b>Max Joseph</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ambjoseph" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=mbjoseph" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://arokem.org"><img src="https://avatars.githubusercontent.com/u/118582?v=4?s=100" width="100px;" alt="Ariel Rokem"/><br /><sub><b>Ariel Rokem</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aarokem" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=arokem" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://jamespaulmason.com"><img src="https://avatars.githubusercontent.com/u/947614?v=4?s=100" width="100px;" alt="James Mason"/><br /><sub><b>James Mason</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ajmason86" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=jmason86" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/astrojuanlu"><img src="https://avatars.githubusercontent.com/u/316517?v=4?s=100" width="100px;" alt="Juan Luis Cano Rodríguez"/><br /><sub><b>Juan Luis Cano Rodríguez</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=astrojuanlu" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aastrojuanlu" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://forgottenprogramme.github.io/"><img src="https://avatars.githubusercontent.com/u/65779580?v=4?s=100" width="100px;" alt="Mahe Iram Khan"/><br /><sub><b>Mahe Iram Khan</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=ForgottenProgramme" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AForgottenProgramme" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/chiinita"><img src="https://avatars.githubusercontent.com/u/17188345?v=4?s=100" width="100px;" alt="Qin"/><br /><sub><b>Qin</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=chiinita" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Achiinita" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.davidstansby.com"><img src="https://avatars.githubusercontent.com/u/6197628?v=4?s=100" width="100px;" alt="David Stansby"/><br /><sub><b>David Stansby</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=dstansby" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Adstansby" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://www.linkedin.com/in/pllim/"><img src="https://avatars.githubusercontent.com/u/2090236?v=4?s=100" width="100px;" alt="P. L. Lim"/><br /><sub><b>P. L. Lim</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=pllim" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Apllim" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://orcid.org/0000-0001-6628-8033"><img src="https://avatars.githubusercontent.com/u/8931994?v=4?s=100" width="100px;" alt="Nick Murphy"/><br /><sub><b>Nick Murphy</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=namurphy" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Anamurphy" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://space.mit.edu/home/guenther/"><img src="https://avatars.githubusercontent.com/u/498688?v=4?s=100" width="100px;" alt="Hans Moritz Günther"/><br /><sub><b>Hans Moritz Günther</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=hamogu" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ahamogu" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/g-patlewicz"><img src="https://avatars.githubusercontent.com/u/52672925?v=4?s=100" width="100px;" alt="g-patlewicz"/><br /><sub><b>g-patlewicz</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=g-patlewicz" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ag-patlewicz" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/yang-ruoxi"><img src="https://avatars.githubusercontent.com/u/13646711?v=4?s=100" width="100px;" alt="ruoxi"/><br /><sub><b>ruoxi</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=yang-ruoxi" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ayang-ruoxi" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://grst.github.io"><img src="https://avatars.githubusercontent.com/u/7051479?v=4?s=100" width="100px;" alt="Gregor Sturm"/><br /><sub><b>Gregor Sturm</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=grst" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Agrst" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://about.me/sean.c.kelly"><img src="https://avatars.githubusercontent.com/u/814813?v=4?s=100" width="100px;" alt="Sean Kelly"/><br /><sub><b>Sean Kelly</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=nutjob4life" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Anutjob4life" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/kierisi"><img src="https://avatars.githubusercontent.com/u/23085445?v=4?s=100" width="100px;" alt="Jesse Mostipak"/><br /><sub><b>Jesse Mostipak</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=kierisi" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Akierisi" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/megies"><img src="https://avatars.githubusercontent.com/u/1842780?v=4?s=100" width="100px;" alt="Tobias Megies"/><br /><sub><b>Tobias Megies</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=megies" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Amegies" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://ivory.idyll.org/blog/"><img src="https://avatars.githubusercontent.com/u/51016?v=4?s=100" width="100px;" alt="C. Titus Brown"/><br /><sub><b>C. Titus Brown</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=ctb" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Actb" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="http://banesullivan.com"><img src="https://avatars.githubusercontent.com/u/22067021?v=4?s=100" width="100px;" alt="Bane Sullivan"/><br /><sub><b>Bane Sullivan</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=banesullivan" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Abanesullivan" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/ab93"><img src="https://avatars.githubusercontent.com/u/3485425?v=4?s=100" width="100px;" alt="Avik Basu"/><br /><sub><b>Avik Basu</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=ab93" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aab93" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/crhea93"><img src="https://avatars.githubusercontent.com/u/34322936?v=4?s=100" width="100px;" alt="Carter Lee Rhea"/><br /><sub><b>Carter Lee Rhea</b></sub></a><br /><a href="#ideas-crhea93" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Acrhea93" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=crhea93" title="Code">💻</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://thecoatlessprofessor.com"><img src="https://avatars.githubusercontent.com/u/833642?v=4?s=100" width="100px;" alt="James J Balamuta"/><br /><sub><b>James J Balamuta</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=coatless" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Acoatless" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/jonas-eschle"><img src="https://avatars.githubusercontent.com/u/17454848?v=4?s=100" width="100px;" alt="Jonas Eschle"/><br /><sub><b>Jonas Eschle</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ajonas-eschle" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/InessaPawson"><img src="https://avatars.githubusercontent.com/u/43481325?v=4?s=100" width="100px;" alt="Inessa Pawson"/><br /><sub><b>Inessa Pawson</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=InessaPawson" title="Code">💻</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AInessaPawson" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://eliotwrobson.github.io/"><img src="https://avatars.githubusercontent.com/u/1345068?v=4?s=100" width="100px;" alt="Eliot Robson"/><br /><sub><b>Eliot Robson</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Aeliotwrobson" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/software-peer-review/commits?author=eliotwrobson" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://rgoswami.me"><img src="https://avatars.githubusercontent.com/u/4336207?v=4?s=100" width="100px;" alt="Rohit Goswami"/><br /><sub><b>Rohit Goswami</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=HaoZeke" title="Documentation">📖</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3AHaoZeke" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://jedbrown.org"><img src="https://avatars.githubusercontent.com/u/3303?v=4?s=100" width="100px;" alt="Jed Brown"/><br /><sub><b>Jed Brown</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=jedbrown" title="Documentation">📖</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ajedbrown" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="http://www.mapdatascience.com"><img src="https://avatars.githubusercontent.com/u/12127746?v=4?s=100" width="100px;" alt="Lauren Yee"/><br /><sub><b>Lauren Yee</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=yeelauren" title="Documentation">📖</a> <a href="https://github.com/pyOpenSci/software-peer-review/pulls?q=is%3Apr+reviewed-by%3Ayeelauren" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/eigenbrot"><img src="https://avatars.githubusercontent.com/u/2183757?v=4?s=100" width="100px;" alt="Arthur Eigenbrot"/><br /><sub><b>Arthur Eigenbrot</b></sub></a><br /><a href="https://github.com/pyOpenSci/software-peer-review/commits?author=eigenbrot" title="Documentation">📖</a> <a href="https://github.com/pyOpenSci/software-peer-review/issues?q=author%3Aeigenbrot" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
