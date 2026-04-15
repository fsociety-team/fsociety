# sherlock Tutorial

## Overview
`sherlock` searches for social profile presence for one or more usernames.

## Prerequisites
- Usernames collected through authorized OSINT workflows.

## Interactive Steps
1. Run `fsociety`.
2. Select `information_gathering`.
3. Select `sherlock`.
4. At `Enter one or more usernames:`, provide space-separated usernames.

## Practical Example
Input:

```text
Enter one or more usernames: alice_example bob_example
```

Executed pattern:

```bash
python3 sherlock alice_example bob_example
```

## Expected Output
- List of platforms checked.
- Hit/miss status per platform for each username.

## Troubleshooting
- Ensure usernames are separated by spaces.
- Network latency can slow checks across many sites.

## Safety Notes
Use only lawful OSINT methods and respect platform policies.
