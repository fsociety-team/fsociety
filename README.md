<div align="center">
  <a href="https://fsociety.dev/">
    <img width="467" height="78" src="https://raw.githubusercontent.com/fsociety-team/fsociety/master/images/fsociety.png" alt="fsociety">
  </a>
</div>

# fsociety [![Python Version](https://img.shields.io/pypi/pyversions/fsociety?color=orange&style=flat-square)](https://www.python.org/downloads/) [![PyPi](https://img.shields.io/pypi/v/fsociety?style=flat-square)](https://pypi.org/project/fsociety/) [![Docker Automated build](https://img.shields.io/docker/automated/fsocietyteam/fsociety?style=flat-square)](https://hub.docker.com/repository/docker/fsocietyteam/fsociety) [![License](https://img.shields.io/pypi/l/fsociety?style=flat-square)](https://github.com/fsociety-team/fsociety/blob/master/LICENSE)

A Penetration Testing Framework

[comment]: # "UPDATE: Add CLI graphic here"

![cli](https://raw.githubusercontent.com/fsociety-team/fsociety/master/images/cli.png)

## Install

```bash
pip install fsociety
```

## Update

```bash
pip install --upgrade fsociety
```

## Usage

```bash
usage: fsociety [-h] [-i]

A Penetration Testing Framework

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     start interaction cli
```

## Develop

```bash
git clone https://github.com/fsociety-team/fsociety.git
pip install -e ".[dev]"
```

## Docker

```bash
docker pull fsocietyteam/fsociety
docker run -it fsocietyteam/fsociety # -it makes the terminal interactive
```

## License

[MIT Licence](https://github.com/fsociety-team/fsociety/blob/master/LICENSE)
