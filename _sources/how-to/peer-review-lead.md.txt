# Peer Review Lead Guide

:::{tip}
There are several resources that will help you with this role.
Make sure that you have access to the:

* shared Google folder that contains a list of editors and reviewers who have recently signed up to participate in our review process
* Check out our [peer review status dashboard](https://www.pyopensci.org/metrics/peer-review/peer-review-status-dashboard.html) for the state of peer review
* [Check out our editorial dashboard](https://www.pyopensci.org/metrics/peer-review/editorial-dashboard.html) to get a sense of how many of our editors are busy, and who might be available to lead a review.
* Check out the current review status for the [current state of peer review](https://www.pyopensci.org/metrics/peer-review/current-review-status.html)
:::


The Peer Review Lead is responsible for keeping the software review process moving forward. They are responsible for:

* Keeping the review process moving forward by checking in on stalled reviews and supporting the editorial team.
* Ensuring a diverse and active editorial board.
* Onboarding and offboarding new editors.
* Making updates to the [pyOpenSci Software Peer Review Guide](https://www.pyopensci.org/software-peer-review/) as needed.
* Updating [software peer review policies](https://www.pyopensci.org/software-peer-review/our-process/policies.html) as needed.
* Helping editors find reviewers as necessary.

This role will also help manage conflicts that may arise in the software peer review process.

:::{note}
The pyOpenSci Executive Director has historically held the lead role in peer review. However, we are transitioning this role to a stipend position, which a community volunteer with excellent organizational and communication skills will hold.

Ideally, this person has experience with our peer review process as an editor or has been part of our community for some time and is familiar with the process.
:::

## How to keep peer review moving forward

A volunteer editorial team runs software peer review; it also relies on volunteer community reviewers. As with any volunteer-led effort, it is common for the review process to stall or slow down.

As Peer Review Lead, you should monitor the status of reviews and help editors move stalled reviews forward. Our [review status dashboard](https://www.pyopensci.org/metrics/peer-review/current-review-status.html) will help you stay informed about the overall review process.

Ideally, you should check in on peer reviews weekly or every other week, depending on the volume of reviews submitted. We anticipate that your time allocation in this role will be 4-8 hours a month. Some months may require additional hours if we are working on new policies. Others you may simply be checking in on the review process.

Keep an eye on a few things when you check in:

### 1. Dashboard: check the date the comment date for every review

Before you begin, ensure the peer review dashboard is up to date. At the top of the dashboard, you will see the **Last Updated** date. The metrics repository has a cron job that runs weekly to update review status metrics. If the date at the top of the page is older than 1-2 weeks, likely, a pull request, [similar to this one](https://github.com/pyOpenSci/metrics/pull/147) needs to be merged. Go ahead and merge that PR if one exists. If the dashboard date is old and there is no open PR to merge, our cron job has likely failed. In that case, please leave a note in our Slack `#pyos-infrastructure` channel. Our infrastructure lead can investigate and resolve any issues that arise with our build.

:::{image} /images/peer-review-metrics-dashboard.png
:alt: Dashboard last updated date
:::

### 2. Check in on prereview checks

Next, check in on the prereview checks by sorting the [all-open-reviews table](https://www.pyopensci.org/metrics/peer-review/current-review-status.html#all-open-reviews) table on the **Active_Status** column. Sometimes our Editor in Chief becomes overwhelmed with too many submissions at once. It's easy to forget that they are also able to [delegate the prereview checks to another editor on the team](pre-review-checks) if they fall behind. You can remind them and even help them find other editors to step in if needed.

### 3. Identify and check in on stalled reviews

The [All Open Reviews](https://www.pyopensci.org/metrics/peer-review/current-review-status.html#all-open-reviews) section of this page will also help you keep tabs on the current activity status of our reviews.

Check out the **The last date a comment was left on a review.** You can sort the table by this column to see the date that someone last commented on the issue.

If a review has been quiet for over a month, it's a good idea to check in on things. You can either leave a note on the issue to see if anyone responds (this is ideal, as you can then track when someone responds to the issue or if you were the last person to respond!). If momentum is not gained by leaving a note for the editor and reviewers on the issue, then follow up with the editor in Slack after 2 weeks to see if they need some support. If Slack doesn't work normally, email works as a last attempt to connect with the editor.

Also, check out the days open column. Keep an eye out for reviews that have been open for longer than 6 months. In some cases, you may want to check in with the editor to see how things are going and whether there is a way to move the review forward.

In some cases a review hasn't moved forward because the editor is struggling to find reviewers. [This page](finding-reviewers) will help you with some tips on helping an editor find reviewers. Sometimes this is as easy as posting in our pyOpenSci #software-review channel. Other times we might need to run a call for reviewers.

### 4. Check the reviews seeking editors section

The [**Editors Needed** section of the dashboard](https://www.pyopensci.org/metrics/peer-review/current-review-status.html#editors-needed) is useful for you to check in and see how the Editor in Chief (EiC) is doing. In some cases, the Editor in Chief needs support in onboarding a new editor. If packages are seeking editors for more than a month, it's time to check in. Sometimes, all that is needed is for the package to have an editor, but the YAML at the top of the issue hasn't been filled out properly. This is an easy fix - just add the editor to the `editor:` field at the top of the issue. In other cases, we may need to run a call for more editors. In that case, you can consult
    * Post in the software-review channel to see if anyone in our Slack community is interested in stepping into an editorial role
    * Please reach out to the Executive Director about posting on social media to find a new editor to join our team. [The editorial signup form can be found here](https://forms.gle/VEUxEzN6YmeWSb6t8), and the responses (names, emails, and domains only) to that form can be provided to you by the Executive Director upon request. It's not publicly shared to maintain the privacy of those who sign up to volunteer with us.
