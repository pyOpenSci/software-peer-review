# Editor in Chief Guide

## Editor in Chief (EiC) role & responsibilities

The Editor in Chief (EiC) is a rotating position that serves 
for 3 to 6 months or a time agreed to by all members of the editorial 
board. 

If the EiC needs to step down at any time before the agreed-upon 
duration of their tenure, pyOpenSci requests and appreciates 2 weeks notice
to support finding a new EiC.

### The Editor in Chief fulfills the following roles:

- Watches all issues posted to the [software-review repository](https://github.com/pyOpenSci/software-review/issues) (by "watching" it on GitHub to receive notifications, and by joining the `#feed-software-review` channel on Slack).
- Performs an initial set of editor checks on new package submissions (see {ref}`template <editor-checklist-template>` for these checks below)
- Raises scope/overlap issue with all editors if they see an ambiguous submission. 
This may also be done by handling editors if appropriate (see note below). If 
the scope of a package is in question, the EiC should post to the pyOpenSci 
Slack `software-review` channel, tagging all editors.
- Assigns package submissions to other editors to handle. Assigning may be based upon domain background or just who has bandwidth to lead the review. The editor in chief can assign packages to themself for review.
- Responds to pre-submission inquiries posted to the software-review repository 
and similarly pings editors in the `software-review` Slack channel if discussion 
is needed. Any editor should feel free to communicate with package authors as it 
makes sense. See [this section](#responding-to-out-of-scope-submissions) about 
how to respond to out-of-scope (pre-) submissions.
- Responds to review referrals from JOSS or other publication partners.
- Monitors pace of review process and reminds other editors to move packages along as needed.
- Requests a new EiC when their rotation is up (set a calendar reminder ahead of your expected end date and ask for volunteers in the editors’ Slack channel)

This Editor in Chief position rotates between different pyOpenSci editors. 

```{note}
In some cases, if the EiC is unable to support review of a particular package due to 
conflicts OR if they simply believe another editor is better suited to assess 
the scope and readiness of a package to be reviewed, they may opt to assign an editor to perform initial checks.
```

## Editor in Chief checklist

When a new package is submitted for review, the Editor in Chief will:

### 1. ✅ Tag the issue with `1/editor-checks` tag in GitHub

### 2. ✅ Next, they will use the {ref}`template <editor-checklist-template>` below in the issue 

This step serves to check whether the package has 
the bare minimum requirements to initiate a review (or they will assign that task to an editor as stated above). 
These checks ensure that the package is ready to be reviewed.

Following this step will ensure that we are using our volunteer reviewer time effectively.

In some situations, these checks may be passed down to an editor including:
 
* If the Editor in Chief is overwhelmed with package submissions to evaluate 
* If the Editor in Chief simply is busy at the time and needs support with checks 
* If the Editor in Chief thinks that the checks might be better served if done by an Editor 
(For instance if a specific domain or technical expertise would support more effective checks)


(editor-checklist-template)=
### Editor checklist (copy template below to use in the issue)

```markdown
## Editor in Chief checks 

Hi there! Thank you for submitting your package for pyOpenSci
review. Below are the basic checks that your package needs to pass 
to begin our review. If some of these are missing, we will ask you 
to work on them before the review process begins. 

- [ ] **Fit**: The package meets criteria for [fit](https://www.pyopensci.org/contributing-guide/about-peer-review/aims-and-scope.html#package-categories) and [overlap](https://www.pyopensci.org/contributing-guide/about-peer-review/aims-and-scope.html#package-overlap).
- [ ] **Documentation** The package has sufficient documentation available online (README, sphinx docs) to allow us to evaluate package function and scope *without installing the package*. This includes:
  - [ ] tutorials or vignettes that help a user understand how to use the package and what it can do for them (often these have a name like "Getting started")
  - [ ] API documentation - this includes clearly written doc strings with variables defined using a standard docstring format
  - [ ] README that clearly articulates the function of the package
  - [ ] Contributing documentation that details how to install a development environment and how to contribute to the package
- [ ] **Issue Submission Documentation**: All of the information is filled out in the `YAML` header of the issue (located at the top of the issue template).
- [ ] **Automated tests:** Package has a testing suite and is tested via GitHub actions or another Continuous Integration service.
- [ ] **License:** The package has an [OSI approved license](https://opensource.org/licenses)
- [ ] **Repository:** The repository link resolves correctly
- [ ] **README:** The package has a README with clear explanation of what the package does and instructions on how to install it along with development instructions. 
- [ ] **Contributing statement:** The package has a contributing.md file that details how to contribute to the package. 
- [ ] **Package overlap:** That package doesn't fully overlap with functionality of other packages that have already been submitted to pyOpenSci
- [ ] **Archive** (JOSS only, may be post-review): The repository DOI resolves correctly
- [ ] **Version** (JOSS only, may be post-review): Does the release version given match the GitHub release (v1.0.0)?

---
- [ ] [Initial onboarding survey was filled out ](https://forms.gle/F9mou7S3jhe8DMJ16) 
We appreciate each maintainer of the package filling out this survey individually. :raised_hands: 
Thank you authors in advance for setting aside five to ten minutes to do this. It truly helps our organization. :raised_hands:
---

*******

## Editor comments


```

### 3. ✅ Finally they will ensure the onboarding survey is filled out. 

Thank the authors graciously for doing this. They can skip sections of it if they wish, but we do need their contact information and we do want to track their experience with our review process and organization. 

### 4. ✅ Assign an editor to the issue to manage the rest of the review

Once the package initial checks are complete, and it is determined that 
the package is in scope for pyOpenSci review, the Editor in Chief will assign an 
editor to the review issue. The editor will begin the process of finding reviewers 
for the package. [Check out the editor guide for more information on this process](editors-guide.md) 

### 5. ✅ Update the YAML header of the issue 

Once all of the above is complete, the Editor in Chief should:
 
- Add any comments to the bottom of your editor checks comment
- Update the yaml in the header of the issue with the editor assigned to the review 
- Add the tag `2/seeking-reviewer(s)` to the issue.

## A Note about submissions that are incomplete or vague

In some cases online documentation of a package is sparse, the README is 
minimal or hard to understand or there is no clear documentation setup. Or 
in other cases some of the YAML at the top of the issue is missing. 
This makes assessment of the package's scope much harder. 
In this case, please ask for more information. Even if the package is deemed
out-of-scope, the package documentation will improve as a result of your questions. 

Example text

```markdown
Hello <username> and many thanks for your submission.

We are discussing whether the package is in scope and need a bit more 
information.

Would you mind adding more details and context to your `README` file?
After reading it, someone with little domain knowledge should understand 
the aim, goals and functionality of the package.

<optional>
If a package has overlapping functionality with other packages, we require you 
to mention in your documentation (README) and in this issue [how it is "best in class"](https://www.pyopensci.org/contributing-guide/about-peer-review/aims-and-scope.html?highlight=overlap#package-overlap). Could you add a more detailed comparison to the packages you mention in the README so we can evaluate?
</optional>

```

### Responding to out-of-scope submissions

If the package is determined to be out-of-scope, the Editor in Chief should thank authors for their submission,
explain the reasons for the decision, and direct them to other publication venues 
if relevant. If further discussion is warranted that can take place within the issue. 