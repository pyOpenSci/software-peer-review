# pyOpenSci Software Peer Review Partnerships

```{toctree}
:hidden:
:caption: Our Partners

About Our Partnerships <self>
JOSS <joss>
Pangeo <pangeo>
```

pyOpenSci collaborates with organizations that support the
scientific community. This page focuses on domain-specific community
partnerships with communities that want to add affiliated packages to
their ecosystem through a review process.

## How does the pyOpenSci / domain community partnership work?

Numerous scientific Python communities are developing their own peer review
processes for affiliated packages. Communities with their own package
review processes can leverage our existing peer review process, which is
built on community-driven package standards. In partnership with these
communities, we enhance our standard review process with a community-specific
step that adds your specific requirements for package affiliation.

Through this single end-to-end review process, a package can potentially:

- Be accepted by pyOpenSci.
- Undergo a fast-track review and get published with JOSS.
- Achieve affiliation with your domain-specific community.

This page outlines policies for community partners collaborating with us.
For more information, please visit our website.

## What do we get when we become a pyOpenSci partner?

In addition to [the core benefits that pyOpenSci peer review provides](/about/benefits),
we will provide you with the following:

1. A community page in this peer review guide where you can define your guidelines for a package to become affiliated with your community. Check out the
   [pangeo example](pangeo). On this page, each community can define the
   peer review guidelines specific to becoming an affiliated package
   within the community.
2. A dedicated community page on the pyOpenSci website. Here, we will
   list your community along with all affiliated packages that have
   successfully undergone our review process. You can add descriptive text and graphics and branding to the page as you wish.
3. [Coming in 2024] Access to metric dashboards for all accepted packages in the
   ecosystem.
4. Access to a vibrant and diverse Python community with tremendous expertise in packaging best practices.

## Partnership benefits to the broader scientific community

The benefit for the broader scientific community include:

- We also have broader reach to users of scientific software across the ecosystem.
- We have a broad view across all scientific ecosystems which will help us to better identify overlap of package functionality.
- A consolidated peer review process will help enforce standardization of scientific Python packaging and best practices across the ecosystem.

## Frequently asked questions

