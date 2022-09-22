# Editor in Chief Guide

## Editor in Chief Role & Responsibilities

The Editor in Chief (EiC) is a rotating position that serves 
for 3 months or a time agreed to by all members of the editorial 
board. 

If the EiC needs to step down at any time before the agreed-upon 
duration of their tenure, pyOpenSci requests and appreciates 2 weeks notice
to support finding a new EiC.

The Editor in Chief fulfills the following roles:

- Watches all issues posted to the software-review repo.
- Performs an initial set of EiC checks (see template for these checks below)
- Raises scope/overlap issue with all editors if they see an ambiguous submission. 
This may also be done by handling editors if appropriate (see note below). If 
the scope of a package is in question, the EiC should post to the pyOpenSci 
Slack `software-review` channel, tagging all editors.
- Assigns package submissions to other editors, including themselves, to handle. 
This position most often will rotate between different pyOpenSci editors. 

```{note}
In some cases, if the EiC is unable to support a particular package due to 
conflicts OR if they simple believe another editor is better suited to assess 
the scope and readiness of a package to be reviewed, an editor may be 
assigned to perform the EiC checks.
```

- Responds to pre-submission inquiries posted to the software-review repository 
and similarly pings editors in the `software-review slack channel` if discussion 
is needed. Any editor should feel free to communicate with package authors as it 
makes sense. See [this section](#responding-to-out-of-scope-submissions) about 
how to respond to out-of-scope (pre-) submissions.
- Responds to review referrals from JOSS or other publication partners.
- Monitors the review process pace.
- Reminds other editors to move the package review process along as needed if 
the timeline seems to be stalled or slow.

## Editor in Chief Checklist

When a new package is submitted for review, the EiC will start by tagging the issue:

- Tag issue with `1/editor-checks` tag and assign a main editor.

Next, they will use the template below in the issue to check whether the package has 
the bare minimum requirements to initiate a review. Again if the EiC feels like this
task would be best completed by an Editor, they can ask the editor to step in at this
point and review the package. 

```
## Editor in Chief Checks (or Editor Checks if that is appropriate):

- [ ] **Fit**: The package meets criteria for [fit](https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/aims-and-scope.html#package-categories) and [overlap](https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/aims-and-scope.html#package-overlap).
- [ ] **Issue Header Information**: All of the required issue header information is contained within the top of the issue.
- [ ] **Automated tests:** Package has a testing suite and is tested via GitHub actions or another Continuous Integration service.
- [ ] **License:** The package has an OSI accepted license
- [ ] **Repository:** The repository link resolves correctly
- [ ] **README:** The package has a README with clear explanation of what the packages does and instructions on how to install it along with development instructions. 
- [ ] **Contributing statement:** The package has a contributing.md file that details how to contribute to the package. 
- [ ] **Package overlap:** That package doesn't fully overlap with functionality of other packages that have already been submitted to pyOpenSci
- [ ] **Archive** (JOSS only, may be post-review): The repository DOI resolves correctly
- [ ] **Version** (JOSS only, may be post-review): Does the release version given match the GitHub release (v1.0.0)?

```

### Responding to out-of-scope submissions

If the package is out-of-scope, the EiC should thank authors for their submission,
explain the reasons for the decision, and direct them to other publication venues 
if relevant. If further discussion is warranted that can take place within the issue. 
