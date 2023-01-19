# pyOpenSci Peer Review Partnerships 

pyOpenSci collaborates with organizations that support the scientific 
community.

## Software peer review support for scientific communities 
pyOpenSci is launching a prototype collaboration that supports an existing 
scientific community.  

### What pyOpenSci provides to existing communities 
In addition to [the core benefits that pyOpenSci peer review provides](/about/benefits), 
we also provide infrastructure and resources for: 
* Peer review of tools in the community's ecosystem 
* Adoption of community specific review standards which will be enforced in addition 
 [to our existing review guidelines](editor-checklist-template) 
* Maintenance support to maintainers that go through our review. 
* Support for finding a new package maintainer in case the current one needs to step down.
* A catalog of vetted tools and a community landing page. 

### Partnership benefits to the broader scientific community 
The benefit of communities partnering with us is: 

* We have a broad view across all scientific ecosystems which will help us to better identify overlap of package functions.
* We also have broader reach to users of scientific software across the ecosystem.
* Finally a consolidated peer review process will help enforce standardization of scientific Python packaging and best pratices across the ecosystem. 
<!-- 
## Pangeo 

pyOpenSci is launching a prototype effort to explore what it looks like to 
support [Pangeo](https://pangeo.io/). 

If you are submitting a package for review that fits into the Pangeo ecosystem,
your package will be:

* Reviewed against current pyOpenSci guidelines and checks. 
* Also reviewed against the Pangeo-specific guidelines below.
-->

<!-- 
```{admonition} Pangeo Review Guidelines
:class: note

On top of the pyOpenSci review guidelines, we will also perform checks for 
the following: 

* **Consume and produce high-level data structures** (e.g. **Xarray datasets**, **Pandas DataFrames**) wherever feasible: 
* **Operate lazily when called on Dask data structure:** Lazy loading refers to a tool only performing operations on data when it's needed. Lazy loading is ideal for workflows using larger datasets which will quickly consume memory and compute power when you work with them. [Learn more here.](https://saturncloud.io/blog/a-data-scientist-s-guide-to-lazy-evaluation-with-dask/)  
TODO: Is this the best link for an overview of lazy loading - maybe there is a tutorial?? 
* **Avoid file I/O unless your package is specifically an I/O package:** I/0 refers to data input and output of data.
TODO: Ask tom for a better explanation of what this specific means and add a link if there is one ? 
``` -->
