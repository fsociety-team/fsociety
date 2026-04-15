# cupp Tutorial

## Overview
`cupp` launches interactive password profiling to generate targeted wordlists.

## Prerequisites
- Authorized assessment context.
- Legitimate profile data from approved engagement inputs.

## Interactive Steps
1. Run `fsociety`.
2. Select `passwords`.
3. Select `cupp`.
4. fsociety executes interactive mode directly.

Executed pattern:

```bash
python3 cupp.py -i
```

## Practical Example
In the CUpp prompts, provide approved sample details for a training target profile and generate a wordlist for controlled testing.

## Expected Output
- Generated candidate password list file from the provided profile data.

## Troubleshooting
- If prompts do not appear, verify Python runtime and terminal interactivity.
- Keep input data concise to avoid oversized lists.

## Safety Notes
Do not use generated wordlists against unauthorized targets.
