# pyOpenSci Open Peer Review Goals and Scope

pyOpenSci has several goals to support the scientific Python open source 
community.

1. **Packages with overlapping functionality:** 
It's easy to find multiple packages on `PyPI` that perform that same tasks (or overlapping tasks). When you submit to us, we ask that you know about other packages in our system that may do similar things. This check will help us connect maintainers who are working on similar goals. It will also help us in the long term reduce the number of overlapping packages, in various states of maintenance on `PyPI`.

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

1. The need for community around and support for smaller Python packages that 
support open science. 

## Is Your Package in Scope For pyOpenSci Review?
pyOpenSci reviews packages within a set of categories define below. 
If you are unsure whether your package fits into one of these categories, please 
open a [pre-submission inquiry via a GitHub Issue](LINK) to get feedback from 
one of our editors. We are happy to look at your package and help you understand 
whether it is in scope or not. 

```{include} ../scope.md
```

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
