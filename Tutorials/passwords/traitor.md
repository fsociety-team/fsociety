# traitor Tutorial

## Overview
`traitor` runs Linux privilege escalation checks and exploit paths from an existing foothold.

## Prerequisites
- Linux target in authorized scope.
- Local execution context on target host.

## Interactive Steps
1. Run `fsociety`.
2. Select `passwords`.
3. Select `traitor`.
4. At `Make a selection:`, choose:
   - `any` for full check (`-a`)
   - or a specific exploit name (mapped to `-e <name>`)

## Practical Example
Input:

```text
Make a selection: any
```

Executed pattern:

```bash
~/.fsociety/traitor/traitor -a
```

Specific exploit example:

```text
Make a selection: docker
```

Executed pattern:

```bash
~/.fsociety/traitor/traitor -e docker
```

## Expected Output
- Enumeration and exploit attempts for privilege escalation vectors.
- Success/failure status per check.

## Troubleshooting
- Ensure architecture-compatible binary was downloaded.
- Requires appropriate local execution context and permissions.

## Safety Notes
Privilege escalation testing must be explicitly authorized and controlled.
