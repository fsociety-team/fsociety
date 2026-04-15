# bettercap Tutorial

## Overview
`bettercap` launches the bettercap interactive environment for network testing workflows.

## Prerequisites
- `bettercap` installed (fsociety can install platform packages).
- Root privileges are typically required.
- Authorized network segment for testing.

## Interactive Steps
1. Run `fsociety`.
2. Select `networking`.
3. Select `bettercap`.
4. fsociety prints: `Please note that bettercap must be run with sudo`.
5. bettercap launches via sudo.

## Practical Example
Executed pattern:

```bash
sudo bettercap
```

Inside bettercap, run safe discovery commands like:

```text
help
net.show
```

## Expected Output
- bettercap interactive prompt and command output.
- Interface/network discovery data based on scope and permissions.

## Troubleshooting
- If sudo fails, verify user sudo privileges.
- Ensure network interface permissions and dependencies are present.

## Safety Notes
Network interception or active attacks are sensitive. Operate only under explicit written authorization.
