# s3scanner Tutorial

## Overview
`s3scanner` checks possible S3 bucket names derived from supplied domains.

## Prerequisites
- Authorized domain list.
- Internet access.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `s3scanner`.
4. At `Enter one or more domains:`, input space-separated domains.

## Practical Example
Input:

```text
Enter one or more domains: example.com example.org
```

Executed pattern:

```bash
python3 s3scanner.py ~/.fsociety/s3_domains.txt
```

Note: fsociety writes your domains to `~/.fsociety/s3_domains.txt` before running.

## Expected Output
- Checked bucket candidates.
- Accessible or misconfigured bucket findings, if any.

## Troubleshooting
- Ensure domains are valid and space-separated.
- If no results, verify network access and region behavior.

## Safety Notes
Do not access or download data from buckets unless explicitly authorized.
