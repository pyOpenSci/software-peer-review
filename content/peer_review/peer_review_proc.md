# Peer Review Process and Policies

## Review Timeline
- *Pre-submission:* If you are unsure if your package fits within the scope of the pyOpenSci suite, create a pre-submission inquiry issue on the pyopensci/software-review repository. An editor will respond within a few days to let you know if we can review your package at this time. For more info, see "Aims and Scope" below. 
- To submit a package for review, the author must initiate a review request in the pyopensci/software-review repo. 
- An editor will review your submission within **1 week** and respond with next steps. The editor may assign the package to reviewers, request that the package be updated to meet minimal criteria before review, or reject the package due to lack of fit or overlap.
- If your package meets minimal criteria, the editor will assign 1-3 reviewers. They will be asked to provide reviews as comments on your issue within **3 weeks**.
- We ask that you respond to reviewers’ comments within **2 weeks** of the last-submitted review, but you may make updates to your package or respond at any time. Here is an author response example. We encourage ongoing conversations between authors and reviewers. See the reviewing guide for more details.
- Once your package is approved, we will provide further instructions about the transfer of your repository to the pyOpenSci repository.

## Review Process Guidelines
- Packages are reviewed for quality, fit, documentation, clarity and the review process is quite similar to a manuscript review (see our packaging guide and reviewing guide for more details). Unlike a manuscript review, this process will be an ongoing conversation.
- Once all major issues and questions, and those addressable with reasonable effort, are resolved, the editor assigned to a package will make a decision (accept, hold, or reject). Rejections are usually done early (before the review process begins, see the aims and scope section), but in rare cases a package may also be not onboarded after review & revision. It is ultimately editor’s decision on whether or not to reject the package based on how the reviews are addressed.
- Communication between authors, reviewers and editors will first and foremost take place on GitHub, although you can choose to contact the editor by email. When submitting a package, please make sure your GitHub notification settings make it unlikely you will miss a comment.
- The author can choose to have their submission put on hold (editor applies the holding label). The holding status will be revisited every 3 months, and after one year the issue will be closed.
- If the author hasn’t requested a holding label, but is simply not responding, we should close the issue within one month after the last contact intent. This intent will include a comment tagging the author, but also an email using the email address listed in the DESCRIPTION of the package which is one of the rare cases where the editor will try to contact the author by email.
- If a submission is closed and the author wishes to re-submit, they’ll have to start a new submission. If the package is still in scope, the author will have to respond to the initial reviews before the editor starts looking for new reviewers.

## Aims and Scope
pyOpenSci aims to support Python packages that enable reproducible research and managing the data lifecycle for scientists. Packages submitted to pyOpenSci should fit into one or more of the categories outlined below. If you are unsure whether your package fits into one of these categories, please open an issue as a pre-submission inquiry. We will let you know if we are able to review it at this time.

**Note:** pyOpenSci is young and this list is tentative. If your scientific Python package does not fit into one of the categories, we'd encourage you to open a pre-submission inquiry.

### Package Categories
- **Data retrieval:** Packages for accessing and downloading data from online sources. Includes wrappers for accessing APIs.
- **Data extraction:** Packages that aid in retrieving data from unstructured sources such as text, images and PDFs.
- **Data munging:** Tools for processing data from scientific data formats.
- **Data deposition:** Tools for depositing data in scientific research repositories.
- **Data visualization:** Packages for visualizing and analyzing data. 
- **Reproducibility:** Tools to scientists ensure that their research is reproducible. E.g. version control, automated testing, or citation tools.
- **Geospatial:** Packages focused on the retrieval, manipulation, and analysis of spatial data.
- **Education:** Packages to aid with instruction.
- **Statistics/Machine Learning:** Packages implementing established ML or statistics methods. Note that this does not include *new* methods, only implemntations of previously published algorithms/techniques.

### Package Overlap
pyOpenSci encourages competition among packages, forking and re-implementation as they improve options of users overall. However, as we want packages in the pyOpenSci suite to be our top recommendations for the tasks they perform, we aim to avoid duplication of functionality of existing Python packages in any repo without significant improvements. A Python package that replicates the functionality of an existing package may be considered for inclusion in the pyOpenSci suite if it significantly improves on alternatives by being:

- More open in licensing or development practices
- Broader in functionality (e.g., providing access to more data sets, providing a greater suite of functions), but not only by duplicating additional packages
- Better in usability and performance
- Actively maintained while alternatives are poorly or no longer actively maintained

These factors should be considered as a whole to determine if the package is a significant improvement. A new package would not meet this standard only by following our package guidelines while others do not, unless this leads to a significant difference in the areas above.

We recommend that packages highlight differences from and improvements over overlapping packages in their README and/or vignettes.

We encourage developers whose packages are not accepted due to overlap to still consider submittal to other repositories or journals.


## After Acceptance: Package Ownership and Maintenance

Authors of contributed packages essentially maintain the same ownership they had prior to their package joining the pyOpenSci suite. Package authors will continue to maintain and develop their software after acceptance into pyOpenSci. Unless explicitly added as collaborators, the pyOpenSci team will not interfere much with day to day operations. However, the team may intervene with critical bug fixes, or address urgent issues if package authors do not respond in a timely manner (see the section about maintainer responsiveness).

### Quality Commitment
pyOpenSci strives to develop and promote high quality research software. To ensure that your software meets our criteria, we review all of our submissions as part of the Software Peer Review process, and even after acceptance will continue to step in with improvements and bug fixes.

Despite our best efforts to support contributed software, errors are the responsibility of individual maintainers. Buggy, unmaintained software may be removed from our suite at any time.

### Maintener Responsiveness
If package maintainers do not respond in a timely manner to requests for package fixes, we will remind the maintainer a number of times, but after 3 months (or shorter time frame, depending on how critical the fix is) we will make the changes ourselves.

Should authors abandon the maintenance of an actively used package in our suite, we will consider petitioning PyPI to transfer package maintainer status to pyOpenSci.

### Requesting Package Removal
In the unlikely scenario that a contributor of a package requests removal of their package from the suite, we retain the right to maintain a version of the package in our suite for archival purposes.

## Community Code of Conduct
- We are committed to providing a friendly, safe and welcoming environment for all, regardless of gender, sexual orientation, disability, ethnicity, religion, or similar personal characteristic.
- Please avoid using openly sexual nicknames or other nicknames that might detract from a friendly, safe and welcoming environment for all.
- Please be kind and courteous. There’s no need to be mean or rude.
- Respect that people have differences of opinion and that every design or implementation choice carries a trade-off and numerous costs. There is seldom a right answer.
- Please keep unstructured critique to a minimum. If you have solid ideas you want to experiment with, make a fork and see how it works.
- We will exclude you from interaction if you insult, demean or harass anyone. That is not welcome behavior. We interpret the term “harassment” as including the definition in the Citizen Code of Conduct; if you have any lack of clarity about what might be included in that concept, please read their definition. In particular, we don’t tolerate behavior that excludes people in socially marginalized groups.
- Private harassment is also unacceptable. No matter who you are, if you feel you have been or are being harassed or made uncomfortable by a community member, please contact us at earth.lab@colorado.edu immediately with a capture (log, photo, email) of the harassment if possible. Whether you’re a regular contributor or a newcomer, we care about making this community a safe place for you and we’ve got your back.
- Likewise, any spamming, trolling, flaming, baiting or other attention-stealing behavior are not welcome.
- Avoid the use of personal pronouns in code comments or documentation. There is no need to address persons when explaining code (e.g. “When the developer”). The focus should be on the code, not the author.
