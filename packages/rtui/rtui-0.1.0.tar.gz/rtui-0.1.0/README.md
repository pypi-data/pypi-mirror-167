# RTUI - Robot Terminal User Interface

A TUI for [Astoria](https://github.com/srobo/astoria)-driven robots.

[![asciicast](https://asciinema.org/a/NJoUTaZ0G7VcotlNVgL7iXufR.svg)](https://asciinema.org/a/NJoUTaZ0G7VcotlNVgL7iXufR)

## Usage

The `rtui` command can be used standalone by running `rtui`.

It can also be used as an SSH forced command by adding the following to the `authorized_keys` file:

```
command="/usr/bin/rtui" ssh-ed25519 AAAA....
```

## Development

This application is written in Python 3.7+ and is managed using poetry.

```shell
poetry install
poetry run rtui
```

You will need to have an instance of Astoria running for some functionality, the docker setup is recommended for this.