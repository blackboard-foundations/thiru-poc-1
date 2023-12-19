# Contributing

This is a Python [CDK][getting-started] project. To start developing, you must first set
up access to Artifactory because this project uses constructs from the [cdk-constructs]
project. Follow [these instructions][artifactory] up until the creation of the `~/.netrc`
in the Python section. You do not need to configure `pip` with indexes.

Next, create a virtualenv:

```shell
python3 -m venv .env
```

Use the following to activate the newly created virtualenv:

```shell
source .env/bin/activate
```

If you are using Windows platform, you would activate the virtualenv like this:

```shell
.env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies:

```shell
pip install pip-tools
pip-sync
```

At this point you can now synthesize the CloudFormation template for this project:

```shell
cdk synth
```

## Local deployments

Sometimes it is helpful to manually deploy this project in order to quickly iterate on a
feature. These types of deployments are often called local deployments and use the stage
name of `local` instead of something like `dev` or `prod`.

To deploy, you must first have the [Foundations CLI][fnds-cli] installed. Once installed,
explore the built-in documentation for the CDK command and its subcommands:

```shell
fnds cdk -h
```

## Code formatting

This project is using [black][black] to handle formatting.

Install `black`:

```shell
brew install black
```

Format all files:

```shell
black .
```

There are also [editor integrations][black-editor] available. The file watcher for
PyCharm/Intellij works well for auto-formatting on file save.

## Pre-commit integration

If you are a frequent contributor, you should set up the [pre-commit][pre-commit]
integration. From within this project's directory, run:

```shell
brew install pre-commit
pre-commit install
```

Now various checks, import sorting and formatting will be done on git commit. To run
manually on all files, use this:

```shell
pre-commit run --all-files
```

If you want to know where `pre-commit` installs the tools it uses, see [this
section][pre-commit-cache] on how `pre-commit` handles caching.

## Dependency management

This project uses [pip-tools][pip-tools] to manage dependencies. The following commands
require the virtualenv to be active:

```shell
source .env/bin/activate
```

There are two primary workflows, **update** and **sync**.

### Update

To update dependencies, modify `requirements.in` file. Generally requirements get pinned
in this file for simplicity. After that, run:

```shell
pip-compile --upgrade
```

This will update `requirements.txt`.

### Sync

The sync command will sync `requirements.txt` with the virtualenv:

```shell
pip-sync
```

[getting-started]: https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html
[black]: https://github.com/psf/black
[black-editor]: https://black.readthedocs.io/en/stable/editor_integration.html
[pre-commit]: https://pre-commit.com
[pre-commit-cache]: https://pre-commit.com/#managing-ci-caches
[pip-tools]: https://github.com/jazzband/pip-tools
[cdk-constructs]: https://github.com/blackboard-innersource/cdk-constructs
[artifactory]: https://github.com/blackboard-innersource/cdk-constructs/blob/main/docs/artifactory.md
[fnds-cli]: https://github.com/blackboard-foundations/fnds-go/blob/main/cmd/fnds-cli/README.md
