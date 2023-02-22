# The Scope of  Packages that pyOpenSci Reviews

## What types of packages does pyOpenSci review?
pyOpenSci reviews higher level software packages that support scientific workflows.

:::{figure-md} fig-target

<img src="../images/python-stack-jupyter-earth.png" alt="Image showing the tiers of software in the python ecosystem starting with Python itself and as you move out packages become more domain specific. In this image packages like xarray and numpy are considered core to scientific python. Packages and distributions like astropy, simpeg and metpy are considered to be domain specific." width="700px">

Diagram showing the tiers of software in the python ecosystem starting with Python itself and as you move out packages become more domain specific. In this image packages like xarray and numpy are considered core to scientific python. Packages and distributions like astropy, simpeg and metpy are considered to be domain specific. pyOpenSci's review
process focuses on domain specific packages rather than core packages as
these packages tend to have more variability in long term maintenance and
package infrastructure and quality compared to established core packages. **Source: ["Jupyter meets earth" project](https://jupytearth.org/jupyter-resources/introduction/ecosystem.html)**
:::


Currently, the packages that pyOpenSci reviews also need to fall into the
technical and applied scope of our organization. This scope may expand over time
as the organization grows.

## Is Your Package in Scope For pyOpenSci Review?

pyOpenSci reviews packages that fall within a list of specified categories and
domains. Packages must also meet our technical scope requirements.

If you are unsure whether your package is in scope for review, please
open a [pre-submission inquiry using a GitHub Issue](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=) to get feedback from
one of our editors. We are happy to look at your package and help you understand
whether it is in scope or not.

### About the types of packages that we review

pyOpenSci reviews packages that support open reproducible science,
data processing and and the various stages of managing the
data lifecycle. Packages submitted to pyOpenSci should fit into one or
more of the categories below and should be within our technical scope.

```{admonition} Your Package Does Not Need to Be In Widespread Use Yet to be Reviewed
:class: important

We review packages with the goal of improving package quality and usability for scientists.
As such, we review packages across a spectrum of small to large user bases. The popularity of your package is not a consideration in our review process!

When we evaluate whether you package is within our scope, we only consider:

1. how the package is developed and
2. how the package relates to and supports the broader scientific ecosystem.

We welcome young packages that are just entering the scientific Python
ecosystem to apply for review if they are relevant to the science community and
fit into at least one scope category below. We also welcome mature packages with
a growing or established community!
```

If you are unsure whether your package fits into one of the general or
statistical categories, please open an issue as a [pre-submission inquiry](https://github.com/pyOpenSci/software-submission/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=).

```{note}
This is a living document. The categories below may change through time.
This may mean in some cases, some previously peer review-accepted packages
may not be in-scope today. We strive for consistency in our peer review process. However, we also evaluate packages on a case-by-case basis.
In some cases exceptions are made.
```

## Package categories

The following are the current categories that fall into scope for
pyOpenSci. In addition to fitting into one or more of these categories, your package should have some level of
demonstrated scientific application. This could be a use case that you can
link to or a tutorial that demonstrates its potential application for science.

Below we provide examples of packages from pyOpenSci ecosystem. Because we
have growing community of packages, in some cases we link to R packages
within the rOpenSci community that match the category scope for reference.

We will update this page as our review process evolves.

```{note}
Many of the example packages below perform tasks that might fit in multiple
categories. There examples are there to provide you with a flavor of the types
of packages that would fall into that category.
```

### Data retrieval
Packages for accessing and downloading data from online sources. This category
includes wrappers for accessing APIs.

Our definition of scientific applications is broad, including data storage
services, journals, and other remote servers, as many data sources may be of
interest to scientists. However, retrieval packages should be focused on data
sources / topics, rather than services. For example a general client for Amazon
Web Services data storage would not be in-scope.

* Examples: [OpenOmics](https://github.com/pyOpenSci/software-submission/issues/31), [pyDov](https://github.com/pyOpenSci/software-submission/issues/19), [Physcraper](https://github.com/pyOpenSci/software-review/issues/26)


### Data extraction

These packages aid in retrieving data from unstructured sources such as text,
images, and PDFs. They might also parse scientific data types and outputs from
scientific equipment.

* Examples: [devicely](https://github.com/pyOpenSci/software-submission/issues/37), [jointly](https://github.com/pyOpenSci/software-submission/issues/45)

### Data processing & munging

Data [munging tools transform data in a way that makes further analysis possible (as [defined on Wikipedia](https://en.wikipedia.org/wiki/Data_wrangling)). Munging complements the other categories so it's common for packages to include some functionality to munge data. This
category focuses on tools for handling data in specific formats that scientists
may be interested in working with. These data may also be generated from
scientific workflows or exported from instruments and wearables.

* Examples: [devicely](https://github.com/pyOpenSci/software-submission/issues/37), [jointly](https://github.com/pyOpenSci/software-submission/issues/45), [MovingPandas](https://github.com/pyOpenSci/software-submission/issues/18), [OpenOmics](https://github.com/pyOpenSci/software-submission/issues/31), [Physcraper](https://github.com/pyOpenSci/software-submission/issues/26)


### Data deposition

Tools for depositing data into scientific research repositories.

* Examples: [This is an example from rOpenSci - eml](https://github.com/ropensci/software-review/issues/80)

### Data validation and testing:

Tools that enable automated validation and checking of data quality and
completeness. These tools should be able to support scientific workflows.

* Example: [pandera](https://github.com/pyOpenSci/software-submission/issues/12)

### Scientific software wrappers

Scientific software wrappers refer to packages that provide a Python interface
for existing scientific packages written in other languages.

These packages should have a clear scientific application. Wrappers must provide
significant added value to the scientific ecosystem be it in data handling, or
improved installation processes for Python users.

We strongly encourage submissions that wrap tools that are open-source with
an OSI-approved license. Exceptions will be evaluated case-by-case,
considering whether open-source options exist.

* Examples: [PyGMT](https://github.com/pyOpenSci/software-submission/issues/43)

### Workflow automation & versioning
Tools that automate and link together workflows and as such support
reproducible workflows. These
tools may include build systems and tools to manage continuous integration.
This also includes tools that support version control.

* Examples: Both of these tools are not pyOpenSci reviewed as of yet but are examples of tools that might be in scope for this category - [snakemake](https://snakemake.readthedocs.io/en/stable/), [pyGitHub ](https://github.com/PyGithub/PyGithub)

### Citation management and bibliometrics:

Tools that facilitate managing references, such as for writing manuscripts,
creating CVs or otherwise attributing scientific contributions, or accessing,
manipulating or otherwise working with bibliometric data. (Example: [Example from rOpenSci - RefManageR](https://github.com/ropensci/software-review/issues/119))

### Data visualization & analysis
These are packages that enhance a scientists experience visualizing and
analyzing data.

* Examples: [PyGMT - (also spatial and data munging)](https://github.com/pyOpenSci/software-submission/issues/43),

### Database software bindings

 Bindings and wrappers for database APIs.

 * Example: [Example from rOpenSci - rrlite](https://github.com/ropensci/software-review/issues/6)


## Domain areas

In addition, our scope includes focused domain areas. These areas are based on
partnerships that we form with communities and also expertise that we hold
within our organization. As we develop [new community partnerships](/partners/scientific-communities) and grow,
we will expand this list.

### Geospatial

Packages focused on the retrieval, manipulation, and analysis of spatial data.

* Examples: [PyGmt](https://github.com/pyOpenSci/software-submission/issues/43),
[Moving Pandas ](https://github.com/pyOpenSci/software-submission/issues/18)

### Pangeo

We have a [partnership with Pangeo](../partners/pangeo). Often times packages submitted as a part of that partnership are also in the geospatial domain.

* Examples: [xclim - under review now](https://github.com/pyOpenSci/software-submission/issues/73)

### Education

Packages to aid with instruction.

* Examples: [pyrolite](https://github.com/morganjwilliams/pyrolite)

## Package technical scope

To be in technical scope for a pyOpenSci review, your package:

* Should have maintenance workflows documented.
* Should declare vendor dependencies using standard approaches rather than including code from other packages within your repository.
* Should not have an exceedingly complex structure. Others should be able to contribute and/or take over maintenance if needed.

```{admonition} pyOpenSci's goal is to support long(er) term maintenance
pyOpenSci has a goal of supporting long term maintenance of open source
Python tools. It is thus important for us to know that if you need to step down as a maintainer, the package infrastructure and documentation is
in place to support us finding a new maintainer who can take over you
package's maintenance.
```

### What if my package seems like its category or domain is out of scope?
- pyOpenSci is still developing as a community. If your scientific Python
package does not fit into one of the categories or if you have any other
questions, we'd encourage you to open a pre-submission inquiry. We're happy to help.
- Data visualization packages come in many varieties, ranging from small
hyper-specific methods for one type of data to general, do-it-all packages
(e.g. matplotlib). pyOpenSci accepts packages that are somewhere in between the
two. If you're interested in submitting your data visualization package, please
open a pre-submission inquiry first.

## Examples of packages that might be out of technical scope

pyOpenSci may continue to update its criteria for technical scope
review as more packages with varying structural approaches are reviewed.
Your package **may not be in technical scope** for us to review at this time if
fits any of the out-of-technical-scope criteria listed below.

Your package is in technical scope if it is:
* Pure Python or Python with built extensions
* Available from PyPI and/or community conda channels such as conda-forge or bioconda

Your package might be out of in technical scope if it is:
* Not published in a community channel such as PyPI or a channel on anaconda cloud
* Exceedingly complex in its structure or maintenance needs

A few examples of packages that may be too technically challenging for us to
find a new maintainer for in the future are below.

### Example 1: Your package is an out of sync fork of another package repository that is being actively maintained.

Sometimes we understand that a package maintainer may need to step down. In
that case, we strongly suggest that the original package owner, transfer the
package repository to a new organization along with PyPI credentials. A new
organization would allow transfer of ownership of package maintenance rather
than several forks existing.

If your package is a divergent fork of a maintained repository we will encourage you
to work with the original maintainers to merge efforts.

However, if there is a case where a forked repository is warranted, please
consider submitting a pre-submission inquiry first and explain why the package is a
fork rather than an independent parent repository.

### Example 2: Vendored dependencies

If your package is a wrapper that wraps around another tool, we prefer that
the dependency be added as a dependency to your package. This allows
maintenance of the original code base to be independent from your package's
maintenance.

(package-overlap)=
## Package Overlap
pyOpenSci encourages competition among packages, forking and re-implementation
as they improve options of users. However, we strive to make packages in the
pyOpenSci suite to represent our top recommendations for the tasks that they
perform. We aim to avoid duplication of functionality of existing Python
packages in any repo without significant improvements. A Python package that
replicates the functionality of an existing package may be considered for
inclusion in the pyOpenSci suite if it significantly improves on alternatives by
being:

- More open in licensing or development practices
- Broader in functionality (e.g., providing access to more data sets, providing
a greater suite of functions), but not only by duplicating additional packages
- Better in usability and performance
- Actively maintained while alternatives are poorly or no longer actively maintained

These factors should be considered as a whole to determine if the package is a
significant improvement. A new package would not meet this standard only by
following our package guidelines while others do not, unless this leads to a
significant difference in the areas above.

We recommend that packages highlight differences from and improvements over
overlapping packages in their `README` and/or vignettes or get started tutorials.

We encourage developers whose packages are not accepted due to overlap to still
consider submittal to other repositories or journals.
