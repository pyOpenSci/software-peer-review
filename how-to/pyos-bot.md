# pyOS Bot

This page walks you through how the pyosBot supports the pyOpenSci
peer review process.

## A new submission or presubmission inquiry is submitted

When a new submission is created on the pyOpenSci software-submission
github repository, the bot performs the following steps:

* It welcomes the author with a friendly message that pulls the submittor's name from (I think the header)

```md
Hey @lwasser 👋 Welcome to pyOpenSci’s scientific Python peer review process!

We’ve seen your message. Someone from our editorial team will get back to you within the next week about this submission.
In the meantime, feel free to check out our packaging guide or feel free to ask questions on our Discourse forum.
```

Also:

* The issue is by default tagged with `new submission!!` Or `pre-submission` based on the issue template that the author selects.
* A [CI workflow](https://github.com/orgs/pyOpenSci/projects/7/workflows) runs that automagically adds the issue to our [pyOpenSci peer review project board](https://github.com/orgs/pyOpenSci/projects/7).

:::{todo}
I am putting things in the todo box that require us to modify our review template and process.

* Checks for specific missing fields in the issue
* Post a comment identifying what is missing

```yaml
   initial_values:
     values:
       - version-submitted
       - target-repository
       - author-handle
```
:::



:::{TODO}
add message we want here
:::

:::{figure} /images/pyosbot/new-submission-welcome.png
:scale: 50 %
:alt: Add alt....

Interacting with the pyosBot after an initial submission.

:::


## Step 2 - start pre-review checks checks

Next, it's time to begin the pre-review checks.
For the time being, you can update the EiC that is running the review manually

:::{TODO}
When we have the submission template in place, we can use this comment.

`@botname set @lwasser as eic`

### Outcomes:
Updates the EIC field at the top of the issue using a set value responder
If you run this again with the same command but a different user it updates the field to the new user.
:::

To begin the prereview stage, use the command:

`@pyosbot start prereview`

This command:

* Adds a comment with the [pre-review checks template](https://github.com/pyOpenSci/software-peer-review/blob/main/appendices/editor-in-chief-checks.md) to the issue as a comment.
* Updates ISSUE LABELS as follows:
    * Removes `New Submission!` label and
    * Replaces with `0/pre-review-checks`

:::{todo}
We could include the pre-review-checks template as an inline embed the file here using sphinx!
:::



:::{todo}
Add image of the command & output

:::


## Step 3: EiC Assigns editor to review

* Bot assigns editor as an assignee to the issue (I added add_collaborator to this responder to ensure they have permissions as a collaborator in the repo)
* Bot fails quietly if user assigned does not have repository collaborator permissions see docs.

:::{note}
If the bot can't assign the github user to the issue, you must add them to the pyOpenSci peer review GitHub team.
:::

:::{todo}
Step 3: EiC Assigns editor to review
@pyosbot add @chayadecacao as editor
Outcomes:
Bot adds editor name to yaml header (see image below)
Bot assigns editor as an assignee to the issue (I added add_collaborator to this responder to ensure they have permissions as collaborator in the repo)
Bot fails quietly if user do not have repository collaborator permissions see docs but this shouldn’t be a problem.

https://github.com/pyOpenSci/software-peer-review/blob/main/appendices/editor-initial-response-template.md

Bot updates the `yaml` header at the top of the issue with the editor name

TODO: We could modify this step for now to only assign the issue and change the label /
:::

### Step 3.1: Remove an editor


To remove an editor, you can call:

`@pyosbot remove editor`

* Bot removes the previous editor from the GitHub issue assignee field

:::{todo}
* REMOVED: Bot removes editor from the issue metadata (top of the issue)
:::

## Step 4: Editor Finds & Assigns reviewers & kicks off review
Now the editor takes over and begins the reviewer search
Ask the bot to change the state of the review:

`@pyosbot seeking reviewers`

* Bot changes label to `2/seeking-reviewers`
* Bot removes `1/editor-assigned`

:::{todo}
Requires issue header html comments

Step 4.2: Add reviewers to review issue header
@pyosbot add @lwasser as reviewer
NOTE: bot can’t handle more than one person at a time. So you have to add each reviewer individually
@pyosbot remove @lwasser as reviewer
If you wish to remove a reviewer from the issue

:::

## Step 4.3: Update labels Reviewers assigned
Once you have found reviewers, you can ask the bot to change the
label once again:

`@pyosbot reviewers assigned`

* Change the label to the next step in the process
* The label change triggers a project board update, moving the issue to the `under-review` column.

## Step 4.4: Post editor response template with review deadlines

`@pyosbot editor response`

Once reviewers are found, the review can begin. The command below will post the first editor template to the issue for the editor. The editor can manually add reviewers and the due date to the template as needed

* Please ensure that the author and maintainers have taken the pre-review survey. The spreadsheet for this check can be found in our private-editorial-team slack channel as a pinned message.


### TODO: I think we want to add a reminder for reviews in 2 weeks and then another in 3 weeks

## Step 5: reviews are in

Command: `@pyosbot reviews are in`

Action:
* Bot Changes label to `4/review-in-awaiting-changes`,


## Step 6: author response is in for both reviews

Command: `@pyosbot author response complete`

Actions:
* Bot changes label to: `5/awaiting-reviewer-response`

It also will remove any labels that haven't been removed from previous steps.


## Step 7: Accept package

`@pyosbot package accepted`

* Adds wrap up template text
*
Template text has the package-name embedded in the message as well as the submitting author github handle

https://github.com/pyOpenSci/software-peer-review/blob/main/appendices/package-approval-template.md

Change issue label to `6/pyOS-approved 🚀🚀🚀`. (remove previous labels)
Change project board status to pyos-accepted


Step 7 - JOSS steps – start JOSS review (optional)
@pyosbot begin joss
Change project board to under-joss-review
ADD Issue Label 7/under-joss-review (keep the pyos-approved label)
NOTE: remove extra label 8/joss-review-complete

Step 8 - JOSS steps – JOSS approved (optional)
@pyosbot joss accepted
Change project board to joss-accepted
Update issue label 9/joss-accepted (keep pyos-accepted label)



## Placing a review on hold

In some cases, a review stalls or needs to be placed on hold. In that case, you can call:

`@pyos-bot pause review`

This should be on-hold
Set label to `⌛ pending-maintainer-response`


If the package is out of scope -` pyos-bot out-of-scope`

Set issue label to: currently-out-of-scope

Move to project board out-of-scope


# Show our community Code of Conduct and Guidelines
@pyosbot code of conduct
