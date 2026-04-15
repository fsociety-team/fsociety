# hash_buster Tutorial

## Overview
`hash_buster` attempts to resolve a hash value using online/offline lookup sources supported by the upstream tool.

## Prerequisites
- Authorized hash sample from your assessment.

## Interactive Steps
1. Run `fsociety`.
2. Select `passwords`.
3. Select `hash_buster`.
4. Enter value at `Enter a hash:`.

## Practical Example
Input:

```text
Enter a hash: 5f4dcc3b5aa765d61d8327deb882cf99
```

Executed pattern:

```bash
python3 hash.py -s 5f4dcc3b5aa765d61d8327deb882cf99
```

## Expected Output
- Matching plaintext result when known.
- No-match output when not found.

## Troubleshooting
- Verify hash string has no spaces/newlines.
- Confirm supported hash types in upstream tool docs.

## Safety Notes
Handle recovered plaintext credentials under strict policy and authorization controls.
