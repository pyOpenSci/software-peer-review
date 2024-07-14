# About the pyOpenSci software peer review process

```{toctree}
:hidden:
:caption: About peer review

Intro <self>
Our Goals </about/our-goals>
Benefits for Package Authors </about/benefits>
Package Scope (What we review) </about/package-scope>
Why Open Review Matters </about/why-open-review>

```

```{toctree}
:hidden:
:caption: Our Process

How Review Works <../our-process/how-review-works>
Review Timeline <../our-process/review-timeline>
Peer Review Policies <../our-process/policies>
Code of Conduct <../code-of-conduct>
```

```{toctree}
:hidden:
:caption: Appendices

Changelog <../changelog>
Glossary <../appendices/glossary>
Templates <../appendices/templates>
Contributing <../CONTRIBUTING>
```

## Community-driven software peer review

pyOpenSci leads an open, volunteer-based review process for scientific Python
open source software. Our review process focuses on:

- Code quality and style,
- Documentation quality,
- Package usability,
- Test coverage that supports the maintenance of code function. Test coverage also makes it easier for contributors to understand how their contributions impact other parts of the code,
- Evaluation of infrastructure such as continuous integration that runs test suites and code format checks on pull requests. This infrastructure supports software quality and reliability. It also makes it easier for contributors to submit changes to the code base and know that those changes aren't breaking other parts of the code.

The overarching goal of this review process is to improve the quality,
consistency and usability of scientific software tools over time. Further, we
ensure that packages in our ecosystem are continuously maintained. Over time
knowing that a tool is both vetted and maintained builds trust with tool users in the community.

## Peer review is needed in the scientific community

Software peer review supports scientists receiving credit for putting in the
effort of making tools that scientists need to propel open science forward.
Software peer review provides credit for the community investment that
developers make in creating and maintaining scientific software in the same way
that paper review recognizes scientific findings.

### Peer review also addresses issues specific to the Python ecosystem

The pyOpenSci peer review program also addresses several issues
that are specific to the scientific Python ecosystem:

1. The struggle for scientists to select the right tool to use for their workflow given that there are often multiple packages with overlapping functionality and varying levels of maintenance. [See this example of the many packages that interface with Twitter on `PyPI`](https://pypi.org/search/?q=twitter)
1. Packages that are not documented enough to support:
   - Contributions from others
   - Directions on how to get started using the package functionality (quick start vignettes or tutorials)
1. Packages using varying types of packaging and documentation approaches making it more difficult to contribute.
1. Packages that are well-maintained and used but then maintenance comes to a halt when the maintainer needs to step down (burn-out is common and understandable).
1. Packages that are missing proper licensing and citation information.

Further, pyOpenSci addresses the issue of software maintenance.
It addresses the question:

> What happens to a tool that the community is using when the maintainer needs to step down

In these cases pyOpenSci will help find a new maintainer(s) for that tool. If
that is not possible, we will help sunset the package in a way that allows
users to gracefully update their workflows rather than be caught by
surprise when a new bug arises.

### Peer review of open source software helps maintain consistent quality

Peer review of python tools that support science is critical to enforcing
quality and usability standards. All pyOpenSci packages contributed by the
community undergo a transparent, constructive, non adversarial and open peer
review process. The goal of that process is to enforce commonly accepted standards.
These standards include technical structure of the package, usability of the
package, documenting package functionality in a way that is accessible
to all levels of users as well as proper licensing and citation information.

### Why is pyOpenSci focused on the Python programming language?

Python is a general programming language used across many different applications
that extend well beyond science. Furthermore, the Python package landscape is
highly dynamic and constantly evolving to support many different types of
users and developers.

As such there is a huge amount of variation
in the scientific Python ecosystem in terms of how tools are built, supported
and documented. This variation can be hard for software users (data scientists for example) to find the right tool to use for their workflow.

We aspire to help scientists find the high quality, documented and
maintained tools that they need to do their science. We also support
developers in maintaining their tools and receiving credit for their work.

Our _peer review_ badge
and catalog of tools will help scientists find the tools that they need. Our
diverse and welcoming community will support maintainers as they maintain their tools. Advocating for citation of software will also help maintainers
receive academic credit for their work.

```{note}
[This blog post](https://www.numfocus.org/blog/how-ropensci-uses-code-review-to-promote-reproducible-science/) written by editors from our partner organization, rOpenSci, is a good introduction to the pyOpenSci software peer review process.
```

### How do I know that a Python package has been reviewed by pyOpenSci?

You can identify pyOpenSci packages that have been peer-reviewed by the green
"peer-reviewed" badge at the top of their `README.md` file.

:::{figure-md} pyos-badge
:class: myclass

<img src="https://pyopensci.org/badges/peer-reviewed.svg" alt="The pyOpenSci Peer Reviewed badge" class="bg-primary mb-1" width="200px">

pyOpenSci Peer Review Badge
:::

This badge is added by the package author after the package
has successfully completed review and ideally links to the specific GitHub issue
where the tool was reviewed. [See this example from devicely, one of our accepted pyOpenSci ecosystem packages](https://github.com/hpi-dhc/devicely).


### Partnership with JOSS

pyOpenSci collaborates with organizations that support the scientific community, for example, Journal of Open Source Software (JOSS).
We are not a publisher, but rather a community that supports Python-specific packages. You don't have to choose between JOSS and us since we are complementary. See details [here](https://www.pyopensci.org/software-peer-review/partners/pangeo.html).
