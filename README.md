# Example integration of Peewee and FastAPI.

## Setup project

* Use `pipenv` to create virtualenv:
  ```bash
  pipenv --python 3.12
  pipenv shell
  pipenv install --dev
  ```
* Init database:
  ```bash
  make init
  ```

## (Optional) Migrations
* Run migrations:
  ```bash
  make migrate-forwards
  ```

## Run app

Turn on pipenv shell and run:
  ```bash
  make run
  ```

Navigate to [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/) to check API endpoints definitions.
