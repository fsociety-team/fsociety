# nmap Tutorial

## Overview
`nmap` performs host scanning using predefined profiles exposed by fsociety.

## Prerequisites
- `nmap` installed (fsociety can install it per platform).
- Authorized host/IP target.

## Interactive Steps
1. Run `fsociety`.
2. Select `networking`.
3. Select `nmap`.
4. Enter target at `Enter a host:`.
5. Choose one profile at `Make a selection:`.

Common profiles include `simple`, `common_ports`, `all_ports`, `detect_os`, `vuln_scan`, and `heartbleed_test`.

## Practical Example
Input flow:

```text
Enter a host: 93.184.216.34
Make a selection: common_ports
```

Executed pattern:

```bash
nmap -F 93.184.216.34
```

## Expected Output
- Open/filtered/closed ports for the selected profile.
- Additional service/script output for advanced profiles.

## Troubleshooting
- Empty host input is invalid; provide a hostname or IP.
- Some profiles need elevated privileges for accurate results.

## Safety Notes
Port scanning must only target systems explicitly authorized for testing.
