# Policy for use of generative AI / LLMs

::::{admonition} How this policy was developed
::class: important

The Generative AI policy below was co-developed by the pyOpenSci community. Its goals are:

* To **acknowledge the widespread use of Generative AI tools** (LLMs) and promote transparency and responsible use that ensures better software outputs that support sound open source development practices.
* **Ensure equitable balance of effort in peer review** — authors are responsible for human review of AI-generated content before submission; our volunteer reviewers are not responsible for identifying and/or correcting machine-generated errors or issues.
* **Protect volunteer reviewers** from being the first line of review for generated code.
* Give reviewers and editors the information they need to make informed decisions about what they choose to review.
* **Support and promote packages that follow sustainable software practices** that enable future discovery and uphold the foundational principles of scientific open source.
* Raise awareness of the broader challenges Generative AI presents to the scientific open source community.
* To promote transparency and privacy in user data

[Please see this GitHub issue for a discussion of the topic.](https://github.com/pyOpenSci/software-peer-review/issues/331)

In generating our Generative AI policy, we acknowledge some of the other policies in the open source ecosystem that inspired our work here, including:

* [FastAPI docs](https://fastapi.tiangolo.com/contributing/#automated-code-and-ai)
* [JOSS AI Policy](https://blog.joss.theoj.org/2026/01/preparing-joss-for-a-generative-ai-future)
* [Scikit-Learn Policy](https://scikit-learn.org/dev/developers/contributing.html#automated-contributions-policy)
* [Melissa Mendonça’s Collection of GenAI Policies](https://github.com/melissawm/open-source-ai-contribution-policies)

::::

## Generative AI and open source development

We understand and support your use of Generative AI tools to improve software development workflows and to make your developer workflows more efficient. We want you to use them thoughtfully and effectively, and in ways that improve both the open source ecosystem and your development trajectory.

We expect that all code and documentation submitted to our peer review process should have meaningful human review, intervention, judgment, and context. We understand that the use of current Generative AI tools is often tightly woven into development workflows, making disclosure challenging. But **we still require disclosure** to support both transparency and to allow reviewers and editors to understand what they are reviewing.

The policies below support adherence to thoughtful open source development best practices. A pyOpenSci package submission should demonstrate both need and sustained value to the research community. **Short-lived, single-use codebases are out of scope for pyOpenSci.**

## Communication in review issues

* We prefer that all communication in our software review issues are written by a human. We embrace the use of LLMs for translation and grammar correction. We prefer honest interactions over ones that prioritize perfect language and grammar. As little aid from an LLM as possible.
* We will block accounts that spam our repositories or burden our volunteers with repeated, automated comments that aren't directly related to and in support of productive conversations in a review.

## Package development and design approach

* **Development History Timeline:** Projects should have at least **3-6 months of public development history**, with evidence of releases, public issues, and pull requests that reflect **iterative, thoughtful development** rather than rapid and recent code generation.
* If the human effort put into the package is less than the effort required to review it, please don't submit the package.
* Software should be developed openly, rather than developed in private and then moved to a public repository with an OSI-approved license to meet minimal open source requirements.
* **Development History Approach:** We encourage thoughtful development history and patterns, including tightly scoped commits with clear commit messages that follow iterative development best practices, rather than large commits that address multiple issues in a package and affect large volumes of files throughout the package. These workflows signal careful design and development, and changes to a codebase that could be reviewed by a human.
* Projects with very short, rapid development timelines (weeks to a few months) will face higher scrutiny by our review teams than those that have a significant development history (more than 6 months)
* **Package Scope & Design:** We value packages with a thoughtful, well-scoped design. When submitting, we will ask you to describe the key design decisions behind your package — the tradeoffs you considered and why you built it the way you did.
* We place greater value on packages that have been adopted or used by a wide user base, since this demonstrates that the package has design and performance characteristics that meet multiple use cases.
* Be sure to situate your package within the broader Python ecosystem: identify related tools, explain how your package differs from them, and explain how it complements, extends, or builds upon them.
* We particularly value **work that builds upon or extends existing tools rather than reinventing solutions** where quality alternatives already exist.

Below is the checklist that you will need to respond to in our submission form:

```{include} ../appendices/gen-ai-checklist.md

```
