# Welcome to the pyOpenSci Software Peer Review Guidebook!

::::{grid} 2
:reverse:

:::{grid-item}
:columns: 4
:class: sd-m-auto
:::  

:::{grid-item}
:columns: 8
:class: sd-fs-3
pyOpenSci is a diverse community that supports the open Python tools that 
drive open science.

% The SVG rendering breaks latex builds for the GitHub badge, so only include in HTML
```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/contributing-guide?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/contributing-guide?style=social)](https://github.com/pyopensci/contributing-guide)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7101778.svg)](https://doi.org/10.5281/zenodo.7101778)
```
:::

::::
<!-- I think this is the end of the header - below begins the next grid-->

::::{grid} 1 1 1 2
:class-container: text-center
:gutter: 3

:::{grid-item-card} {octicon}`book;1.5em;sd-mr-1` Learn About Open Peer Review ✏️
:link: about-peer-review/intro
:link-type: doc
:class-header: bg-light

Get a basic overview of our open peer review process for Python scientific open source
software.
+++
[Click to learn more »](about-peer-review/aims-and-scope)
:::

:::{grid-item-card} {octicon}`code-square;1.5em;sd-mr-1`For Maintainers
:link: software-peer-review-guide/author-guide
:link-type: doc
:class-header: bg-light

Are you a package author / maintainer? ✨

Learn how to submit a package for peer review with pyOpenSci.
+++
[Click to learn more »](software-peer-review-guide/author-guide)
:::

:::{grid-item-card} {octicon}`pencil;1.5em;sd-mr-1`For Editors
:link: software-peer-review-guide/editors-guide
:link-type: doc
:class-header: bg-light

 ✨ Our editor guide will walk you through the editorial process. ✨ 
+++
[Click to learn more »](software-peer-review-guide/editors-guide)
:::

:::{grid-item-card} {octicon}`codescan-checkmark;1.5em;sd-mr-1` For Reviewers
:link: software-peer-review-guide/reviewer-guide
:link-type: doc
:class-header: bg-light

Are you a reviewer? ✨

Click here to read our reviewer guide which will walk you through the review
process step-by-step.
+++
[Click to learn more »](software-peer-review-guide/editors-guide)
:::

::::


## Why pyOpenSci?
pyOpenSci promotes open and reproducible research through peer-review of 
scientific Python packages. We also build technical capacity by providing a 
curated repository of high-quality packages and enabling scientists to write 
and share their own software. We hope to foster a greater sense of community 
among scientific Python users so that we can help each other become better 
programmers and researchers.

## This Guide
This guidebook contains information for pyOpenSci package authors, reviewers, 
and editors. It is organized into three sections:

### 1. Before Review - Packaging Guide
Contains our guidelines for creating and testing scientific python packages. 
Before submitting a package for review, check to be sure that your software 
meets the basic [requirements](authoring/overview#overview). The section also 
contains recommendations and best practices that might be helpful as you are 
writing and preparing your package.

### 2. Peer Review Process
Outlines the pyOpenSci peer review process. This includes guidelines for 
submitting and reviewing packages, as well as our 

[Code of Conduct](about-peer-review/code-of-conduct). The 
[Aims and Scope](about-peer-review/aims-and-scope) section 
lays out what types of packages we review.


```{toctree}
:hidden:
:caption: About peer review

About Peer Review  <about-peer-review/intro>
Peer Review Benefits <about-peer-review/review-benefits>
How peer review works <about-peer-review/how-peer-review-works.md>
Aims & Scope <about-peer-review/aims-and-scope>
pyOpenSci, JOSS & rOpenSci <about-peer-review/pyopensci-related-joss-ropensci>
Peer review policies <about-peer-review/policies-guidelines>
Code of Conduct <about-peer-review/code-of-conduct>
```

```{toctree}
:hidden:
:caption: Peer Review Guides

Peer review process overview <software-peer-review-guide/intro>
Author Guide <software-peer-review-guide/author-guide>
Reviewer Guide <software-peer-review-guide/reviewer-guide>
Editor Guide <software-peer-review-guide/editors-guide>
Editor in Chief Guide <software-peer-review-guide/editor-in-chief-guide>
Onboarding Guide <software-peer-review-guide/onboarding-guide>
```

```{toctree}
:hidden:
:caption: Appendices

Glossary <appendices/glossary>
Templates <appendices/templates>
```


