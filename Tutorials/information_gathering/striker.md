# striker Tutorial

## Overview
`striker` runs recon and vulnerability scanning against a domain.

## Prerequisites
- Authorized domain target.
- Working DNS resolution.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `striker`.
4. At `Enter a domain to scan:`, enter a domain.

## Practical Example
Input:

```text
Enter a domain to scan: example.com
```

Executed pattern:

```bash
python3 striker.py example.com
```

## Expected Output
- Recon details about the domain.
- Scanner findings from striker modules.

## Troubleshooting
- Verify DNS resolves for the target domain.
- Retry with a clean domain format (no protocol).

## Safety Notes
Scan only domains you have written permission to test.
