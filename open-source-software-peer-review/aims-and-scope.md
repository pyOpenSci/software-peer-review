# pyOpenSci Open Peer Review Goals

pyOpenSci was created to address a few goals:

1. **Redundancy of packages with overlapping functionality:** 
It's easy to find multiple packages on PyPi that perform that same tasks (or overlapping tasks). When you submit to us, we ask that you know about other packages in our system that may do similar things. This check will help us connect maintainers who are working on similar goals. It will also help us in the long term reduce the number of overlapping packages, in various states of maintainence on pypi.

2. **Improve package usability:** Documentation makes it easier for scientists to use your tools. Our review process looks at documentation, quick start vignettes (code samples to get started) to make it easier for new users to get started using your package. 

3. **Standardize packaging:** There are many different ways to create a Python 
package. We will embrace community driven standards created by organizations 
such as Scientific Python and help maintainers create more consistent 
infrastructure for their packages. In the long term consistent infrastructure 
will make it easier for new contributors to contribute too.

1. **Long term maintenance:** Most maintainers are not paid and thus work on tools 
in their free time. So what happens when a maintainer of a commonly used tool wants 
to step down? We will help maintainers find someone new to take over the reigns.
If that doesn't make sense we will help the maintainer gracefully sunset the 
package. 

2. <>build community to support maintainers and empower community with contributiont skills 

## Is Your Package in Scope For pyOpenSci Review?
Below you can find a list of what general package areas are in scope for pyOpenSci.
If you are unsure whether your package fits into one of these categories, please 
open a [pre-submission inquiry via a GitHub Issue](LINK) to get feedback from 
one of our editors. We are happy to look at your package and help you understand 
whether it is in scope or not. 

## Package Categories
- **Data retrieval:** Packages for accessing and downloading data from online sources. Includes wrappers for accessing APIs.
- **Data extraction:** Packages that aid in retrieving data from unstructured sources such as text, images and PDFs.
- **Data munging:** Tools for processing data from scientific data formats.
- **Data deposition:** Tools for depositing data in scientific research repositories.
- **Reproducibility:** Tools to scientists ensure that their research is reproducible. E.g. version control, automated testing, or citation tools.
- **Geospatial:** Packages focused on the retrieval, manipulation, and analysis of spatial data.
- **Education:** Packages to aid with instruction.
- **Data visualization:**\* Packages for visualizing and analyzing data.

\* Please fill out a pre-submission inquiry before submitting a data visualization package. See the notes below.

### Notes on Categories
- pyOpenSci is young and this list is tentative. If your scientific Python package does not fit into one of the categories or if you have any other questions, we'd encourage you to open a pre-submission inquiry. We're happy to help.
- Data visualization packages come in many varieties, ranging from small hyper-specific methods for one type of data to general, do-it-all packages (e.g. matplotlib). pyOpenSci accepts packages that are somewhere in between the two. If you're interested in submitting your data visualization package, please open a pre-submission inquiry on first.
- Note that we cannot currently accept statistics and/or machine learning packages. We don't feel that we can give these the deep, thorough review that they require.

## Package Overlap
pyOpenSci encourages competition among packages, forking and re-implementation as they improve options of users overall. However, as we want packages in the pyOpenSci suite to be our top recommendations for the tasks they perform, we aim to avoid duplication of functionality of existing Python packages in any repo without significant improvements. A Python package that replicates the functionality of an existing package may be considered for inclusion in the pyOpenSci suite if it significantly improves on alternatives by being:

- More open in licensing or development practices
- Broader in functionality (e.g., providing access to more data sets, providing a greater suite of functions), but not only by duplicating additional packages
- Better in usability and performance
- Actively maintained while alternatives are poorly or no longer actively maintained

These factors should be considered as a whole to determine if the package is a significant improvement. A new package would not meet this standard only by following our package guidelines while others do not, unless this leads to a significant difference in the areas above.

We recommend that packages highlight differences from and improvements over overlapping packages in their README and/or vignettes.

We encourage developers whose packages are not accepted due to overlap to still consider submittal to other repositories or journals.
