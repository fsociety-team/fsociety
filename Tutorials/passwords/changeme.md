# changeme Tutorial

## Overview
`changeme` checks a host for default credential exposures.

## Prerequisites
- Authorized host target.
- Reachability to services on the target.

## Interactive Steps
1. Run `fsociety`.
2. Select `passwords`.
3. Select `changeme`.
4. Enter host at `Enter a host:`.

## Practical Example
Input:

```text
Enter a host: 192.168.56.10
```

Executed pattern:

```bash
python3 changeme.py 192.168.56.10
```

## Expected Output
- Service checks and any default-credential findings.

## Troubleshooting
- Blank host values are invalid.
- Verify target services are reachable from your test system.

## Safety Notes
Default-credential testing is intrusive; run only with explicit authorization.
