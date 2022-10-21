# Documentation for your Python open source tool



## Requirements
This section has descriptions of all the packaging requirements for pyOpenSci.
Most of the sections also include Good/Better/Best recommendations.
Good meets the requirements, but going beyond the minimum can make package maintenance easier.



Documentation is as important to the success of your Python open source package 
as the code itself. While quality code is valuable as it gets the tasks that your
package seeks to achieve, completed, if users don't understand how to use the 
tools in your package then they won't use your tool. 


## Documentation elements that we look for when reviewing a Python package

In the pyOpenSci peer review process we look for several things when evaluating
package documentation including:

1. A clear and to the point README file 
2. Documentation of the funcaintliy of your code. This is often setup using Sphinx/ Read the docs or some other documentation platform 
3.  Sufficient API documentation of your packages API (this means that docstrings are formatted with explanations of each variable and better yet quick vignettes that demonstrate how to use the function or class)

We will discuss all of these items below

### README.md file

The README.md file is often the first thing that someone sees when they consider
installing your package. This file is the landing page of your file on package 
manager landing pages like PyPI and Anaconda. And it is your landing page in
your GitHub repository. 

#TODO provide some screenshots of what this looks like 

As such it is important that you spend some time up front creating a high quality 
readme file. This file should be located in the root of your GitHUb repository.  

# TODO find language for this that we used for earth py. The readme file should follow the best practices of starting broad and 
becoming more specific lower down in the file 

This file should at a minimum contain:

### README
 The README should include, from top to bottom:

- Your packages name
- Badges for current package version, continuous integration and test coverage. See [the badges section](#badges) for more information.
- At that top you should include a **short description** of your 
package's goals. This language should **clearly articulate** what the package does using 
easy-to-understand language that is accessible to a variety of users with 
scientific background. Consider a 12th grade level of explanation where possible 
to ensure maximum accessibility of your README file.
- Descriptive links to package tutorials or vignettes.
- Instructions on installing your package. Be sure to include instructions for both PiP and Conda if you have published to both 
- Any additional setup required (authentication tokens, etc)
- Brief demonstration of how to use the package. This description ideally includes a quick start vignette that provides a code sample demonstrating use
- A link to your online documentation
- If applicable, how the package compares to other similar packages and/or how it relates to other packages
- Instructions on how to CITE your package. 

#TODO there is redundant stuff below vs above
**Good/Better/Best Recommendations:**
- **Good:** README with name, description, installation instructions, and direction to further documentation.
- **Better/Best:** All the above plus usage examples, citation information, and CI and/or test coverage badges.

**Better:**
Ideally you should also include a quick-start code demo that provides a quick vignette 
of how the tool might be used. 

The a clear explanation of what your package does, a quick-start vignette and instructions
to install your package provide users with an easy to digest understanding of 
how your package might be useful to them. 

# TODO add some links to tools that do this well (good better best examples here)
# also add some code snippets showing a well documented function or class vs less well


# TODO Maybe add something like the readme file we created for earthpy - 

*that readme bests practices where is starts broad and gets more specific*

## Package documentation 

Your package should be well documented. While the readme is a great first step, 
you should also have a documentation website. Many prefer to use Sphinx to create 
they Python package documentation. Sphinx is great because it offers some extensions
that support things like documenting your api (see below), running and testing code 
vignettes in your docstrings and more. 

Sphinx also offers numerous themes that you can use to customize your documentation.
This contributing guide is created using a Spinx Book theme. <I PLAN TO MOVE TO book soon>

If you aren't excited about maintaining a website for your documentation, we 
suggest using the [READTHEDOCS platform](https://www.readthedocs.org) which 
allows you to easily host your documentation and track versions of your docs
as you release updates. 


# TODO LINK TO CI BUILDS FOR Documentation>
Maybe we can curate a list of CI builds that people can use??? or is that moving too close to a cookie cutter situation

## API documentation 

There are several parts of package documentation

All external package functions, classes, and methods should be fully documented with examples.

**Good/Better/Best:**
- **Good:** Manually updated documentation as text files that ship with your package.
- **Better:** A documentation website using Sphinx to convert rst files to HTML and Read the Docs to host your site.
- **Best (optional):** Also consider automatically generated documentation from docstrings using autodoc


### License file 

Your software should be licensed using an OSI approved license. The GitHub 
repo should have a license file for that specific license. 
<LINK TO A LICENSE RESOURCE(s) for selecting a license>

### CONTRIBUTING file  

pyOpenSci packages must:

- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.




### License
pyOpenSci projects should use an open source software license that is approved by the Open Software Initiative (OSI). OSI's website has a [list of popular licenses](https://opensource.org/licenses), and GitHub has a [handy tool](https://choosealicense.com/) for choosing a license.

**Good/Better/Best:**
- **Good:** Include a open source software license with your package.
- **Better/Best:** Choose a license based on your needs and future use of package, plus explain your choice in your submission for review.

## Other recommendations
### Python version support
You should always be explicit about which versions of Python your package supports.
Keeping compatibility with old Python versions can be difficult as functionality changes.
A good rule of thumb is that the package should support, at least,
the latest three Python versions (e.g., 3.8, 3.7, 3.6).

### Code Style
pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

### Linting
An automatic linter (e.g. flake8) can help ensure your code is clean and free of syntax errors. These can be integrated with your CI.

### Badges

Badges are a useful way to draw attention to the quality of your project and to
assure users that it is well-designed, tested, and maintained.
It is common to provide a collection of badges in a table for others
to quickly browse.

[See this example of a badge table](https://github.com/ropensci/drake). Such a table should be more wide than high. (Note that the badge for pyOpenSci peer-review will be provided upon acceptance.)