import nox
import pathlib

nox.options.reuse_existing_virtualenvs = True

build_command = ["-b", "html", ".", "_build/html"]

AUTOBUILD_IGNORE = [
    "_build",
    ".nox",
    "build_assets",
    "tmp",
    ".pytest_cache",
]

# Sphinx output and source directories
BUILD_DIR = "_build"
OUTPUT_DIR = pathlib.Path(BUILD_DIR, "html")
SOURCE_DIR = pathlib.Path(".")

# Sphinx build commands
SPHINX_BUILD = "sphinx-build"
SPHINX_AUTO_BUILD = "sphinx-autobuild"

# Sphinx parameters used to build the guide
BUILD_PARAMETERS = ["-b", "html"]

# Sphinx parameters used to test the build of the guide
TEST_PARAMETERS = ["-W", "--keep-going", "-E", "-a"]


@nox.session
def docs(session):
    session.install("-r", "requirements.txt")
    cmd = ["sphinx-build"]
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)


@nox.session(name="docs-live")
def docs_live(session):
    session.install("-r", "requirements.txt")
    cmd = ["sphinx-autobuild"]
    for folder in AUTOBUILD_IGNORE:
        cmd.extend(["--ignore", f"*/{folder}/*"])
    cmd.extend(build_command + session.posargs)
    session.run(*cmd)


@nox.session(name="docs-test")
def docs_test(session):
    """
    Build the packaging guide with more restricted parameters.

    Note: this is the session used in CI/CD to release the guide.
    """
    session.install("-e", ".")
    session.run(
        SPHINX_BUILD,
        *BUILD_PARAMETERS,
        *TEST_PARAMETERS,
        SOURCE_DIR,
        OUTPUT_DIR,
        *session.posargs,
    )
