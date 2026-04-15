# xsstrike Tutorial

## Overview
`xsstrike` runs XSS-oriented testing against a target URL with optional crawling and parameter discovery.

## Prerequisites
- Authorized web target URL.
- Internet/local access to target application.

## Interactive Steps
1. Run `fsociety`.
2. Select `web_apps`.
3. Select `xsstrike`.
4. Enter URL at `Enter a url to scan:`.
5. Choose crawl option when asked.
6. Choose hidden parameter discovery when asked.

## Practical Example
Input flow:

```text
Enter a url to scan: http://testphp.vulnweb.com/artists.php?artist=1
Do you want to crawl? y
Do you want to find hidden parameters? y
```

Executed pattern:

```bash
python3 xsstrike.py --url http://testphp.vulnweb.com/artists.php?artist=1 --crawl --params
```

## Expected Output
- Reflected/DOM/contextual XSS test progress.
- Candidate payload and endpoint findings.

## Troubleshooting
- Use full URL with protocol.
- Large crawl scopes can increase scan duration.

## Safety Notes
Only test web applications where you have explicit testing permission.
