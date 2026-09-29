#!/usr/bin/env bash
# Build the Sphinx peer review guide on Netlify (deploy previews).
set -euo pipefail

# Full history so git describe can see release tags.
if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
  git fetch --unshallow
fi
git fetch --tags || true

python -m pip install --upgrade pip
python -m pip install nox
nox -s docs
