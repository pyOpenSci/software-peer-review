# An Overview Of the Peer Review Process

## pyOpenSci open peer review steps
There are several components to the pyOpenSci peer review process. Below, we overview the entire process
from start to finish.

### Step 0. *optional* : Author submits pre-submission inquiry
A **presubmission inquiry** is useful if you are unsure whether your package
is in scope. To submit a pre-submission inquiry, open up an issue using the presubmission template in our [pyopensci/software-review repository](https://github.com/pyOpenSci/software-review/issues/new/choose/). During this time an Editor in Chief will review for scope and performs
basic checks for package infrastructure

- Estimated time: ~1-2 weeks

**Below, are the basic checks that your package should have prior to being
submitted for peer review.** These are the checks that an Editor in Chief or
and editor will look at when evaluating your package for review.

```{include} /appendices/editor-in-chief-checks.md
```

### 1. Author submits their package for review

To do this, you open an issue using the software submission template in our
[pyopensci/software-review repository](https://github.com/pyOpenSci/software-review/issues/new/choose/).

### 2. Editor in Chief reviews package submission

The Editor in Chief will review your submission at this point for both package scope and minimal infrastructure criteria
(listed above).
- TIME ~2 weeks (or longer if editor requests changes that take the author longer to implement)

### 3. Editor finds reviewers for package
At this point if your package has the minimal infrastructure
requirements and is in scope the Editor in Chief will assign an editor
to review your package. That editor will then look
for reviewers.

Time: ~2-3 weeks

### 4. Peer review of submitted Python Package begins
Once we have an editor and 2 reviewers on board, review begins. **Reviewers have 3 weeks to return a review.** To do this
they will use our reviewer template in the [reviewer guide](/how-to/reviewer-guide.md) and paste that, filled out, into the issue.

TIME: ~3 weeks

### 5. Author responds to reviews

At this point the authors should respond to the review. We prefer that **authors
respond within 2 weeks of the submitted review**. We also understand that it may
take longer to actually implement the changes requested in the review. But we
request that authors respond to reviews to acknowledge
that they have seen them.

The reviewers are encouraged to open pull requests and issues to help the
maintainers update their package.

*Often there is some back and forth between reviewers and maintainers at this step.*

There is no specified duration for this period. Rather as long as all
parties are responsive within 2 weeks the review shall continue until the author has completed work addressing the reviews.

### 6. Package acceptance

Once the maintainers have completed updating the package, the assigned editor
will ask the reviewers if they are happy with changes made. At this point the
editor performs one last check on the package. And accepts it if that is appropriate.

Now, there are a few final cleanup activities including:

 * Adding the pyOpenSci peer-reviewed badge to the package README file.
 * Creating a new release on GitHub from the reviewed version.
 * Adding package authors and the package to the pyOpenSci website.

The package is now accepted into the pyOpenSci ecosystem!

### JOSS submission

JOSS refers to the [Journal of Open Source Software](https://joss.theoj.org/). If the maintainer wishes, and their package is within JOSS' scope, they can now
be fast tracked through the JOSS review process (another review is not required
for this step).

## Peer review guides

If you want to learn more about each step listed above, we suggest that you read
through the peer-review guides below that are tailored to each role in the peer review process:


::::{grid} 1 1 1 2
:class-container: text-center
:gutter: 3

:::{grid-item-card} {octicon}`code-square;1.5em;sd-mr-1` Author / Maintainer Guide
:link: /how-to/author-guide
:link-type: doc
:class-header: bg-light

Learn everything that you need to know about the peer review  for **package maintainers** who submit a package to pyOpenSci for peer review.
+++
Learn more »
:::

:::{grid-item-card} {octicon}`pencil;1.5em;sd-mr-1` Editor Guide
:link: /how-to/editors-guide
:link-type: doc
:class-header: bg-light
+++

Learn about the process that editors follow in the pyOpenSci peer review
process.
+++
Learn more »
:::

:::{grid-item-card} {octicon}`codescan-checkmark;1.5em;sd-mr-1` Reviewer Guide
:link: /how-to/reviewer-guide
:link-type: doc
:class-header: bg-light

Click here to read more about the process that reviewers take when reviewing
a Python package for pyOpenSci.

+++
Learn more »
:::

:::{grid-item-card} {octicon}`pencil;1.5em;sd-mr-1` ✨ Editor in Chief Guide
:link: /how-to/editor-in-chief-guide
:link-type: doc
:class-header: bg-light

The Editor in Chief is a rotating position within pyOpenSci held by members
of the pyOpenSci editorial board. Learn more about the processes involved with
being an editor in chief for pyOpenSci.
+++
Learn more »
:::

::::
