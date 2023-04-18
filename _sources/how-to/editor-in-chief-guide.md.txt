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

### 1. ✔️ Tag the issue with `1/editor-checks` tag in GitHub

### 2. ✔️ Add the editor checks to the issue

```{important}
It is important that this step occur in one post rather than a string of
conversational feedback that is more difficult to follow. This allows the author to address all issues at
one time. Thus the EIC should:

1. Review the checklist.
1. Give the author a rough estimate of how long the checks might take to complete.
1. Perform all of the checks locally.
1. When all of the above are complete, post the checklist with any feedback for the author in the issue. This should be one single post.
```

Copy the {ref}`template below <editor-checklist-template>`
and add it to the issue.

Editor checks ensure that the package has
the bare minimum requirements to initiate a review.
We hope that even the process of going through these checks will
improve the quality of the package.

In some situations, the editor-in-chief initial checks may be passed down to an editor as follows:

* If the Editor in Chief is overwhelmed with package submissions to evaluate.
* If the Editor in Chief simply is busy at the time and needs support with checks.
* If the Editor in Chief thinks that the checks might be better served if done by an Editor
(For instance, if a specific domain or technical expertise would support more effective checks).

(editor-checklist-template)=
### Editor-in-chief checklist

Copy the template below to use it in the issue.

```{include} ../appendices/editor-in-chief-checks.md
```

### 3. ✔️ Ensure that the package onboarding survey is filled out.

Thank the authors graciously for filling out our survey. They can
skip sections of it if they wish. We do need their contact
information to stay in touch about package maintenance. We also
want to track their experience with our review process and
organization.

### 4. ✔️ Assign an editor to the issue to manage the rest of the review

Once the package initial checks are complete, and it is determined that
the package is in scope for pyOpenSci review, the Editor in Chief will assign an
editor to the review issue.
This may involve finding a new (guest) editor
as described in the [onboarding guide](onboarding-guide.md).
If you as Editor in Chief do recruit a new editor,
be sure to complete all the onboarding steps described
[here](onboarding-a-new-editor) so that the new editor
has everything they need to manage the review,
such as GitHub permissions and access to the relevant channels
in the pyOpenSci Slack team.
The editor will now begin the process of finding reviewers
for the package.
[Check out the editor guide for more information on the process that an editor follows](editors-guide.md)

```{admonition} Diversity in the editorial & reviewer  team is important
:class: important

Diversity is core to the pyOpenSci mission. As such it's important to have an
editorial team comprised of an editor + 2 reviewers from diverse backgrounds.

As you select an editor (and guide that editor in finding reviewers),
ensure that there is diversity
in the team supporting package review. [Specifically reviewers and the editor should have a mix of gender-identities whenever possible](reviewer-diversity). pyOpenSci [also supports mentoring new reviewers and editors if needed!](review-mentorship)

```

### 5. ✔️ Update the YAML header of the issue

Once all of the above is complete, the Editor in Chief should:

* Add any comments to the bottom of your editor checks comment.
* Update the YAML in the issue's header with the editor assigned to the review.
* Add the tag `2/seeking-reviewer(s)` to the issue.

## A note about submissions that are incomplete or vague

In some cases:

* Online documentation of a package is sparse.
* README is minimal or hard to understand.
* No clear documentation setup.
* Elements of the YAML template at the top of the issue are not filled out.

This makes assessment of the package's scope much harder.
In this case, please ask the author for more information. Even if the package is deemed
out-of-scope, the package documentation will improve as a result of your questions.

Example text:

```markdown
Hello <username> and many thanks for your submission.

We are discussing whether the package is in scope and need a bit more
information.

Please add more details and context to your `README` file.
After reading it, someone with little domain knowledge should understand
the aim, goals and functionality of the package.

<optional>
If a package has overlapping functionality with other packages, we require you
to mention in your documentation (README) and in this issue [how it is "best in class"](https://www.pyopensci.org/software-peer-review/about/package-scope.html#package-overlap). Please add a more detailed comparison to the packages you mention in the README so we can evaluate?
</optional>

```

## Responding to out-of-scope submissions

If the package is determined to be out-of-scope, the Editor in Chief should
thank authors for their submission, explain the reasons for the decision, and
direct them to other publication venues if relevant. If further discussion is
warranted that can take place within the issue.
