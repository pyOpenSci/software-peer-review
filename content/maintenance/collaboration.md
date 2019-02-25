# Collaboration Guide 

Note: pyOpenSci is still building out this section of our guidebook. Many of the examples come from rOpenSci. If you have suggestions for changes, check out the [GitHub repo](https://github.com/pyOpenSci/dev_guide).

## Make your repo contribution and collaboration friendly

### Code of conduct

We require that you use a code of conduct such as the [Contributor Covenant](http://contributor-covenant.org/) in developing your package.  You should document your code of conduct in a `CODE_OF_CONDUCT` file in the package root directory, and link to this file from the `README` file.

### Contributing guide

We have a template contributing guidelines in our [cookiecutter repository](https://github.com/pyOpenSci/cookiecutter-pyopensci/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/CONTRIBUTING.rst). Even if you're not using cookiecutter to build your project, you can download our CONTRIBUTING.rst as a starting point.

You can tweak it a bit depending on your workflow and package. For example, make sure contributors have instructions in your CONTRIBUTING file for running local tests if not trivial. CONTRIBUTING can also contain some details about how you acknowledge contributions (see [this section](#attributions)) and the roadmap of your package (cf [this example](https://github.com/ecohealthalliance/fasterize/blob/master/CONTRIBUTING.md)).

### Issue labelling

You can use labels such as "help wanted", "good first issue", or "beginner" to help potential collaborators, including newbies, find your repo. For more info, see this [GitHub article](https://help.github.com/articles/helping-new-contributors-find-your-project-with-labels/). 

## Working with collaborators

### Onboarding collaborators

There's no general pyOpenSci rule as to how you should onboard collaborators. You should increase their rights to the repo as you gain trust, and you should definitely acknowledge contributions (see [this section](#attributions)).

You can ask a new collaborator to make PRs (see following section for assessing a PR locally, i.e. beyond CI checks) to dev/master and assess them before merging, and after a while let them push to master, although you might want to keep a system of PR reviews... even for yourself once you have team mates!

A possible model for onboarding collaborators is provided by Jim Hester in [his `lintr` repo](https://github.com/jimhester/lintr/issues/318).

If your problem is _recruiting_ collaborators, you can post an open call like Jim Hester's [on Twitter](https://twitter.com/jimhester_/status/997109466674819074), [GitHub]((https://github.com/jimhester/lintr/issues/318)). As an pyOpenSci package author, you can also ask for help from pyOpenSci. 

### Working with collaborators (including yourself)

You could implement the "[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)" philosophy as explained by Amanda Dobbyn in [this rOpenSci blog post](https://ropensci.org/blog/2018/04/20/monkeydo/).

One particular aspect of working with collaborators is reviewing pull requests. Even if not adopting gitflow it might make sense for repo collaborators to make PRs and have them reviewed, and in general PRs by external developers will need to be assessed Sometimes you'll be fine just reading the changes and trusting [Continuous integration](../packaging/packaging_guide#continuous-integration). Sometimes you'll need more exploration and even extension of the PR in which case we recommend reading ["Explore and extend a pull request" in happygitwithr.com](http://happygitwithr.com/pr-extend.html).

### Be generous with attributions {#attributions}

If someone contributes to your repository consider adding them in CONTRIBUTORS, as contributor for small contributions, author for bigger contributions. Also consider adding their name near the feature/bug fix line in HISTORY We recommend your being generous with such acknowledgements.

If your package was reviewed by pyOpenSci and you feel that your reviewers have made a substantial contribution to the development of your package, you may list them in CONTRIBUTORS as a reviewer. Only include reviewers after asking for their consent. 

Please do not list editors as contributors. Your participation in and contribution to pyOpenSci is thanks enough!

### Welcoming collaborators to pyOpenSci

If you give someone write permissions to the repository, please contact one of [the editors]() so that this new contributor can get invited to pyOpenSci's GitHub organization. 

