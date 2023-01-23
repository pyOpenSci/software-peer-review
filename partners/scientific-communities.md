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
* Finally a consolidated peer review process will help enforce standardization of scientific Python packaging and best practices across the ecosystem.

## Pangeo

pyOpenSci is launching a prototype effort to explore what it looks like to
support [Pangeo](https://pangeo.io/).

If you are submitting a package for review that fits into the Pangeo ecosystem,
your package will be:

* Reviewed against current pyOpenSci guidelines and checks.
* Also reviewed against the Pangeo-specific guidelines below.



```{admonition} Pangeo Specific Software Peer Review Guidelines
:class: note

In addition to [basic pyOpenSci review checks](https://www.pyopensci.org/software-peer-review/how-to/editor-in-chief-guide.html#editor-checklist-template), when reviewing a
Pangeo-related package, we will also perform checks for the following:

* **Consume and produce high-level data structures** (e.g. **Xarray datasets**, **Pandas DataFrames**) wherever feasible:
* **Operate lazily when called on Dask data structure:** Lazy loading refers to a tool only performing operations on data when it's needed. Lazy loading is ideal for workflows using larger datasets which will quickly consume memory and compute power when you work with them. Lazy loading allows a tool to create a connection to a dataset, but only actually access / open the part of the dataset that you require to use in your workflow.  [Learn more here.](https://docs.dask.org/en/stable/user-interfaces.html?highlight=lazy#laziness-and-computing)

    * A few other resources related to lazy loading:

        * [Dask and stages of computation](https://docs.dask.org/en/stable/phases-of-computation.html): this provides and overview of using Dask effectively to optimize your compute workflow.
        * [Using Dask and Xarray together:](https://docs.xarray.dev/en/stable/user-guide/dask.html?highlight=lazy#using-dask-with-xarray) this page provides an overview of how to use Dask to optimize working with data arrays in Xarray.

* **Avoid file input and output (I/O) unless your package is specifically an I/O package:** I/0 refers to data input and output of data.
    * [Read more about file input and output in the cloud](https://docs.2i2c.org/en/latest/data/cloud.html)

<!-- TODO: Ask Tom for a better explanation of
why this is important - ie wouldn't some packages like een xarray allows you to write data into a
usable format. ... need more clarification.

* We could also add content in our packaging guide as it makes sense for pangeo
guidelines - particularly if they have other best practices that they want to
see related to API dev see: https://discourse.pangeo.io/t/tutorial-idea-writing-apis-for-your-pangeo-package/3105/9
-->
