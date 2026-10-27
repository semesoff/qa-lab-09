# Laboratory Work 9

The project contains API tests for JSONPlaceholder and a GitHub Actions workflow
that runs them on pushes and pull requests to `main` or `master`.

## Local run

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -v
```

Workflow file: `.github/workflows/run-tests.yml`.
