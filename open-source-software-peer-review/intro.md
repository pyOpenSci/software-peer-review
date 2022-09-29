# How Peer Review Works

```{tableofcontents}
```

## Why do we need pyOpenSci peer review?

The open peer review process lead by pyOpenSci address several issues in the scientific Python
ecosystem:

1. [Multiple packages that have overlapping functionality. See this example on `PyPI`](https://pypi.org/search/?q=twitter) 
2. Packages that have varying levels of maintenance yet are used by the community to support open science workflows. 
3. Packages that are well-maintained and used but then maintenance comes to a halt when the maintainer needs to step down (burn-out is common and understandable).
4. Packages using varying types of packaging and documentation approaches making it more difficult to contribute.
5. Packages that are not documented enough to support:
   * Contributions from others
   * Directions on how to get started using the package functionality (quick start vignettes or tutorials)  
* Packages that are missing OSI licensing and citation information

### How is pyOpenSci different from JOSS and other review processes?
pyOpenSci is different from other review processes
out there because:

1. We specifically review to community accepted python packaging standards
2. We consider accepted packages as vetted and a part of our ecosystem. We recommend those packages to others. If the maintainer needs to step down, we will ensure a new maintainer takes over OR sunset and remove the package from our ecosystem.

The JOSS review process is about publication. There, you will receive a DOI that is cross-ref
enabled. However JOSS will not followup with the maintainer to ensure that the package is maintained over time. 


## Why submit your package to pyOpenSci for review?

There is a lot to gain from submitting your package to pyOpenSci.
But of course, before you submit, please be sure to read the policies 
... to ensure pyOpenSci is the right fit for you. 

First, and foremost, we hope you submit your package for review **because you value the feedback**.  We aim to provide useful feedback to package authors and for our review process to be open, non-adversarial, and focused on improving software quality.

- Once your package is accepted, your package will receive **support from pyOpenSci members**. You'll retain ownership and control of your package. However, if you need help with ongoing maintenance issues, we will try to find people who can help. 
  
-  pyOpenSci will **promote your package** through our:
   - [webpage](https://pyopensci.org/python-packages/), 
   - [blog](https://wwwpyopensci.org/blog/), and 
   - [social media account](https://twitter.com/pyopensci).

-   pyOpenSci packages that are in scope for the [Journal of Open-Source Software](https://joss.theoj.org/) and add the necessary accompanying short `paper.md` file, can, at the discretion of JOSS editors, benefit from a fast-tracked review process. [Read more about our partnership with JOSS here](#pyopensci-and-joss).

## Why do we need peer review for Python scientific software?

pyOpenSci's [suite of packages](https://pyopensci.org/python-packages/) are fully 
contributed by community members with a great diversity of skills. This diversity 
of developer backgrounds results in a range of quality associated with the suite 
of tools available to process scientific data.

### Peer review helps maintain consistent open source software quality

Peer review of python tools that support science is critical to enforcing 
quality and usability standards. All pyOpenSci packages contributed by the 
community undergo a transparent, constructive, non adversarial and open peer 
review process. The goal of that process is to enforce commonly accepted standards.
These standards include technical structure of the package, usability of the 
package, documenting package functionality in a way that is accessible 
to all levels of users and proper licensing and citation information. 

### A truly community-founded review process

Our peer review process is run by volunteer members of the Python scientific 
community:

* Editors manage the incoming package review submissions and ensure 
reviews move forward progress of submissions; 
* authors create, submit and improve their package; 
* Reviewers, two per submission, examine the software code and user experience. 

```{note}
[This blog post](https://www.numfocus.org/blog/how-ropensci-uses-code-review-to-promote-reproducible-science/) written by editors from our partner organization, rOpenSci, is a good introduction to pyOpenSci software peer review 
```
### How do I know a python package is pyOpenSci vetted?

You can identify pyOpenSci packages that have been peer-reviewed by the green 
"peer-reviewed" badge at the top their README, [![pyOpenSci](https://tinyurl.com/y22nb8up)]() linking to the specific issue
where the tool was reviewed. [See this example from devicely, one of our packages](https://github.com/hpi-dhc/devicely).

### How do reviews work?

We use GitHub for our entire review process. We like GitHub because:

* It's free to create an account
* It facilitates collaboration and supports community around a package
* It facilitates open discussion via issues
* It supports version control
* Numerous packages store their code bases on GitHub

We make the most of [GitHub](https://github.com/)infrastructure in
our review process.

Each package review is contained within an issue in the [pyOpenSci/software-review GitHub repository](https://github.com/pyopensci/software-review/). 


```{note}
For instance, click [here](https://github.com/ropensci/software-review/issues/24) to read the review thread from an rOpenSci review of the `ropenaq` package. Note that the  process is an ongoing conversation until the package is accepted. Two external reviews are important milestones in the review process. 
```

### GitHub tools including issue submission templates and labels help us streamline peer review
We use GitHub features including:

* issue templates (as submission templates), and
* labelling issues to track progress of submissions (from editor checks to approval).
* Project boards to track help wanted items

All of this functionality supports a streamlined and open peer review
process. 

## Why review a package for pyOpenSci?

We hope you choose to review **to give back to the rOpenSci and scientific communities.**  Our mission to expand the ability to efficiently use scientific data and promote a culture of open reproducible is only possible through the volunteer efforts of community members like you.

-   Peer review is a two-way conversation. By reviewing packages, you'll have the chance to **continue to learn development practices from authors and other reviewers**.
-   The open nature of our review process allows you to **network and meet colleagues and collaborators** through the review process. Our community is friendly and filled with supportive members expert in Python package development, a diversity of science domains and computer science.

### Volunteer to review for us
-   To volunteer to be one of our reviewers, fill out [this short form](https://forms.gle/9dv99gri6XKNU8177). In the form you will provide your contact information and areas of expertise. We are always looking for more reviewers with both general package-writing experience and domain expertise in the fields where packages are used. Some of our reviewers focus on package usability and documentation. This allows you to review even if you don't have strong technical background. We will pair you with a second reviewer that can focus more on the technical aspect of the review. 

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


### If you submit to pyOpenSci You Can Also Be Accepted by JOSS
We have a strong partnership with JOSS (Journal of Open Source Software); JOSS
accepts our review as their own. If your package is within JOSS' scope you can 
then submit it to JOSS, linking to the accepted pyOpenSci review. Note that
JOSS won't accept packages that are don't have research applications such as 
API wrappers. JOSS will then accept our review (you will not need a second 
review with JOSS!). JOSS will review your paper and you will get a JOSS badge 
to add next to your pyOpenSci badge of review. And a cross-ref enabled DOI.


## pyOpenSci and JOSS

> You don't have to chose between pyOpenSci and JOSS; You can submit your package to both.

pyOpenSci and [the Journal of Open Source Software (JOSS)](https://joss.theoj.org/)
are complementary, partner organizations; and you don't have to chose one or the 
other! After a package to pyOpenSci has been reviewed and accepted by pyOpenSci
you can chose to also register it with JOSS. JOSS has [more limited scope](https://joss.readthedocs.io/en/latest/review_criteria.html)  of the 
for packages that it will review. For instance while pyOpenSci will review and 
accept API wrappers, JOSS won't. 

If your package is accepted by pyOpenSci and in scope for JOSS, JOSS will fast 
track your package through their process given it was already reviewed by us.
Once accepted by JOSS, you now have both a pyOpenSci acceptance and one by JOSS. 
Joss will then give you a cross-ref supported DOI for citation. 

### Why Two Review Processes JOSS and pyOpenSci? 

the pyOpenSci review process is different from that of JOSS in a few ways:
* pyOpenSci is specific to the Python community and thus will enforce community specific python specific standards. 
* pyOpenSci places heavy emphasis on documentation and usability in our reviews and associated standardization of both.
* pyOpenSci builds community around and visibility for it's tools.
* pyOpenSci supports long term tool maintenance.    


JOSS reviews are [more limited in scope](https://joss.readthedocs.io/en/latest/review_criteria.html) compared to pyOpenSci and the
[submission criteria](https://joss.readthedocs.io/en/latest/review_criteria.html)
are, in places, less stringent than those of pyOpenSci.
