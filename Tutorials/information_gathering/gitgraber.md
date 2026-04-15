# gitgraber Tutorial

## Overview
`gitgraber` searches GitHub content for potentially sensitive strings using keyword lists.

## Prerequisites
- A valid search query.
- Optional GitHub token for better API limits.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `gitgraber`.
4. Enter query at `Enter a search query:`.
5. Enter keyword file at `Enter a keywords path [default=keywords.txt]:`.
6. Optionally add token when prompted.

## Practical Example
Input flow:

```text
Enter a search query: org:examplecorp password
Enter a keywords path [default=keywords.txt]: keywords.txt
Do you want to add a GitHub token? y
Enter a GitHub token: ghp_xxxxxxxxxxxxxxxxxxxx
```

Executed pattern:

```bash
python3 gitGraber.py -k <wordlists_path>/keywords.txt -q org:examplecorp password
```

## Expected Output
- Matching files/snippets for provided keywords.
- Improved request stability when token is configured.

## Troubleshooting
- Verify keyword file exists in gitgraber wordlists.
- Use token if rate limits are encountered.

## Safety Notes
Search and review only data within legal and authorized boundaries.
