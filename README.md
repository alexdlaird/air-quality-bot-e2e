[![Build Status](https://travis-ci.org/alexdlaird/air-quality-bot-e2e.svg?branch=master)](https://travis-ci.org/alexdlaird/air-quality-bot-e2e)


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

```
make test
```

## Travis Build

For the E2E tests to run in Travis, simply add the environment variables found
in `.env` to the configuration for the Travis build. In Travis, you can also
set these E2E tests to run based on a cron schedule.

In addition to running the E2E tests manually or on a schedule, you can trigger
them to run after each deploy. To do this, simply add the following variables to
your `.env` file in the [Air Quality Bot](https://github.com/alexdlaird/air-quality-bot/blob/master/.env.example)
repository. If they are set, E2E tests will automatically run after the
`./deploy.sh` script is executed successfully.

* `TRAVIS_E2E_REPO` (something like `<USERNAME>%2Fair-quality-bot-e2e`, preserving the `%2F` instead of a `/`)
* `TRAVIS_ACCESS_TOKEN` (found [here](https://travis-ci.org/account/preferences))
