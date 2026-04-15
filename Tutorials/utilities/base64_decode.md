# base64_decode Tutorial

## Overview
`base64_decode` decodes Base64 text to raw bytes/text.

## Prerequisites
- A valid Base64 string.

## Interactive Steps
1. Run `fsociety`.
2. Select `utilities`.
3. Select `base64_decode`.
4. At prompt `Enter base64:`, paste your value.

## Practical Example
Input:

```text
Enter base64: ZnNvY2lldHk=
```

## Expected Output
You should see output similar to:

```text
Decoded that is: b'fsociety'
```

## Troubleshooting
- If decoding fails, verify padding and Base64 format.
- Remove accidental spaces/newlines in the input.

## Safety Notes
Only decode data you are allowed to inspect.
