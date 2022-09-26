# Editor in Chief Guide

## Editor in Chief role & responsibilities

The Editor in Chief (EiC) is a rotating position that serves 
for 3 to 6 months or a time agreed to by all members of the editorial 
board. 

If the EiC needs to step down at any time before the agreed-upon 
duration of their tenure, pyOpenSci requests and appreciates 2 weeks notice
to support finding a new EiC.

### The Editor in Chief fulfills the following roles:

- Watches all issues posted to the software-review repo.
- Performs an initial set of editor checks on new package submissions (see template for these checks below)
- Raises scope/overlap issue with all editors if they see an ambiguous submission. 
This may also be done by handling editors if appropriate (see note below). If 
the scope of a package is in question, the EiC should post to the pyOpenSci 
Slack `software-review` channel, tagging all editors.
- Assigns package submissions to other editors (including themselves if they have bandwidth), to handle. 
- Responds to pre-submission inquiries posted to the software-review repository 
and similarly pings editors in the `software-review slack channel` if discussion 
is needed. Any editor should feel free to communicate with package authors as it 
makes sense. See [this section](#responding-to-out-of-scope-submissions) about 
how to respond to out-of-scope (pre-) submissions.
- Responds to review referrals from JOSS or other publication partners.
- Monitors the review process pace.
- Reminds other editors to move the package review process along as needed if 
the timeline seems to be stalled or slow.


This Editor in Chief position rotates between different pyOpenSci editors. 


```{note}
In some cases, if the EiC is unable to support a particular package due to 
conflicts OR if they simple believe another editor is better suited to assess 
the scope and readiness of a package to be reviewed, they may opt to assign an editor to perform initial checks.
```

## Editor in Chief checklist

When a new package is submitted for review, the EiC will:

- Tag the issue with `1/editor-checks` tag 
- Next, they will use the template below in the issue to check whether the package has 
the bare minimum requirements to initiate a review (or they will assign that task to an editor as stated above). 
- SURVEY data: To ensure we have information from the authors, please be sure that they filled out our survey. Thank them graciously for doing this. They can skip sections of it if they wish, but we do need their contact information and we do want to track their experience with out review process and organization  


### Editor checklist (copy template below to use in the issue)

```markdown
## Editor checks 

Hi there! Thank you for submitting your package for pyOpenSci
review. Below are the basic checks that your package needs to pass 
to begin our review. If some of these are missing, we will ask you 
to work on them before the review process begins. 

- [ ] **Fit**: The package meets criteria for [fit](https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/aims-and-scope.html#package-categories) and [overlap](https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/aims-and-scope.html#package-overlap).
- [ ] **Documentation** The package has sufficient documentation available online (README, sphinx docs) to allow us to evaluate package function and scope *without installing the package*. This includes:
  - [ ] Get started vignettes or tutorials that help a user understand how to use the package and what it can do for them
  - [ ] API documentation - this includes clearly written doc strings with variables defined using a standard docstring format
  - [ ] README that clearly articulates the function of the package
  - [ ] Contributing documentation that details how to install a development environment and how to contribute to the package
- [ ] **Issue Header Information**: All of the required issue header information is contained within the top of the issue.
- [ ] **Automated tests:** Package has a testing suite and is tested via GitHub actions or another Continuous Integration service.
- [ ] **License:** The package has an OSI accepted license
- [ ] **Repository:** The repository link resolves correctly
- [ ] **README:** The package has a README with clear explanation of what the packages does and instructions on how to install it along with development instructions. 
- [ ] **Contributing statement:** The package has a contributing.md file that details how to contribute to the package. 
- [ ] **Package overlap:** That package doesn't fully overlap with functionality of other packages that have already been submitted to pyOpenSci
- [ ] **Archive** (JOSS only, may be post-review): The repository DOI resolves correctly
- [ ] **Version** (JOSS only, may be post-review): Does the release version given match the GitHub release (v1.0.0)?

---
- [ ] [Initial onboarding survey was filled out ](https://forms.gle/F9mou7S3jhe8DMJ16) 
We appreciate each maintainer of the package filling out this survey individually. :raised_hands: 
Thank you authors in advance for sending 10 minutes to do this. It truly helps our organization. :raised_hands:
---

*******

## Editor comments


```

Once the package initial checks are complete, and it is determined that 
the package is in scope for pyOpenSci review, the EiC will assign an 
editor to the review. The editor will begin the process of finding reviewers for the package. [Check out the editor guide for more information on this process](editors-guide.md) 

A few final tasks to perform here:

- Add any comments to the bottom of your editor checks comment
- Update the yaml in the header of the issue with the editor assigned to the review 
- Add the tag `2/seeking-reviewer(s)` to the issue.

### Responding to out-of-scope submissions

If the package is determined to be out-of-scope, the editor in chief should thank authors for their submission,
explain the reasons for the decision, and direct them to other publication venues 
if relevant. If further discussion is warranted that can take place within the issue. 