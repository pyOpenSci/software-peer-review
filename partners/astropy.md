# pyOpenSci's partnership with Astropy

:::{image} /images/astropy_project_logo.svg
:alt: The Astropy logo. The logo is an orange egg shape with a white snake spiraling in it. The text of the image says The Astropy Project on three lines.
:width: 600px
:align: center
:::

pyOpenSci has a collaboration with the [Astropy scientific community](https://www.astropy.org/). Through this collaboration we add an additional layer of peer review checks to Astropy-related packages that go through our [open peer review process](https://www.pyopensci.org/software-peer-review/about/intro.html). If the package meets both the [Astropy criteria for becoming an affiliated package](https://www.astropy.org/affiliated/#becoming-an-affiliated-package) and our pyOpenSci peer review criteria, it can then become both an Astropy-affiliated package and a pyOpenSci ecosystem package.

If you are submitting a package for review and wish to also apply for Astropy affiliation, your package will be:

* Reviewed against current pyOpenSci guidelines and checks.
* Also reviewed against the Astropy-specific guidelines listed below.

(astropy-collaboration)=
### Astropy Specific Software Peer Review Guidelines

To be an affiliated Astropy package, your package should:

- Be useful to astronomers. This can mean useful to a specific sub-domain of astronomy, or more broadly useful to a large fraction of astronomy (or beyond, as long as it is also useful for astronomy).
- Specifically use, interface with, or provide complementary capabilities to other Astropy packages.
- Use classes and functions from the astropy core package wherever possible and appropriate, and (as much as possible) avoid duplication with other packages in the Astropy ecosystem. This facilitates reuse of code and sharing of resources.

### Ecointegration - Integration with the Astropy Ecosystem

Your package should clearly integrate into the broader Astropy ecosystem. It should:

- Use Astropy or other affiliated packages wherever possible
- Use / depend upon astropy or other affiliated packages functionality wherever possible to avoid duplication of functionality across the ecosystem.

## Long-term maintenance & affiliate status over time

All packages accepted into the pyOpenSci ecosystem will follow the [pyOpenSci
policies](archive-process) associated with package maintenance.

They will also need to follow the Astropy standards as follows:

If packages become unmaintained or do not meet the standards anymore, they may be removed from the list of affiliated packages.

This rule also applies to any package that applies for affiliated status with a
specific domain community through the pyOpenSci partnership program.
