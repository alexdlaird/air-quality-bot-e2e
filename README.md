[![CI Tests](https://github.com/alexdlaird/air-quality-bot-e2e/actions/workflows/ci.yml/badge.svg)](https://github.com/alexdlaird/air-quality-bot-e2e/actions/workflows/ci.yml)
![GitHub License](https://img.shields.io/github/license/alexdlaird/air-quality-bot)

# Air Quality Bot E2E Tests

The [Air Quality Bot](https://github.com/alexdlaird/air-quality-bot) is
generally available by texting a zip code (and optionally the word "map") to
(415) 212-4229. This project runs end-to-end tests against the bot to ensure it
is up and responding properly.

## Running Locally

Run `make install`, then update the values in `.env` to reflect your account's
values. Ideally, E2E tests should run from against a different Twilio account
than the bot itself.

To run the tests, simply execute:

```sh
make test
```

## CI Build

For the E2E tests to run in a CI system, simply add the environment variables found
in `.env` to the configuration for the CI build. In the CI system, you can also
set these E2E tests to run based on a cron schedule.

In addition to running the E2E tests manually or on a schedule, you can trigger
them to run after each deploy. To do this, simply add the following variables to
your `.env` file in the [Air Quality Bot](https://github.com/alexdlaird/air-quality-bot/blob/main/.env.example)
repository. If they are set, E2E tests will automatically run after the
`./deploy.sh` script is executed successfully.
