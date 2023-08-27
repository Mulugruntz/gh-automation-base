# gh-automation-base
A project base for automating Python tasks using GitHub actions and an Aiven for PostgreSQL database.

## Setup
1. Create a new repository using this repository as a template.
2. Create a new Aiven PostgreSQL service.
3. Copy `.env.example` to `.env` and fill in the values.
4. Install poetry and the dependencies (base + dev) using the following commands:

    ```bash
    pip install poetry
    poetry install --all-extras
    ```

5. Initialize the database using the following command:

    ```bash
    make migration-init migration-apply
    ```

6. Push to GitHub, set the [repo secrets][github-secrets] and enable GitHub actions.
7. This will start populating your database with Quotes (example pipeline).


[github-secrets]: https://docs.github.com/en/actions/reference/encrypted-secrets