Below is a list of questions that we get asked about our community partnerships.
If you have a question that is now answered here, feel free to ask it on the
[pyOpenSci discourse forum](https://pyopensci.discourse.group/).

### General peer review questions

:::{dropdown} How do I get my community involved?
:animate: fade-in-slide-down

We are always open to new partners. Please feel free to ask questions or to
leave a post on [our discourse forum](https://pyopensci.discourse.group/). We
can connect with you from there. You can also email us directly at
admin at pyopensci.org.
:::

:::{dropdown} How do you find reviewers?
:animate: fade-in-slide-down

pyOpenSci maintains a reviewer database with individuals who have signed
up using our [reviewer sign-up form](https://forms.gle/GHfxvmS47nQFDcBM6).
Our goal is to assign two reviewers for each package. Typically, one
reviewer possesses domain-specific expertise while the second may
focus on usability, installation, documentation, or packaging
infrastructure, without necessarily needing domain expertise.

We prioritize diversity among contributors in every review, ensuring
inclusion of individuals with different gender, cultural backgrounds,
and identities.
:::

:::{dropdown} What if there is a conflict of interest
:animate: fade-in-slide-down

pyOpenSci's [conflict of interest policy can be found here](https://www.pyopensci.org/software-peer-review/our-process/policies.html#conflict-of-interest-for-reviews-and-editors).
:::

:::{dropdown} How do I know that a review is community-affiliated?
:animate: fade-in-slide-down

We will add your community name as a label to our review repository here. This will allow anyone to filter for reviews specific to your community. Here is an example of the [community tag for Pangeo](https://github.com/pyOpenSci/software-submission/issues?q=is%3Aissue+label%3Apangeo+).
:::

### Affiliated review / pyOpenSci integration questions

:::{dropdown} Where do affiliated guidelines get published?
:animate: fade-in-slide-down

The criteria for a package becoming affiliated with a community needs to be clearly communicated on the partner landing page in our peer review guide. These are the criteria that will then be evaluated at the end of a review once the package has been accepted by pyOpenSci.
:::

:::{dropdown} Can a package be accepted by pyOpenSci but not affiliated?
:animate: fade-in-slide-down

Sometimes, a package may be accepted by pyOpenSci but not meet community
affiliation criteria. In such cases, the package will still be listed as an accepted pyOpenSci package. However, it will not receive community affiliation status.

While rare, if a package is rejected by pyOpenSci but the community
editor believes it should be affiliated, they can make that call.

In such cases, pyOpenSci won't list the package on its website, but the
community can list it on their page.

:::

:::{dropdown} When do the affiliated get evaluated in the peer review process?
:animate: fade-in-slide-down

We request that your community appoint a minimum of two individuals to
serve on our editorial board. During the initial Editor-in-Chief phase
of our peer review process, we assess whether a package aligns with the
scope of pyOpenSci. For potential community-affiliated packages, the
editor, who is a member of your community, will evaluate the package
both at the beginning and end of the review to determine if it meets
the criteria for affiliated status.

:::

:::{dropdown} How do we list pyOpenSci-accepted packages on our website post-review?
:animate: fade-in-slide-down

We will provide you with a link to a [.yml file similar to the one that drives
our website here](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/packages.yml)
that is updated via a GitHub action cron job. This file will contain a list of
packages for your community.
:::

### Package maintenance

::::{dropdown} “Rereview” of packages & package maintenance
:animate: fade-in-slide-down

A core goal of pyOpenSci is to support long-term maintenance of Python
scientific packages. To achieve this, we monitor repository activity for all
our packages to detect any signs of becoming unmaintained.

However, pyOpenSci does not conduct full re-reviews, involving the Editor-in-
Chief, Editor, and two reviewers, for packages that have already been
accepted.

:::{note}
We intend to establish automated checks to monitor the "health" and
maintenance status of packages over time. These checks aim to identify
unmaintained packages. [View our process for this here:](https://www.
pyopensci.org/software-peer-review/our-process/policies.html#maintainer-
responsiveness).

Once we identify a tool requiring additional maintenance, we will flag it
for our user community.

:::

In the event that a package becomes unmaintained, we will adhere to
the [current pyOpenSci policies regarding package maintenance
post-review](https://www.pyopensci.org/software-peer-review/our-process/
policies.html#after-acceptance-package-ownership-and-maintenance).

If it's a widely-used package and the maintainer wishes to see it
continue, we will make efforts to assist the maintainer in finding a
new team of maintainers.

Otherwise, we will gracefully sunset it, removing it from our list
of actively maintained and accepted packages.
::::

:::{dropdown} How will you track package maintenance?
:animate: fade-in-slide-down

We will track package maintenance by collecting metrics such as the commit frequency,
releases, and passing tests. Some, if not most, of this
data collection will be automated using the GitHub API and other community tools.
:::

### Packaging guidelines

:::{dropdown} How do you develop your packaging guidelines?
:animate: fade-in-slide-down

## Packaging Guidelines

pyOpenSci is developing a [community-driven packaging guide](https://www.pyopensci.org/python-package-guide/)
that encompasses modern best practices and recommendations for scientific
Python packaging. This guide undergoes a stringent community review process
involving reviewers from various groups, including members of PyPA, the core
Python team, Anaconda, conda/conda-forge maintainers, and maintainers of
core packages and front-end/back-end tools (e.g., flit, PDM, hatch/hatchling,
etc.). Additionally, it is actively maintained by members of both the scientific
Python community and maintainers.

:::

:::{dropdown} What if we already have community packaging guidelines?
:animate: fade-in-slide-down

While it's perfectly fine if your community has its own packaging guidelines,
we encourage the broader scientific community to adopt similar packaging best
practices. Doing so will enhance the experience for new contributors across
different domains. If you have the bandwidth and are interested in
collaboration, we welcome contributions to our community-driven pyOpenSci
packaging guide.
:::

## For communities with existing peer review processes

For communities with existing peer review processes and accepted packages,
we recommend the following steps:

1. If you're in the process of transitioning your review process, start by
   looking for packages that have recently entered the review phase.
   Reach out to the maintainers of these packages and see if they'd be
   interested in shifting their review to pyOpenSci. If you already have
   an editor leading the review, they can become a guest editor on our
   board and continue the review using our process. We're also available
   to mentor any new editors through our review process.

2. For packages that have already undergone review, consider prioritizing
   the older ones. Older packages are more likely to become unmaintained
   over time. This presents an excellent opportunity to re-evaluate
   packages that were accepted in previous years by taking them through
   our pyOpenSci peer review process.

### Review is scary. How do we convince our package maintainers to do more work?

We recognize that peer review can feel daunting, especially for those
from academic backgrounds. Our review process diverges from conventional
methods. We see review as a constructive dialogue involving the maintainer
team, reviewers, and an editor, all collaborating to enhance the package's
quality and user-friendliness. Occasionally, our editors and reviewers even
create issues and pull requests. Our community is readily available to
address technical inquiries.

Although participating in a review demands extra time and effort, the
benefits are substantial. Improving packaging infrastructure, documentation,
and code makes your package more accessible and welcoming to contributors.
Over time, this investment will yield significant rewards.

All our reviews are open on GitHub, ensuring transparency. Everyone
participating in the peer review process is also expected to adhere to our
code of conduct.
