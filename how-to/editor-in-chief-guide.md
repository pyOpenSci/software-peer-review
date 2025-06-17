# Editor in Chief Guide

:::{admonition} Useful pyOpenSci resources
:class: tip

Here are some helpful resources to support you in your Editor in Chief role:

* [**Python Package Guide**](https://www.pyopensci.org/python-package-guide/):
  A community-developed guide offering an overview of the Python packaging
  ecosystem, plus tutorials for building and publishing a package.
* [**pyOpenSci metrics dashboard**](https://www.pyopensci.org/metrics/):
  View the current state of peer reviews and track review activity over time.
* [**pyOpenSci Python package template**](https://github.com/pyOpenSci/python-package-template):
  A Copier-powered template for creating a new Python package that follows
  pyOpenSci best practices.
:::

## Editor in Chief (EiC) role & responsibilities

The Editor in Chief (EiC) is a rotating position, typically selected from the
current editorial team. It may also be held by a member of the broader
pyOpenSci community who is familiar with our organization and software peer
review.

The EiC term lasts **3 to 6 months**, or another duration agreed upon with the
Peer Review Lead. If the EiC needs to step down early, we request at least
**two weeks’ notice** to allow time to identify and onboard a replacement.

The Editor in Chief fulfills the  roles discussed below:

### 1. Manage incoming reviews

* Watch all issues in the
  [software-review repo](https://github.com/pyOpenSci/software-review/issues)

:::{tip}
Enable GitHub notifications and join the `#feed-software-review` Slack channel
to stay up to date on new submissions.
:::

* Perform the **initial editor checks** on new submissions using the
  [editor checklist](pre-review-checks).
* Flag scope or overlap concerns. Raise questions by tagging editors in
  `#software-review` or, if needed, in `#private-editorial-team`.
* Assign submissions to handling editors based on:
  - subject matter fit
  - editor availability

> The EiC may assign a package to themselves if they have capacity and want to
> lead the review.

### 2. Manage pre-submission inquiries

* Respond to pre-submission inquiries and help assess scope or structure in
  the `#software-review` Slack channel.
* Handle or delegate review referrals from the Journal of Open Source Software
  (JOSS) or other partners.

### 3. Monitor review progress

Check the status of active reviews **monthly**. Use the
[peer review dashboard](https://www.pyopensci.org/metrics/peer-review/peer-review-status-dashboard.html)
to identify stalled reviews or submissions needing editors or reviewers.

The dashboard highlights:

* Packages still seeking reviewers
* Packages needing an editor
* Open pre-submission inquiries
* Stale issues with no recent comments

If a review has been inactive for 3–4 weeks, message the editor in Slack to
check in. You or the peer review lead can help move things forward. If needed,
discuss in the `#private-editorial-team` channel.

:::{tip}
Need help unblocking a review? Contact the acting peer review lead (currently
the Executive Director of pyOpenSci).
:::

### 4. Monitor package maintenance

Once or twice during your term, review our list of accepted packages and flag
any that appear unmaintained. If needed, follow the
[archiving process](https://www.pyopensci.org/software-peer-review/our-process/policies.html#package-maintenance-and-maintainer-responsiveness).

### 5. Support EiC transition

As your term nears its end, discuss with the peer-review lead the process of identifying your successor.
Set a calendar reminder 2–3 weeks in advance to start the transition process.

:::{note}
See [this section](#responding-to-out-of-scope-submissions) for guidance on
responding to out-of-scope pre-submissions.
:::

:::{note}
If the EiC has limited time to handle pre-review checks for a package, a conflict of interest, or lacks relevant expertise, they may ask another editor to perform initial checks on a package at any time.
:::

## Editor in Chief checklist

When a new package is submitted for review, the Editor in Chief should:

### 1. ✔️ Tag the issue with the `0/pre-review-checks` label in GitHub

### 2. ✔️ Add a partner tag if the author selected a partner affiliation

pyOpenSci supports
[partnerships with other communities](partner-communities). Astropy is our only active partner.

If the author selects a partner in the submission template,

1. Notify an editor from that community that a review may be forthcoming. — they will typically take
the lead on that review.
2. Add the appropriate partner label to the issue.

The partner section of the submission looks like this:

```markdown
## Community Partnerships
If your package is associated with an
existing community, please check below:

- [ ] Astropy:[My package adheres to Astropy community standards](https://www.pyopensci.org/software-peer-review/partners/astropy.html)
- [ ] Pangeo: My package adheres to the [Pangeo standards listed in the pyOpenSci peer review guidebook][PangeoCollaboration]
```

(pre-review-checks)=
### 3. ✔️ Add the pre-review checks to the issue

:::{important}
Post your complete pre-review/editor checks in **one single comment**, rather than in multiple
comments. This keeps the review easy to follow and lets the author address
everything at once.

Before posting:

1. Review the editor-in-chief checklist.
2. Estimate how long the checks might take and share that with the author.
3. Perform all checks locally.
4. Post the completed checklist and any feedback in a **single GitHub comment**.
:::

Copy the template below and add it to the issue.

These checks confirm that the package meets the **minimum standards for
review**. In many cases, going through this process improves the package itself.

The EiC may ask another editor to complete the checks if:
* They are overwhelmed with new submissions.
* They are temporarily unavailable.
* Another editor has relevant domain or technical expertise.

(editor-checklist-template)=
### Editor-in-chief checklist

Copy the template below and use it in the review issue.

```{include} ../appendices/editor-in-chief-checks.md
```

### 4. ✔️ Ensure that the package onboarding survey is complete

Use [this spreadsheet](https://docs.google.com/spreadsheets/d/1jEk-DDpkz14Z07OX_o1cN2vHzVbJO6mQ83ihGXsWkLc/edit?gid=930774086#gid=930774086)
to check whether the author—and ideally all maintainers—have completed the
pre-review survey. You can search using their GitHub handle.

Thank the author for completing the survey. While some sections are optional,
we do need contact information to follow up about package maintenance. The
survey also helps us track and improve our peer review process.

### 5. ✔️  Assign an editor and add the `1/editor-assigned` label to the GitHub issue

Once the package is determined to be in scope, the pre-review surveys are complete, and pre-review checks
are done, it's time to assign an editor.

Use the [editorial dashboard](https://www.pyopensci.org/metrics/peer-review/editorial-dashboard.html)
to check which editors are currently available.

Once you’ve selected an editor:

1. Assign the issue to them in GitHub
2. Update the YAML at the top of the issue with their GitHub username
3. Add the `1/editor-assigned` label to the issue

:::{note}
If no current editor with relevant expertise is available, work with the peer
review lead to recruit a guest editor or onboard someone new.

Follow the [onboarding guide](onboarding-guide.md), and complete the full
[onboarding process](onboarding-a-new-editor) to ensure they have:

* GitHub access
* Slack access
* Everything needed to manage the review

See the [editor guide](editors-guide.md) for more on an editor’s responsibilities. Once the editor is assigned, your
work on the review is complete and they will now begin identifying reviewers.

:::


:::{admonition} Diversity in the editorial & reviewer  team is important
:class: important

Inclusion is core to the pyOpenSci mission. It's important to have an
editorial team comprised of an editor + 2 reviewers from different backgrounds and identities to enrich the review process.

As you select an editor (and guide that editor in finding reviewers),
seek diversity in the team supporting package review. [Specifically, reviewers and the editor should have a mix of gender identities whenever possible](reviewer-diversity). pyOpenSci [also supports mentoring new reviewers and editors if needed!](review-mentorship)

:::

### 6. ✔️ Update the YAML header

After assigning the editor to the issue and adding the `1/editor-assigned` label:

* Update the YAML at the top of the issue with the editor’s GitHub username
* Add any final comments to the bottom of your pre-review checklist comment

:::{important}
Be sure to update both the **GitHub assignment** and the **YAML header** with the editors name. Our peer
review dashboard depends on both!
:::

## A note about submissions that are incomplete or vague

Sometimes a submission lacks enough information to assess whether it’s in
scope. For example:

* Online documentation is sparse
* The README is minimal or unclear
* There’s no documentation structure
* The YAML template at the top of the issue is incomplete

In these cases, ask the author for more information. Even if the package is
ultimately out of scope, this will still help improve its documentation.

You can adapt the message below when requesting more details:

```markdown
Hello <username>, and thank you for your submission!

We are reviewing whether your package fits within pyOpenSci’s scope and
could use a bit more information.

Please expand your `README` to give more context. After reading it, someone
without domain expertise should understand the package’s goals, use cases,
and core functionality.

<optional>
If your package overlaps with others, please explain in the README and in
this issue how your package is "best in class." You can refer to our
[guidance on package overlap](https://www.pyopensci.org/software-peer-review/about/package-scope.html#package-overlap).
</optional>

```

## Responding to out-of-scope submissions

If a package is determined to be out of scope, thank the author for their
submission, briefly explain why it is not in scope, and suggest other venues
for review if relevant.

Keep the conversation respectful and clear. If the author has questions,
continue the discussion in the GitHub issue.

## Stepping down from the EiC role

As your term ends, help onboard the next Editor in Chief.

* Set a calendar reminder 2–3 weeks before your term ends and begin to communicate with the incoming editor-in-chief about the transition.
* Craft a summary of where peer review is, and where the incoming Editor in Chief will need to pick up.
* Let the peer review lead know that a transition is coming soon so they can support as needed.
* If you can, try to be available after your term has ended to answer questions and support a smooth transition for the new editor in chief


:::{important}
If you are leading any active reviews as EiC, you must hand them off to the
incoming Editor in Chief before stepping down. This ensures continuity and
prevents reviews from stalling.
:::

The new EiC assumes full responsibility for all active reviews and
pre-submission inquiries previously managed by the outgoing EiC.

### Share your reflections

Before stepping down, write a summary of:

* What went well
* What could be improved
* Any challenges or ideas you’d recommend to future EiCs

Post your reflection in the `#private-editorial-team` Slack channel or share it with
the peer review lead directly.
