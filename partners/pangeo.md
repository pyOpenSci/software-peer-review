# pyOpenSci's partnership with Pangeo

pyOpenSci is creating a collaboration workflow to
collaborate with the [Pangeo](https://pangeo.io/) scientific community. Through
this collaboration we add an additional layer of peer review checks to Pangeo-related
packages that go through our [open peer review process](/about/intro).


If you are submitting a package for review that fits into the Pangeo ecosystem,
your package will be:

* Reviewed against current pyOpenSci guidelines and checks.
* Also reviewed against the Pangeo-specific guidelines listed below.

(pangeo-collaboration)=
### Pangeo Specific Software Peer Review Guidelines

In addition to [basic pyOpenSci review checks](https://www.pyopensci.org/software-peer-review/how-to/editor-in-chief-guide.html#editor-checklist-template), when reviewing a
Pangeo-related package, we will also perform the checks below that are
defined by the Pangeo community.

* **Consume and produce high-level data structures** (e.g. **Xarray datasets**, **Pandas DataFrames**) wherever feasible.
* **Operate lazily when called on Dask data structures:** To support larger-than-memory datasets, many Pangeo workflows use [Dask](https://dask.org) to parallelize the workflow. Doing this efficiently requires lazily loading data and triggering compute only when needed. See the [Dask documentation](https://docs.dask.org/en/stable/user-interfaces.html#laziness-and-computing) for more.

    * A few other resources related to lazy loading:

        * [Dask and stages of computation](https://docs.dask.org/en/stable/phases-of-computation.html): this provides and overview of using Dask effectively to optimize your compute workflow.
        * [Using Dask and Xarray together:](https://docs.xarray.dev/en/stable/user-guide/dask.html?highlight=lazy#using-dask-with-xarray) this page provides an overview of how to use Dask to optimize working with data arrays in Xarray.
        * [Tutorial on using Dask and lazy loading]( https://tutorial.dask.org/01_dataframe.html )

* **Use existing data reading and writing libraries rather than creating your own:** In general, your package should use existing libraries for reading and writing data (e.g. xarray, pandas, geopandas, or the libraries those are built on like Zarr, GDAL, pyarrow, etc.) and should not include its own custom code for read/write data operations. These tools already read and write a variety of file types to a variety of file systems that are important to Pangeo users, including Cloud Object storage.
[See: 2i2c documentation for more on cloud native file format support.](https://docs.2i2c.org/en/latest/data/cloud.html#cloud-native-formats)
