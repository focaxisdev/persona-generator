# Software checks

From a Git checkout with Python and Git available, run:

```sh
python scripts/check.py
```

The standard-library runner derives the repository directory from its own path,
so the command also works from another directory when given the script's path.
It parses every tracked `*.py` file with `ast.parse`, without importing source or
writing bytecode. Stage newly added Python files before checking them so Git
includes them in that syntax pass. It then runs all seven existing unittest
groups as separate subprocesses with the same Python interpreter:

- profiles-core
- adapter
- triage-v1
- triage-v2
- validation
- evaluation
- diagnostic-v2

Each group prints its actual output. A failed group does not prevent later groups
from running; the final summary lists all failed groups and returns a nonzero
exit status. Child processes receive `PYTHONDONTWRITEBYTECODE=1`. The checks do not
call a model or require package installation. They use synthetic temporary
fixtures and read-only checks of preserved historical records; they do not resume
live experiments or validate real owner confirmation.
Optional `jsonschema` validation is skipped when that package is absent; unittest
output reports the skips. Runs with and without it do not have identical optional
validation coverage.

Use a full-history checkout: diagnostic-v2 checks protected files against a Git
baseline and needs the referenced history. A source archive or shallow checkout
does not provide the same test prerequisites. Local verification used Python
3.12.14. Python 3.9 was not tested; this is not a compatibility claim for 3.9.

## GitHub Actions draft

[The workflow](../.github/workflows/software-checks.yml) runs the same command in
one GitHub-hosted Ubuntu 24.04 job with Python 3.12 and a ten-minute job timeout.
It requests pull-request events `opened`, `synchronize`, `reopened`, and
`ready_for_review`, for every target branch, including draft pull requests. It
also requests pushes to `main` only. Repository Actions settings and fork
approval requirements can still gate execution; an event trigger alone does not
guarantee a run. See GitHub's [event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request)
and [fork approval guidance](https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/approving-workflow-runs-from-public-forks).

Concurrency is grouped by workflow and pull-request number (or Git ref for a
push). A newer pull-request run cancels an older run in its group; push runs are
not automatically canceled. The job timeout bounds a single run, without making
any fee or billing claim.

The workflow pins [checkout v6.1.0](https://github.com/actions/checkout/tree/v6.1.0)
and [setup-python v7.1.0](https://github.com/actions/setup-python/tree/v7.1.0) to
full commit SHAs. Checkout fetches full history and disables persisted checkout
credentials. The token has `contents: read` permission. These controls do not
create a no-network sandbox: checkout, Python setup, and hosted infrastructure
can use the network. See GitHub's [security guidance](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)
and [token permissions documentation](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication#modifying-the-permissions-for-the-github_token).
There are no package installation, dependency cache, artifact upload, deployment,
release, secret, or OIDC steps.

This is a local-only workflow draft until explicitly published and run. A local
pass is not evidence of a hosted CI pass. Passing software checks supports only
the checked engineering behavior. Source grounding does not establish
psychometric validity, stable model behavior, or scientific acceptance; see the
[claims matrix](CLAIMS_MATRIX.md) and [release acceptance tracks](RELEASE_ACCEPTANCE.md).
