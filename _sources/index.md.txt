# Welcome to the pyOpenSci Software Peer Review Guidebook!

::::{grid} 2
:reverse:

:::{grid-item}
:columns: 4
:class: sd-m-auto
:::  

:::{grid-item}
:columns: 12
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
:link: about/intro
:link-type: doc
:class-header: bg-light

Get a basic overview of our open peer review process for Python scientific open source
software.
+++
[Click to learn more »](about/intro)
:::

:::{grid-item-card} {octicon}`code-square;1.5em;sd-mr-1`For Maintainers
:link: how-to/author-guide
:link-type: doc
:class-header: bg-light

Are you a package author / maintainer? ✨

Learn how to submit a package for peer review with pyOpenSci.
+++
[Click to learn more »](how-to/author-guide)
:::

:::{grid-item-card} {octicon}`pencil;1.5em;sd-mr-1`For Editors
:link: how-to/editors-guide
:link-type: doc
:class-header: bg-light

 ✨ Our editor guide will walk you through the editorial process. ✨ 
+++
[Click to learn more »](how-to/editors-guide)
:::

:::{grid-item-card} {octicon}`codescan-checkmark;1.5em;sd-mr-1` For Reviewers
:link: how-to/reviewer-guide
:link-type: doc
:class-header: bg-light

Are you a reviewer? ✨

Click here to read our reviewer guide which will walk you through the review
process step-by-step.
+++
[Click to learn more »](how-to/editors-guide)
:::

::::


## Why pyOpenSci?
pyOpenSci promotes open and reproducible research through peer-review of 
scientific Python packages. We also build technical capacity by providing a 
curated repository of high-quality packages and enabling scientists to write 
and share their own software. We hope to foster a greater sense of community 
among scientific Python users so that we can help each other become better 
programmers and researchers.

:::{figure-md} pyos-badge-home
:class: myclass

<img src="https://tinyurl.com/y22nb8up" alt="The pyOpenSci badge- On the left is the badge in grey and it says pyOpenSci. On the right it is bright green and says Peer Reviewed." class="bg-primary mb-1" width="200px">

**pyOpenSci Peer Review Badge will appear on the README.md file of packages that have been 
reviewed and vetted by us.**
:::

## This Guide
This guidebook contains information for pyOpenSci package authors, reviewers, 
and editors. It is organized into three sections:

### 1. About Peer Review
This section provides a broad overview of our peer review process. 


### 2. Our Partners
This section discusses our partnerships with other scientific and open source 
communities including Pangeo and JOSS. 

### 3. How To Guides
This section provides specific guides for each role in our peer review process. 


```{toctree}
:hidden:

🏠 Home <self>
```

```{toctree}
:hidden:
:caption: About peer review

ABOUT </about/intro>
Our Goals </about/our-goals>
Benefits for Package Authors </about/benefits>
Package Scope (What we review) </about/package-scope>
OUR PROCESS </our-process/how-review-works>
```


```{toctree}
:hidden:
:caption: Partners

Scientific Communities <partners/scientific-communities>
JOSS <partners/joss>
```

```{toctree}
:hidden:
:caption: How To Guides

Author Guide <how-to/author-guide>
Reviewer Guide <how-to/reviewer-guide>
Editor Guide <how-to/editors-guide>
Editor in Chief Guide <how-to/editor-in-chief-guide>
Onboarding Editors & Reviewers <how-to/onboarding-guide>
Finding Reviewers <how-to/finding-reviewers>
```

```{toctree}
:hidden:
:caption: Appendices

Glossary <appendices/glossary>
Templates <appendices/templates>
```


