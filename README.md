# devops-demo

Sample project used to demonstrate Jenkins + GitHub integration.

| File | Purpose |
|---|---|
| `app.py` | Small Python app (build step: `python3 app.py`) |
| `test_app.py` | Unit tests (test step: `python3 -m unittest -v`) |
| `index.html` | Static web page |
| `Jenkinsfile` | Declarative pipeline: Checkout → Build → Test |
