# Appendix: Templates

These are templates to be used by editors and reviewers. When a package is submitted, the assigned editor fills out the Editor's Template and posts it in the submission's issue thread on GitHub.

## Editor's Template

```{include} editor-initial-response-template.md
```


```{include} review-template.md
```

## Review Request Template

Editors may make use of the e-mail template below in recruiting reviewers:

```{include} reviewer-request-template.md
```

[reviewers guide]: https://www.pyopensci.org/contributing-guide/peer-review-guides/reviewer-guide.html
[packaging guide]: https://www.pyopensci.org/contributing-guide/authoring/index.html#packaging-guide
[template]: https://www.pyopensci.org/contributing-guide/appendices/templates.html#review-template


## Editor Approval Comment Template
```
----------------------------------------------
🎉 <package-name-here> has been approved by pyOpenSci! Thank you <maintainer-name-here> for submitting <package-name> and many thanks to <reviewer-names-here> for reviewing this package! 😸

There are a few things left to do to wrap up this submission:
- [ ] Add the badge for pyOpenSci peer-review to the README.md of <package-name-here>. The badge should be `[![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/issue-number)`
- [ ] Add <package-name> to the pyOpenSci website. <maintainer-name>, please open a pr to update [this file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/packages.yml): to add your package and name to the list of contributors
- [ ] <reviewers-and-maintainers> if you have time and are open to being listed on our website, please add yourselves to [this file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/contributors.yml) via a pr so we can list you on our website as contributors!

<IF JOSS SUBMISSION>
This package is going to move on to JOSS for review. I believe @arfon will ask you to implement the items below but let's let him chime in here first!
- [ ] Activate Zenodo watching the repo
- [ ] Tag and create a release so as to create a Zenodo version and DOI
- [ ] Submit to JOSS using the Zenodo DOI. We will tag it for expedited review.

<IF JOSS SUBMISSION/>

All -- if you have any feedback for us about the review process please feel free to share it here. We are always looking to improve our process and our documentation in the [contributing-guide](https://www.pyopensci.org/contributing-guide). We have also been updating our documentation to improve the process so all feedback is appreciated!
```

## Generic new member template

A template for inviting others to join the pyOpenSci community calls and otherwise
get engaged.

```
< short greeting />

I'm writing to see if you'd be interested in participating with pyOpenSci, a new community around improving the quality of software in the scientific python stack.

pyOpenSci provides resources, mentoring, and documentation for making scientific python packages more useful and maintainable. It builds off of the successful rOpenSci model, with a Python flavor. It primarily coordinates a review process by which experienced developers in the scientific python ecosystem can provide feedback and suggestions to other (usually fairly small) packages.

You've been in the scientific Python community for some time now, and I think you'd be a great part of the pyOpenSci community. Would you be interested in joining us? Participation can be as small or large as you wish - for example, you could submit your own package for review in pyOpenSci, offer to be a reviewer of someone else's package, or begin attending pyOpenSci planning meetings as we build and refine our processes. We'd just be happy to have you around :-)

< short goodbye />
```
