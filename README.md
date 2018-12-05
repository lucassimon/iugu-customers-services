# IUGU CUSTOMER SERVICES

This is a service that communicates SNS -> SQS -> this service -> to IUGU API

## Commands

Run `make help` to see the follow commands below.

```
make clean:
       Removes all pyc, pyo and __pycache__

make clean-build:
       Clear all build directories

make setup_dev
       Install dev dependencies and flake8 webhook
       Needs virtualenv activated and git initalized

make clone-dotenv
       Creates .env file base on .env-example
       Used by setup_dev command

make setup
       Install prod dependencies
       Needs virtualenv activated and git initalized

make isort:
       Run isort command cli in development features

make lint:
       Run lint

make coverage:
       Run tests with coverage and generate a badge (svg)

make test:
       Run tests with coverage, lint, and clean commands

make dev:
       Run the dev web application, with tests and coverage

make run:
       Run the web application without tests

make release:
       Creates a new tag and set the version in this package
       Ex: make release v=1.0.0
```

## Contributing

Clone this repo and create a virtualenv. Then run `make setup_dev`.

All features, bugs are in issues.

