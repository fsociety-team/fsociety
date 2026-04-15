# spawn_shell Tutorial

## Overview
`spawn_shell` opens a local shell from inside fsociety and returns when you exit.

## Prerequisites
- A local shell environment (`$SHELL` or `/bin/bash`).

## Interactive Steps
1. Run `fsociety`.
2. Select `utilities`.
3. Select `spawn_shell`.
4. Use the shell, then type `exit` to return to fsociety.

## Practical Example
After starting `spawn_shell`, run:

```bash
pwd
ls -la
exit
```

## Expected Output
- fsociety displays: `Enter exit to return to fsociety`
- You get an interactive shell prompt.
- `exit` returns to fsociety menu flow.

## Troubleshooting
- If shell does not start, verify your shell is installed and executable.
- On restricted environments, fallback shell permissions may block execution.

## Safety Notes
Commands run in your local environment. Execute only authorized and safe commands.
