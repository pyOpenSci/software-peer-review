## Python package domain scope

The following categories are the current domain areas that fall into the
pyOpenSci domain scope.

- **Data retrieval:** Packages for accessing and downloading data from online sources. Includes wrappers for accessing APIs.
- **Data extraction:** Packages that aid in retrieving data from unstructured sources such as text, images and PDFs.
- **Data munging:** Tools for processing data from scientific data formats.
- **Data deposition:** Tools for depositing data in scientific research repositories.
- **Reproducibility:** Tools to scientists ensure that their research is reproducible. E.g. version control, automated testing, or citation tools.
- **Geospatial:** Packages focused on the retrieval, manipulation, and analysis of spatial data.
- **Education:** Packages to aid with instruction.
- **Data visualization:** Packages for visualizing and analyzing data.

## Package technical scope

To be in technical scope for a pyOpenSci review, your package:

* Should have maintenance workflows documented.
* Should be structured in a way that someone else could contribute to it.
* Should declare vendor dependencies using standard approaches rather than including code from other packages within your repository.

### Notes on scope categories
- pyOpenSci is still developing as a community. If your scientific Python
package does not fit into one of the categories or if you have any other
questions, we'd encourage you to open a pre-submission inquiry. We're happy to help.
- Data visualization packages come in many varieties, ranging from small
hyper-specific methods for one type of data to general, do-it-all packages
(e.g. matplotlib). pyOpenSci accepts packages that are somewhere in between the
two. If you're interested in submitting your data visualization package, please
open a pre-submission inquiry first.

## Python package technical scope

pyOpenSci may continue to update its technical scope criteria for package
review as more packages with varying structural approaches are reviewed.
Your package **may not be in technical scope** for us to review at this time if
fits any of the out-of-technical-scope criteria listed below.

```{important}

**If the code base of your package is exceedingly complex in terms of
structure of maintenance needs**, we may not be able to review it.

pyOpenSci has a goal of supporting long term maintenance of open source
Python tools. It is thus important for us to know that if you need to step down as a maintainer, the package infrastructure and documentation is
in place to support us finding a new maintainer who can take over you
package's maintenance.

**Examples of technically complex package structures that may be difficult for us to
review**

## Example 1: Your package is an out of sync fork of another package repository that is being actively maintained.

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
```
