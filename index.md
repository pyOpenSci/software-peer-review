# Welcome to The pyOpenSci Community Guidebook!


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

<!-- 
Removing button for the time being
```{button-ref} start/your-first-book
:ref-type: doc
:color: primary
:class: sd-rounded-pill float-left


Get Involved (Maybe a link to a get involved page)
``` -->

% The SVG rendering breaks latex builds for the GitHub badge, so only include in HTML
```{only} html
![GitHub release (latest by date)](https://img.shields.io/github/v/release/pyopensci/contributing-guide?color=purple&display_name=tag&style=plastic)
[![](https://img.shields.io/github/stars/pyopensci/contributing-guide?style=social)](https://github.com/pyopensci/contributing-guide)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7101778.svg)](https://doi.org/10.5281/zenodo.7101778)
```

:::

::::
<!-- I think this is the end of the header - below begins the next grid-->

::::{grid} 1 1 1 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: open-source-software-peer-review/aims-and-scope
:link-type: doc
:class-header: bg-light

Open Peer Review ✏️
^^^
Get a basic overview of our open peer review process for Python open source
software.
:::

:::{grid-item-card}
:link: open-source-software-submissions/reviewer-guide
:link-type: doc
:class-header: bg-light

Are you a package author / maintainer? ✨
^^^

Learn how to submit a package for peer review with pyOpenSci.
:::

:::{grid-item-card}
:link: open-source-software-submissions/editors-guide
:link-type: doc
:class-header: bg-light

Are you an Editor? ✨
^^^

This guide will walk you through the editorial process.
:::

:::{grid-item-card}
:link: open-source-software-submissions/reviewer-guide
:link-type: doc
:class-header: bg-light

Are you a reviewer? ✨
^^^

Click here to read our reviewer guide which will walk you through the review
process step-by-step.
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
[Code of Conduct](open-source-software-peer-review/code-of-conduct). The 
[Aims and Scope](open-source-software-peer-review/aims-and-scope) section 
lays out what types of packages we review.



## Build out the toctree hidden

```{toctree}
:hidden:
:caption: About peer review

open-source-software-peer-review/intro  
open-source-software-peer-review/aims-and-scope
open-source-software-peer-review/policies-guidelines
open-source-software-peer-review/code-of-conduct

```

```{toctree}
:hidden:
:caption: Peer Review Guides

open-source-software-submissions/intro
open-source-software-submissions/author-guide
open-source-software-submissions/reviewer-guide
open-source-software-submissions/editors-guide
open-source-software-submissions/editor-in-chief-guide
open-source-software-submissions/onboarding-guide
:title: title here
```

```{toctree}
:hidden:
:caption: Authoring information

authoring/index
authoring/overview
authoring/collaboration
authoring/tools-for-developers 
authoring/testing 
authoring/release

```
