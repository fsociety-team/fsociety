# sqlmap Tutorial

## Overview
`sqlmap` automates SQL injection detection and database enumeration on authorized web targets.

## Prerequisites
- Authorized target URL with query parameters.
- Internet access if dependencies need installation.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `sqlmap`.
4. At prompt `Enter a url to scan:`, provide the target URL.
5. Optionally answer `Do you want to add any extra args?`.
6. If yes, provide arguments at `Enter any extra args:`.

## Practical Example
Input flow:

```text
Enter a url to scan: http://testphp.vulnweb.com/artists.php?artist=1
Do you want to add any extra args? y
Enter any extra args: --dbs --batch
```

Executed pattern:

```bash
python3 sqlmap.py -u http://testphp.vulnweb.com/artists.php?artist=1 --dbs --batch
```

## Expected Output
- Parameter testing progress.
- Injection findings (if present).
- Database names when `--dbs` is used.

## Troubleshooting
- Ensure target URL is reachable.
- If nothing is found, try different risk/level args.
- Use only legal test environments.

## Safety Notes
Run SQL injection testing only against assets you are explicitly authorized to assess.
