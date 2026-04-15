# sublist3r Tutorial

## Overview
`sublist3r` enumerates subdomains for a target domain.

## Prerequisites
- Authorized domain target.
- Internet access for passive source lookups.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `sublist3r`.
4. At `Enter a domain to enumerate:`, enter the domain.

## Practical Example
Input:

```text
Enter a domain to enumerate: example.com
```

Executed pattern:

```bash
python3 sublist3r.py -v -d example.com
```

## Expected Output
- Enumerated subdomains printed in verbose mode.
- Final count and discovered names.

## Troubleshooting
- If results are empty, verify the domain and internet connectivity.
- Some sources may throttle requests.

## Safety Notes
Perform enumeration only for authorized testing scopes.
