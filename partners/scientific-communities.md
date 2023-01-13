# pyOpenSci Peer Review Partnerships 

pyOpenSci collaborates several organizations that support the scientific 
community. Below is a discussion of some of our partners that have been 
involved in our peer review process 

## Software peer review support for scientific communities 
pyOpenSci is launching a prototype effort to explore what it looks like to 
support a large scientific community. In this effort we provide:

In this model, the community supports us by providing volunteer reviewers and 
and editor to help move the peer review process forward. 

### What pyOpenSci provides to existing communities 
In addition to [the core benefits that pyOpenSci peer review provides](/about/review-benefits), 
we also provide infrastructure and resources for: 
* Peer review of tools in the community's ecosystem 
* Adoption of community specific review standards which will be enforced in addition 
 [to our existing review guidelines] <!-- TODO: LINK to our editor checks here-->
* Maintenance support to maintainers that go through our review. 
* Support for finding a new package maintainer in case the current one needs to step down.
* A catalog of vetted tools and a community landing page. 

### Partnership benefits to the broader scientific community 
The benefit of communities partnering with us is: 

* We have a broad view across all scientific ecosystems which will help us to better identify overlap of package functions.
* We also have broader reach to users of scientific software across the ecosystem.
* Finally a consolidated peer review process will help enforce standardization of scientific Python packaging and best pratices across the ecosystem. 

## Pangeo 

pyOpenSci is launching a prototype effort to explore what it looks like to 
support Pangeo. 

If you are submitting a package for review that fits into the Pangeo ecosystem,
your package will be:

* Reviewed against current pyOpenSci guidelines and checks. 
* Also reviewed against the Pangeo-specific guidelines below

```{admonition} Pangeo Review Guidelines
:class: note

On top of the pyOpenSci review guidelines, we will also perform checks for 
the following: 

* Consume and produce high-level data structures (e.g. xarray datasets / pandas dataframes) wherever feasible
* Operate lazily when called on dask data structure
* Avoid file I/O unless specifically an I/O package

```



<!-- 

## rOpenSci

rOpenSci has provided a strong model for the development of 
pyOpenSci. pyOpenSci keeps in touch with and has learned 
from rOpenSci's development. 

 

OpenScience Labs

Pangeo -->