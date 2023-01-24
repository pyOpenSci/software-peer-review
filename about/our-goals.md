# pyOpenSci Software Peer Review Goals

Python is a flexible programming language that is used across numerous
disciplines and domains. Python is so flexible that it is
one of the few languages that can be used to wrap around other languages.

If you are building a pure Python package, your setup can be simple.
However, some scientific packages have complex
requirements as they may need to support extensions or tools written
in other languages such as C or C++.

To support the many uses of Python, there are many ways
to create a Python package.

```{admonition} Python supports extensions written in other languages
:class: info

The spatial data too stack is a common example of tools that
often have complex packaging requirements given they often need to use
tools like GDAL to support spatial operations.
```

## What makes Python unique and valuable can also make packaging complex
The diversity of packaging options can be confusing, particularly
if you are new to Python. However, we are working on a [Python packaging guide](https://www.pyopensci.org/python-package-guide)
that will make the packaging landscape easier to navigate.


## Working towards standardized packaging practices in the Scientific Python community

While there is no single solution to the diverse needs of developers in the
Python scientific community, pyOpenSci strives to encourage a standard approach
to packaging through it's tutorials, documentation and guides and peer review process. We do this by:

1. Following and encouraging best practices for Python packaging that follow modern Python Enhancement Protocols (PEPs). PEPs are standards written for the broader Python community to follow.
1. Reinforcing best practices accepted by the scientific community. This community most often develops packages that are not pure Python. Thus, the scientific community has additional layers of complexity in their tool builds that we need to consider.
1. Enforcing documentation best practices in our reviews that support both usability and accessibility. Great documentation is critical for a package to gain more users from varying backgrounds.

As such pyOpenSci embraces community driven standards created by organizations
such as [Scientific Python](https://scientific-python.org/).

We also strive to help maintainers use similar infrastructure for
their packages. In the long term, consistent infrastructure
and packaging approaches will:

* Make it easier for those who are new to packaging to get started (and in turn push open science forward)
* Make it easier for new contributors to participate given similar infrastructure setup across the ecosystem.

As it makes sense, we recommend (but do not require) packaging
approaches implemented by existing packages in the scientific Python
ecosystem.



## Specific pyOpenSci goals
In addition to the broader goals laid out above, below are our specific goals for open peer review of Python packages.

### 1. A catalog of vetted, maintained tools
We hope that scientists will look to [our online catalog of
maintained and vetted tools](https://www.pyopensci.org/python-packages.html) to help them find tools that they can
depend on. Over time as our catalog grows, this will reduce the
need for searching and sorting through the many packages in various
states of maintenance on PyPI.

Through our peer review, we also help maintainer get the word out
about their packages through our website, blog and social media
presence. Currently, the most popular content on our website are
the [blogs that maintainers have written about their tools](https://www.pyopensci.org/blog/movingpandas-movement-data-analysis).

### 2. Improved package usability through documentation

Clear and useful documentation makes it easier for scientists to use your tools.
During our reviews, we look carefully at:
* documentation,
* quick start tutorials and code examples to help users get started
* and code documentation (docstrings)

To ensure that the package is user friendly. If you need help with documentation,
We also have an entire section of our packaging guide devoted to documentation.

### 3. Reduce the number of packages with overlapping functionality

It's easy to find multiple packages on `PyPI` that perform that same tasks
(or overlapping tasks). When you submit a package to us, we ask that you know
about other packages in our system that may do similar things. This check will
help us connect maintainers who are working towards similar functionality goals.
It will also help us in the long term reduce the number of overlapping packages,
in various states of maintenance on `PyPI`.

In some cases just added information to your **README.md** about how your
package varies from others in the ecosystem is valuable to users.

* [See our discussion of package overlap for more](package-overlap)

### 4. Support long term maintenance of vetted tools

Most maintainers are not paid for their work and thus work on tools
in their free time. So what happens when a maintainer of a commonly used tool wants
to step down? We help maintainers find someone new to take over the reigns.
If that doesn't make sense we will help the maintainer gracefully sunset the
package.

One key element in this process is a clear development guide that outlines
the tools and workflows that you are using to build and maintain your package.

### 5. Support implementation of standards and best practices

Where possible we encourage and help maintainers to update and
enhance their package infrastructure. Examples of this are moving
package metadata from the `setup.py` file and into the modern
[`pyproject.toml` standard format](https://snarky.ca/what-the-heck-is-pyproject-toml/).

### 6. Build a community support system for maintainers

Many packages that are commonly used by scientists are being maintained by a single person. As devoted as this single maintainer
may be, it's always easier to work when you have community support.

Our online community both on [discourse](https://pyopensci.discourse.group/) and more privately on slack, is available for maintainers to interact with each other, ask questions and get support. Core to our
mission is building a welcoming and diverse community for people
of both varying technical background and skills and varying cultural background to belong to.
