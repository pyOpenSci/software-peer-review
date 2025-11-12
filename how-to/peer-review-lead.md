# Peer Review Lead Guide

The Peer Review Lead is responsible for overseeing the entire software review process. They keep the process moving forward, onboard editors, and identify and help with stalled reviews. They are responsible for:

* Ensuring a diverse and active editorial board
* Onboarding and offboarding new editors
* Maintaining the [pyOpenSci Software Peer Review Guide](https://www.pyopensci.org/software-peer-review/)
* Updating [software peer review policies](https://www.pyopensci.org/software-peer-review/our-process/policies.html) as needed
* Helping editors find reviewers as necessary.

This role will also help manage conflicts that may arise in the software peer review process.

:::{note}
The pyOpenSci Executive Director has historically held the lead role in peer review. However, we are testing out the role becoming a stipend position held by a community volunteer with excellent organizational and communication skills.

Ideally, this person has experience with our peer review process as an editor or has been part of our community for some time and is familiar with the process.
:::

## How to keep peer review moving forward

A volunteer editorial team runs software peer review; it also relies on volunteer community reviewers. As with any volunteer-led effort, it is common for the review process to stall or slow down.

As Peer Review Lead, you should monitor the status of reviews and help editors move stalled reviews forward. Our [review status dashboard](https://www.pyopensci.org/metrics/peer-review/current-review-status.html) will help you stay informed about the overall review process.

Keep an eye on a few things here:

1. At the top of this page, you will notice the **Last Updated** date. The metrics repository has a cron job that runs weekly to update review status. If the date at the top of the page is older than 1-2 weeks, likely, a pull request, [similar to this one](https://github.com/pyOpenSci/metrics/pull/147) needs to be merged. If that date is old and there is no open PR to merge, our cron job has likely failed. In that case, please leave a note in the `#pyos-infrastructure` channel in our Slack. Our infrastructure lead can investigate and resolve any issues that arise with our build.
3. The [All Open Reviews](https://www.pyopensci.org/metrics/peer-review/current-review-status.html#all-open-reviews) section of this page will also help you keep tabs on
    * **The last date a comment was left on a review.** You can filter the table by last comment date and see who left the last comment. If a review has been quiet for over a month, it's a good idea to check in on things. You can either leave a note on the issue to see if anyone responds (this is ideal, as you can then track when someone responds to the issue or if you were the last person to respond!). If momentum is not gained by leaving a note for the editor and reviewers on the issue, then follow up with the editor to see if they need some support.
    * How many days each review has been open for: Keep an eye out for reviews that have been open for longer than 6 months. In some cases, you may want to check in with the editor to see how things are going.
4. **Reviews seeking editors:** The **reviews seeking editors** section is useful for you to check. In some cases, the Editor in Chief needs support in onboarding a new editor. If packages are seeking editors for more than a month, it's time to check in. Sometimes, all that is needed is for the package to have an editor, but the YAML at the top of the issue hasn't been filled out properly. This is an easy fix - just add the editor to the `editor:` field at the top of the issue. In other cases, we may need to run a call for more editors. In that case, you can consult
    * Post in the software-review channel to see if anyone in our Slack community is interested in stepping into an editorial role
    * Consult with the Executive Director about posting on social media to find a new editor to join our team.  [The editorial signup form can be found here](https://forms.gle/VEUxEzN6YmeWSb6t8) and the responses (names emails and domains only) to that form can be provided to you by the Executive Director upon request!
