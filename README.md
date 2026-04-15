<p align="center">
  <img src="https://raw.githubusercontent.com/fsociety-team/fsociety/main/images/fsociety.png" width="600px" alt="fsociety-team/fsociety" />
</p>

# fsociety

[![PyPI](https://img.shields.io/pypi/v/fsociety?color=orange&logo=pypi&logoColor=orange&style=flat-square)](https://pypi.org/project/fsociety/)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue?logo=python&style=flat-square)](https://www.python.org/downloads/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fsociety?style=flat-square)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/fsocietyteam/fsociety/latest?style=flat-square)](https://hub.docker.com/r/fsocietyteam/fsociety)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-organge.svg?logo=git&logoColor=organge&style=flat-square)](http://makeapullrequest.com)
[![Open in Visual Studio Code](https://img.shields.io/badge/VSCode-Open-0098FF?style=flat-square)](https://open.vscode.dev/fsociety-team/fsociety)
[![Twitter Follow](https://img.shields.io/twitter/follow/fsociety_team?color=blue&style=flat-square)](https://twitter.com/fsociety_team)

A Modular Penetration Testing Framework

[![Packages](https://img.shields.io/badge/PACKAGES.md-red?style=flat-square)](https://github.com/fsociety-team/fsociety/blob/main/PACKAGES.md)
[![Changelog](https://img.shields.io/badge/CHANGELOG.md-red?style=flat-square)](https://github.com/fsociety-team/fsociety/blob/main/CHANGELOG.md)

<p align="center">
  <img src="https://raw.githubusercontent.com/fsociety-team/fsociety/main/images/cli.png" width="600px" alt="fsociety cli" />
</p>

## Overview

fsociety is a modular penetration testing framework that centralizes multiple security tools behind one interactive command-line interface.
It acts as an orchestrator: it helps install upstream tools, exposes them through a consistent menu, and runs them with guided prompts.

## Objectives

- Provide a unified workflow for common security testing tasks.
- Lower setup friction by handling install-on-demand behavior for integrated tools.
- Keep operator context across sessions with local persistent config and lists.
- Offer fast access to reconnaissance, networking, web testing, password, and utility workflows.

## Capabilities

### Information Gathering

- `sqlmap`: automatic SQL injection and database takeover helper.
- `striker`: recon and vulnerability scanning suite.
- `sublist3r`: subdomain enumeration.
- `sherlock`: username and account hunting across social platforms.
- `s3scanner`: open S3 bucket discovery and content dump support.
- `gitgraber`: search for sensitive information in GitHub content.
- `hydrarecon`: lightweight recon and optional crawling workflow.

### Networking

- `nmap`: network scanning with selectable premade scan profiles.
- `bettercap`: network attack and monitoring integration.

### Web Applications

- `xsstrike`: advanced XSS detection workflow.
- `photon`: high-speed crawler for OSINT and endpoint discovery.

### Passwords

- `cupp`: user password profiling.
- `cr3dov3r`: credential reuse helper.
- `hash_buster`: hash lookup and busting workflow.
- `changeme`: default credential scanner.
- `traitor`: Linux privilege escalation helper for low-hanging-fruit exploitation.

### Obfuscation

- `cuteit`: IP obfuscation helper.

### Built-in Utilities

- `host2ip`: resolve hostnames to IP addresses.
- `base64_decode`: decode Base64 input.
- `spawn_shell`: open a local shell and return with `exit`.
- `suggest_tool`: open tool request issue template.
- `print_contributors`: fetch and print contributor usernames from GitHub.

## Tutorials

Per-tool practical tutorials are available in [Tutorials/README.md](Tutorials/README.md).

### Utilities

- [host2ip](Tutorials/utilities/host2ip.md)
- [base64_decode](Tutorials/utilities/base64_decode.md)
- [spawn_shell](Tutorials/utilities/spawn_shell.md)
- [suggest_tool](Tutorials/utilities/suggest_tool.md)
- [print_contributors](Tutorials/utilities/print_contributors.md)

### Information Gathering

- [sqlmap](Tutorials/information_gathering/sqlmap.md)
- [striker](Tutorials/information_gathering/striker.md)
- [sublist3r](Tutorials/information_gathering/sublist3r.md)
- [sherlock](Tutorials/information_gathering/sherlock.md)
- [s3scanner](Tutorials/information_gathering/s3scanner.md)
- [gitgraber](Tutorials/information_gathering/gitgraber.md)
- [hydrarecon](Tutorials/information_gathering/hydrarecon.md)

### Networking

- [nmap](Tutorials/networking/nmap.md)
- [bettercap](Tutorials/networking/bettercap.md)

### Web Apps

- [xsstrike](Tutorials/web_apps/xsstrike.md)
- [photon](Tutorials/web_apps/photon.md)

### Passwords

- [cupp](Tutorials/passwords/cupp.md)
- [cr3dov3r](Tutorials/passwords/cr3dov3r.md)
- [hash_buster](Tutorials/passwords/hash_buster.md)
- [changeme](Tutorials/passwords/changeme.md)
- [traitor](Tutorials/passwords/traitor.md)

### Obfuscation

- [cuteit](Tutorials/obfuscation/cuteit.md)

## How It Works

1. Start `fsociety`.
2. On first run, accept terms and initialize local config.
3. Select a module in the main menu.
4. Select a tool from that module.
5. If dependencies are not present, fsociety prompts to install.
6. The selected upstream tool is executed with your provided inputs.

Conceptually:

```text
CLI entrypoint
  -> config bootstrap
    -> agreement gate
      -> module menu
        -> tool menu
          -> install (if needed)
            -> run tool
              -> persist state and exit
```

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
fsociety                 # interactive mode
fsociety --info          # system and fsociety config information
fsociety --suggest       # open tool suggestion issue template
fsociety --help          # CLI help
```

CLI synopsis:

```text
usage: fsociety [-h] [-i] [-s]

A Penetration Testing Framework

optional arguments:
  -h, --help     show this help message and exit
  -i, --info     gets fsociety info
  -s, --suggest  suggest a tool
```

## First-Run Behavior

On first launch, fsociety creates a local working directory and config, then asks you to accept terms before continuing to the interactive menu.

## Configuration and Persistence

fsociety stores state under:

- `~/.fsociety/`

Key files and values include:

- `~/.fsociety/fsociety.cfg`
- agreement state
- platform detection
- clone mode (`ssh_clone`)
- host list file name
- username list file name

Some modules persist entered hosts or usernames for improved autocomplete in later runs.

## Requirements and Prerequisites

- Python `>= 3.7`
- Internet connectivity for cloning tool repositories and some API-backed features
- `git` available in the environment
- OS-specific packages may be needed for some tools

Tool-specific caveats:

- `nmap` depends on system binary availability.
- `bettercap` typically requires `sudo` and additional system dependencies.
- Some wrapped tools invoke `python3` directly.

## Docker

```bash
docker pull fsocietyteam/fsociety
docker run --rm fsocietyteam/fsociety
docker run --rm fsocietyteam/fsociety --info
docker run --rm fsocietyteam/fsociety --suggest
docker run -it --rm --entrypoint sh fsocietyteam/fsociety -lc "fsociety"
```

The container entrypoint is `fsociety` and the default command is `--info`.

## Developing

```bash
git clone https://github.com/fsociety-team/fsociety.git
cd fsociety
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Common checks:

```bash
flake8 .
mypy fsociety
black .
```

## Troubleshooting

### `fsociety: command not found`

- Verify the environment where fsociety was installed is active.
- Confirm your scripts path is in `PATH`.

### Tool install or run failure

- Re-run and allow install prompts when requested.
- Verify required system packages for the selected tool.
- Confirm outbound network access.

### Permission issues

- Some networking operations need elevated privileges.
- Run only in authorized environments with required permissions.

### Config and state issues

- Inspect `~/.fsociety/fsociety.cfg`.
- If needed, back up and recreate `~/.fsociety`.

## Authorized Use

Use fsociety only for legal and authorized security testing, research, and education.

You are responsible for obtaining explicit permission before scanning, enumerating, testing, or exploiting any system, network, application, account, or data. Unauthorized activity may violate law and policy.

## License

This software is licensed under the [MIT](https://github.com/fsociety-team/fsociety/blob/main/LICENSE) License.
