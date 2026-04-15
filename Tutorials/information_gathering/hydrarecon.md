# hydrarecon Tutorial

## Overview
`hydrarecon` performs basic or crawl-based recon for a domain.

## Prerequisites
- Authorized domain target.
- Internet connectivity.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `hydrarecon`.
4. Enter domain at `Enter a domain to scan:`.
5. Choose crawl mode when asked `Do you want to crawl? [default=No]`.

## Practical Example
Input flow:

```text
Enter a domain to scan: example.com
Do you want to crawl? [default=No] y
```

Executed pattern:

```bash
python3 hydrarecon.py -d example.com -o ~/.fsociety --crawl
```

## Expected Output
- Recon artifacts written to fsociety install directory.
- More expansive findings when crawl mode is enabled.

## Troubleshooting
- Use plain domain format, not full URL.
- Crawl mode can take longer on larger targets.

## Safety Notes
Recon only assets explicitly included in your test scope.
