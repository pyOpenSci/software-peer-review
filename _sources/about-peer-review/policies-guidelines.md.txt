# Peer Review Guidelines & Policies

## Review Process Guidelines

- Packages are reviewed for quality, fit, documentation, clarity and the review process
  is quite similar to a manuscript review (see our [packaging guide](../authoring/overview)
  and [reviewing guide](../peer-review-guides/reviewer-guide) for more details). Unlike a
  manuscript review, this process will be an ongoing conversation.
- Once all major issues and questions, and those addressable with reasonable effort, are
  resolved, the editor assigned to a package will make a decision (accept, hold, or
  reject). Rejections are usually done early (before the review process begins, see the
  aims and scope section). In rare cases a package may also not be on-boarded after
  review & revision. It is ultimately editor’s decision on whether or not to reject the
  package based on how the reviews are addressed.
- Communication between authors, reviewers and editors will first and foremost take
  place on GitHub, although you can choose to contact the editor by email. When
  submitting a package, please make sure your GitHub notification settings make it
  unlikely you will miss a comment.
- The author can choose to have their submission put on hold (editor applies the holding
  label). The holding status will be revisited every 3 months, and after one year the
  issue will be closed.
- If the author hasn’t requested a holding label, but is simply not responding, we
  should close the issue within one month after the last contact intent. This intent
  will include a comment tagging the author, but also an email using the email address
  listed in the DESCRIPTION of the package which is one of the rare cases where the
  editor will try to contact the author by email.
- If a submission is closed and the author wishes to re-submit, they’ll have to start a
  new submission. If the package is still in scope, the author will have to respond to
  the initial reviews before the editor starts looking for new reviewers.

## Submitting your package for review in other venues

We strongly suggest submitting your package for review with pyOpenSci before:
 
*  publishing on `PyPI` or `conda`; 
*  submitting a software paper describing the package to a journal. 
 
Review feedback may result in major improvements and updates to your package, 
including changes that could be break package functionality. 

We do not consider previous publication on `PyPI` or `conda` or in other venues 
sufficient reason to not adopt reviewer or editor recommendations provided in 
our review.

>Please do not submit your package for review while it or an associated manuscript is 
> also under review at another venue, as this may result on conflicting requests 
> for changes from two sets of reviewers.

### Publication with Journal of Open Source Software (JOSS)
If you have previously published your software package with JOSS, you can still
submit it to pyOpenSci for review. This provides:

* Increased visibility of your package as a vetted tool within the scientific python ecosystem
* We will also keep in touch with you as a maintainer to support long term maintenance. If you need to step down from maintaining your package we will help find a new maintainer and/or help sunset the tool.

### Conflict of interest for reviews and editors
Following criteria are meant to be a guide for what constitutes a conflict of interest
for an editor or reviewer. The potential editor or reviewer has a conflict of interest
if:

- The authors with a major role are from the potential reviewer/editor’s institution or institutional component (e.g., department)
- Within in the past three years, the potential reviewer/editor has been a collaborator
  or has had any other professional relationship with any person on the package who has
  a major role
- The potential reviewer/editor serves as a member of the advisory board for the project under review
- The potential reviewer/editor would receive a direct or indirect financial benefit if the package is accepted
- The potential reviewer/editor has significantly contributed to a competitor project.
- There is also a lifetime COI for the family members, business partners, and thesis student/advisor or mentor.

In the case where none of the associate editors can serve as editor, an 
external guest editor will be recruited to lead the package review.

## After Acceptance: Package Ownership and Maintenance

Authors of contributed packages essentially maintain the same ownership they 
had prior to their package joining the pyOpenSci suite. Package authors will 
continue to maintain
and develop their software after acceptance into pyOpenSci. Unless explicitly added as
collaborators, the pyOpenSci team will not interfere with day to day operations.

If you need to step down from maintaining your accepted pyOpenSci package, please
please notify the EiC / software review lead of this as soon as you can. We 
will talk with you about your tool and work together to either find a new maintainer or sunset the tool depending upon what makes the most sense. 

We will reach out to our package maintainers each year to check in on how 
maintenance is going. 

### Maintainer Responsiveness
If package maintainers do not respond in a timely manner to requests for 
package fixes, we will remind the maintainer a number of times. After 3 months 
(or shorter time frame, depending on how critical the fix is) we will discuss 
the future of the package as a part of our pyOpenSci ecosystem. 

* If a package becomes completely un-maintained we will highlight that fact and 
remove it as a vetted tool in our ecosystem.
* If a sub-community decides to fork and maintain that package we are open to working with the new maintainers to keep the package within our ecosystem.

<!-- Should authors abandon the maintenance of an actively used package in our suite, 
we will consider petitioning PyPI to transfer package maintainer status to pyOpenSci. -->


```{note}
Note from the Executive Director: Please note that we are reviewing the text 
below and will be updating our policy 
surrounding package quality and long term maintenance in the upcoming weeks 
(Fall 2022).
```

### Quality Commitment
pyOpenSci strives to develop and promote high quality research software. To ensure that
your software meets our criteria, we review all of our submissions as part of the
Software Peer Review process. We expect that you will continue to maintain a 
package that has been accepted continually. 

Despite our best efforts to support contributed software, errors are the responsibility
of individual maintainers. Buggy, unmaintained software may be removed from our suite at
any time. We also ask maintainers that they get in touch with us if they do need 
to step down from maintaining a tool. 



### Requesting Package Removal
In the unlikely scenario that a contributor of a package requests removal of their
package from the suite, we retain the right to maintain a version of the package in our
suite for archival purposes.
