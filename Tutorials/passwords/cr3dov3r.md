# cr3dov3r Tutorial

## Overview
`cr3dov3r` checks credential reuse/leak exposure for an email address.

## Prerequisites
- Authorized email target within engagement scope.

## Interactive Steps
1. Run `fsociety`.
2. Select `passwords`.
3. Select `cr3dov3r`.
4. Enter an email at `Enter a email:`.

## Practical Example
Input:

```text
Enter a email: analyst@example.com
```

Executed pattern:

```bash
python3 Cr3d0v3r.py analyst@example.com
```

## Expected Output
- Breach/reuse-related findings for the email if data exists.

## Troubleshooting
- Verify email formatting.
- Network/API availability may affect results.

## Safety Notes
Only query accounts that are explicitly authorized for security assessment.
