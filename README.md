# Pre-commit hooks with Python

This repo contains an example set-up for using pre-commit hooks with your python environment.

The file `.pre-commit-config.yaml` controls the type of pre-commit you are currently using. There exists [several](https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e) ways to do automatic formatting with Python. This is just an example.

Original documentation for [pre-commit](https://pre-commit.com/).

## Usage

Start with activating the virtual environment and installing needed packages from the `pyproject.toml` file

```powershell
C:\Users\SuI\pre-commits-python-example (main)
PS>poetry shell
C:\Users\SuI\pre-commits-python-example (main)
(pre-commits-python-example-py3.11) poetry install
```

### Automatic run each time you try to commit something
```
C:\Users\SuI\pre-commits-python-example (main)
(pre-commits-python-example-py3.11) pre-commit install
```
To later bypass the hook use the `--no-verify` option
```
C:\Users\SuI\pre-commits-python-example (main)
(pre-commits-python-example-py3.11) git commit -m "wip: quick fix of data" --no-verify
```

### Manual run
You can do a manual `pre-commit` run on all files with the command
```
(C:\Users\SuI\pre-commits-python-example (main)
(pre-commits-python-example-py3.11) pre-commit run --all-files
```
