# host2ip Tutorial

## Overview
`host2ip` resolves a hostname to an IP address and stores the host in your local fsociety host list.

## Prerequisites
- Network access to resolve DNS.
- A valid hostname you are authorized to test.

## Interactive Steps
1. Run `fsociety`.
2. Select `utilities`.
3. Select `host2ip`.
4. At prompt `Enter a host:`, provide a hostname.

## Practical Example
Input:

```text
Enter a host: example.com
```

## Expected Output
You should see output similar to:

```text
example.com has the IP of 93.184.216.34
```

## Troubleshooting
- If resolution fails, confirm DNS/network connectivity.
- If hostname is invalid, retry with a valid FQDN.

## Safety Notes
Use only hosts you are authorized to assess.
