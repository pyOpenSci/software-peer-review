# pyOpenSci Software Peer Review Goals 

Python is a flexible programming language that is used across numerous 
disciplines and domains. In the scientific domain, Python packaging has complex 
requirements as it often needs to support extensions or tools written in other languages 

To support the many uses of Python, there are many ways 
to create a Python package. 

```{admonition} Python supports extensions written in other languages
:class: info

Python is a unique programming language in that it supports developers wrapping 
other languages. In many scientific applications, such as working with spatial 
data, the core tools are written in other languages. Developers then create an 
interface (an API) that allows users to install python and work with that spatial 
tool in Python.  
```

The diversity of options can be confusing for new
comers.


## Working towards standardized packaging practices in the Scientific Python community

While there is no single solution to the diverse needs of developers in the 
Python scientific community, pyOpenSci strives to encourage a standard approach 
to packaging, through:

1. Best practices in packaging that follow modern Python Enhancement Protocols (PEPS), which are standards written for the Python community
1. Best practices in the scientific community which tends to have packages that include tools developed in other languages. The scientific community has additional layers of complexity in their tool builds.
1. Best practices in developing documentation to support usability and accessibility.

As such we will embrace community driven standards created by organizations
such as [Scientific Python](https://scientific-python.org/).

We also strive to help maintainers use consistently similar infrastructure for
their packages. In the long term, consistent infrastructure and packaging approaches
will:

* Make is easier for those who are new to packaging to get started (and in turn push open science forward)
* Make it easier for new contributors to participate given similar infrastructure setup across the ecosystem.

As it makes sense, we recommend (but do not require) packaging approaches implemented by existing
packages in the scientific Python ecosystem.



## 1. Improve package usability

Clear and useful documentation makes it easier for scientists to use your tools. 
During our reviews, we look carefully at:
* documentation, 
* quick start tutorials and code examples to help users get started
* and code documentation (docstrings)

To ensure that the package is user friendly. If you need help with documentation, 
We also have an entire section of our packaging guide devoted to documentation. 

## Address packages with overlapping functionality

It's easy to find multiple packages on `PyPI` that perform that same tasks 
(or overlapping tasks). When you submit a package to us, we ask that you know 
about other packages in our system that may do similar things. This check will 
help us connect maintainers who are working towards similar functionality goals. 
It will also help us in the long term reduce the number of overlapping packages, 
in various states of maintenance on `PyPI`.

In some cases just added information to your README.md about how your 
package varies from others in the ecosystem is valuable to users. 

* [See our discussion of package overlap for more](package-overlap)



1. **Long term maintenance:** Most maintainers are not paid and thus work on tools 
in their free time. So what happens when a maintainer of a commonly used tool wants 
to step down? We will help maintainers find someone new to take over the reigns.
If that doesn't make sense we will help the maintainer gracefully sunset the 
package. 

1. The need for community around and support for smaller Python packages that 
support open science.  -->
