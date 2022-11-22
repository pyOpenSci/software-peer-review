# About the pyOpenSci peer review process

```{tableofcontents}
```

## What is software peer review? 

Software peer review refers a peer-review process that focuses on open source software code, documentation and infrastructure. In pyOpenSci this review includes: 

* Code quality,
* Documentation quality,
* Package usability, 
* Testing that supports both code function and making it easier for others to contribute and evaluate how their contribution impacts other parts of the code,
* Quality of infrastructure that contribute to software quality and reliability. 

## What types of packages does pyOpenSci review? 
pyOpenSci reviews higher level software packages that support scientific workflows. 

:::{figure-md} fig-target

<img src="../images/python-stack-jupyter-earth.png" alt="Image showing the tiers of software in the python ecosystem starting with Python itself and as you move out packages become more domain specific. In this image packages like xarray and numpy are considered core to scientific python. Packages and distributions like astropy, simpeg and metpy are considered to be domain specific." width="700px">

Diagram showing the Python ecosystem from the earth science perspective. pyOpenSci's review
process focuses on domain specific packages rather than core packages as 
these packages tend to have more variability in long term maintenance and 
package infrastructure and quality compared to established core packages. **Source Jupyter meets earth**
:::
 

Currently, the packages that pyOpenSci reviews also need to fall into the 
technical and applied scope of our organization. This scope may expand over time 
as the organization grows.

## Why does the scientific community need software peer review?

The pyOpenSci open peer review process addresses several issues in the 
scientific Python ecosystem:

1. [Multiple packages that have overlapping functionality. See this example of the many packages that interface with Twitter on `PyPI`](https://pypi.org/search/?q=twitter) 
1. Packages that have varying levels of maintenance yet are used by the community to support open science workflows. 
1. Packages that are well-maintained and used but then maintenance comes to a halt when the maintainer needs to step down (burn-out is common and understandable).
1. Packages using varying types of packaging and documentation approaches making it more difficult to contribute.
1. Packages that are not documented enough to support:
   * Contributions from others
   * Directions on how to get started using the package functionality (quick start vignettes or tutorials)  
1. Packages that are missing OSI licensing and citation information

### Why is pyOpenSci focused on the Python programming language? 

These challenges with open source software exist in other ecosystems as well.  [rOpenSci](https://www.ropensci.org), an inspirational, sister organization of pyOpenSci, is an 
example of an organization with similar values that operates in the scientific R programming language 
space. However many of the issues 
faced within the scientific Python community are broader in scale given the 
numerous and diverse applications that the Python programming language is used for.

```{note}
[This blog post](https://www.numfocus.org/blog/how-ropensci-uses-code-review-to-promote-reproducible-science/) written by editors from our partner organization, rOpenSci, is a good introduction to pyOpenSci software peer review 
```

### Peer review of open software helps maintain consistent open source software quality

Peer review of python tools that support science is critical to enforcing 
quality and usability standards. All pyOpenSci packages contributed by the 
community undergo a transparent, constructive, non adversarial and open peer 
review process. The goal of that process is to enforce commonly accepted standards.
These standards include technical structure of the package, usability of the 
package, documenting package functionality in a way that is accessible 
to all levels of users and proper licensing and citation information.


## Why are reviews open?

Our reviewing threads are public. Authors, reviewers, and editors all know 
each other’s identities. The broader community can view or even participate 
in the conversation as it happens. This provides an incentive to be thorough 
and provide non-adversarial, constructive reviews. 

It also has the benefit of building a community. Participants have the 
opportunity to meaningfully network with new peers, and new collaborations 
have emerged via ideas spawned during the review process.

We are aware that open systems can have drawbacks. For instance, in 
traditional academic review, [double-blind peer review can increase representation of female authors](https://www.sciencedirect.com/science/article/pii/S0169534707002704), 
suggesting bias in non-blind reviews. 

It is also possible reviewers are less critical in open review. However, we 
believe that the openness of the review conversation provides a check on 
review quality and bias; it’s harder to inject unsupported or subjective 
comments in public and without the cover of anonymity. 

> Ultimately, we 
> believe that having direct and public communication between authors and 
> reviewers improves quality and fairness of reviews.

### How do I know that a Python package has been reviewed by pyOpenSci?

You can identify pyOpenSci packages that have been peer-reviewed by the green 
"peer-reviewed" badge at the top their `README.md` file, [![pyOpenSci](https://tinyurl.com/y22nb8up)](). This badge is added by the package author, after the package
has successfully completed review and ideally links to the specific GitHub issue
where the tool was reviewed. [See this example from devicely, one of our accepted pyOpenSci ecosystem packages](https://github.com/hpi-dhc/devicely).



********

