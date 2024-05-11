# {{ cookiecutter.project_name }}

## Development

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and [just](https://github.com/casey/just) as a comamnd runner.

### Initial Setup

```sh
poetry install
```

### Running

```sh
just
```

This will run your pyview project using uvicorn with hot reloading.
