FROM python:3.14-alpine AS build

RUN apk add build-base libffi-dev
RUN pip install poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    PYTHONUNBUFFERED=1


WORKDIR /app
COPY . .

RUN poetry install --no-root --only main --no-cache

FROM python:3.14-alpine AS runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=build /app /app

WORKDIR /app/src

EXPOSE {{ cookiecutter.port }}

CMD [ "uvicorn", "--host",  "0.0.0.0", "--port", "{{ cookiecutter.port }}", "{{ cookiecutter.package_name }}.app:app" ]
