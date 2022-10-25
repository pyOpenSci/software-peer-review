# An Overview Of the Peer Review Process

## pyOpenSci open peer review steps
There are several components to the pyOpenSci peer review process. Below, we overview the entire process
from start to finish.

### Step 1 *optional*: Author submits pre-submission inquiry:* 
A **presubmission inquiry** is wise to do if you are unsure of whether your package 
is in scope. To submit a pre-submission inquiry, open up an issue using the presubmission template in our [pyopensci/software-review repository](https://github.com/pyOpenSci/software-review/issues/new/choose/issues/new/choose). During this time an Editor in Chief will review for scope and performs 
basic checks for package infrastructure

- Estimated time: ~1-2 weeks


**These are the basic checks that your package should have prior to being submitted for peer review**

```{include} ../checks.md
```

### 2. Author submits their package for review

To do this, you open an issue using the software submission template in our
[pyopensci/software-review repository](https://github.com/pyOpenSci/software-review/issues/new/choose/issues/new/choose).

### 3. Editor in Chief reviews package submission

The Editor in Chief will review your submission at this point for both package scope and minimal infrastructure criteria 
(listed above) 
- TIME ~2 weeks (or longer if editor requests changes that take the author longer to implement)

### 3. Editor finds reviewers for package 
At this point if your package has the minimal infrastructure
requirements and is in scope the Editor in Chief will assign an editor 
to review your package. That editor will then look 
for reviewers.

Time: ~ 2-3 weeks

### 4. Once we had an editor and 2 reviewers on board, the review begins 
Reviewers have 3 weeks to return a review. To do this
they will use our reviewer template in the [reviewer guide](reviewer-guide.md) and past that, filled out, into the issue.

TIME: ~3 weeks 

### 5. Author response to reviews

At this point the authors should respond to the review. We prefer that authors
respond within 2 weeks of the submitted review. We also understand that it may 
take longer to actually implement the changes requested in the review. But we
request that authors respond to reviews to acknowledge
that they have seen them.

The reviewers are encouraged to open pull requests and issues in to help the 
maintainers update their package.

### 6. Often there is some back and forth between reviewers and maintainers at this step

There is no specified duration for this period. Rather as long as all 
parties are responsive within 2 weeks the review shall continue until the author has completed work addressing the reviews.

### 7. Package acceptance

Once the maintainers have completed updating the package, the assigned editor 
will ask the reviewers if they are happy with changes made. At this point the 
editor performs one last check on the package. And accepts it if that is appropriate.
 
 Now, there are a few final cleanup activities including adding a pyOpenSci
 badge to the package README file, and creating a new release on GitHub from the reviewed version. The package is
 now accepted into the pyOpenSci ecosystem!

### JOSS submission

JOSS refers to the [Journal of Open Source Software](https://joss.theoj.org/). If the maintainer wishes, and their package is within JOSS' scope, they can now
be fast tracked through the JOSS review process (another review is not required 
for this step).

If you want to learn more about each step listed above, we suggest that you read 
through the guides below:

* **[Authors Guide](author-guide):** If you are a **package maintainer** who is
interested in submitting a package to
pyOpenSci, check out the authors guide.
* **[Reviewers guide](reviewer-guide):** If you have volunteered to be a
**reviewer** for a pyOpenSci package, you will want to carefully read
through the reviewer guide for guidance on how we run our reviews. Thank you in
advance for volunteering your time to support open science and open source software!
* **[Editor guide](editors-guide):** Editors for pyOpenSci have previous
experience reviewing packages for pyOpenSci. The editor guide
will walk you through the best practices for the editor role.
* **[Editor in Chief guide](editor-in-chief-guide):** The Editor in Chief is a rotating position within pyOpenSci held by members of the
pyOpenSci editorial board.
