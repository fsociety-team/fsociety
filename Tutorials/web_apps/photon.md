# photon Tutorial

## Overview
`photon` crawls a target website for links, endpoints, and OSINT-relevant artifacts.

## Prerequisites
- Authorized target URL.
- Network access to target.

## Interactive Steps
1. Run `fsociety`.
2. Select `web_apps`.
3. Select `photon`.
4. Enter URL at `Enter a url to scan:`.
5. Choose whether to clone site.
6. Choose whether to use Wayback integration.

## Practical Example
Input flow:

```text
Enter a url to scan: https://example.com
Do you want to clone the site? y
Do you want to use wayback? y
```

Executed pattern:

```bash
python3 photon.py --url https://example.com --clone --wayback
```

## Expected Output
- Crawled URLs and discovered endpoints.
- Additional historical artifacts when Wayback is enabled.

## Troubleshooting
- Ensure URL is reachable and includes protocol.
- Disable clone/wayback if scan is too slow.

## Safety Notes
Crawl only systems and domains included in your authorized scope.
