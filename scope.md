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

### Notes on Scope Categories
- pyOpenSci is still developing as a community. If your scientific Python 
package does not fit into one of the categories or if you have any other 
questions, we'd encourage you to open a pre-submission inquiry. We're happy to help.
- Data visualization packages come in many varieties, ranging from small 
hyper-specific methods for one type of data to general, do-it-all packages 
(e.g. matplotlib). pyOpenSci accepts packages that are somewhere in between the 
two. If you're interested in submitting your data visualization package, please 
open a pre-submission inquiry on first.

## Python package technical scope

pyOpenSci is still defining the technical scope criteria for package review.  
Your package **may not be in technical scope** for us to review at this time if
fits any of the out-of-technical-scope criteria listed below. 

- Package is an out of sync fork of another package repository. 
Sometimes we understand that a package maintainer may need to step down.  In that case, we strongly suggest that the original package owner, transfer the package to a new organization that would allow transfer of ownership of the package rather than 
a fork. However, if there is a case where a forked repository is warranted, please 
consider submitting a pre-submission inquiry first and explain why the package is a 
fork rather than an independent parent repository.
- **Vendored dependencies:** If your package is a wrapper that wraps a tool in another 
language or a lower level tool, we prefer that the dependency be added as sa 
dependency to your package so that maintenance of the original code base is independent from your package's maintenance. 
- **If the code base of your package is exceedingly complex in terms of structure of maintenance needs**, we may not be able to review it. pyOpenSci has a goal of supporting long term maintenance of tools. When a maintainer steps down, we need to know that 
the package infrastructure supports a new maintainer that is proficient in Python, stepping in to take over. 
