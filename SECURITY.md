# Security Policy

## Overview
This repository forms part of the UK Home Office Core Cloud Platform’s shared GitHub Actions tooling. It contains a reusable trivy scant composite GitHub Action used across the platform to maintain python code.

Because of its purpose, the repository includes **intentionally invalid python code** for testing, validation, and demonstration.

This design requires specific security guidance, explained below.

## Why This Repository Contains Invalid python

The directories:

* `tests/**`

contain python code that:

* violate different python code rules

These files are required to:

* validate the python reusable actions

These files **must not** be treated as code.

## SAST Exclusions

To prevent false positives and unnecessary CI pipeline failures, the following SAST tools are configured to ignore test fixtures and examples:

**Checkov** (`.checkov.yaml`)

```yaml
skip-path:
  - '^tests/.*'
```

**SonarQube** (`sonar-project.properties`)
```
sonar.exclusions=tests/**,

```
These configurations ensure:

* Only the actual workflow logic and scripts are scanned

* Quality Gate failures reflect real issues, not test fixture content

* SARIF results remain meaningful

**Do Not Add Real Code Under** `tests/**` 

Any production python code must not be added to these directories, because:

* It will be invisible to SAST

* It may be mistaken for intentionally broken python

* It will not be validated by the trivy scan action

* It may mislead contributors and downstream teams


## Reporting Security Issues

If you believe you have found a security vulnerability in:

* this workflow

* the composite action

* the test harness

* or any supporting scripts

please follow the internal vulnerability disclosure process and notify the Core Cloud Platform team privately through the approved internal channels (Slack / security contacts).

**Do not open GitHub Issues for security vulnerabilities**.

## Dependency Security

This repository does not use third-party Python, Go, or python dependencies — only GitHub Actions and shell scripts.

Dependencies must satisfy:

* GitHub Enterprise action allow-lists

* Internal security requirements for workflows

* No hardcoded secrets


## Security Summary

| Area                    | Policy                                               |
| ----------------------- | ---------------------------------------------------- |
| Test python files       | Intentionally invalid & excluded from SAST           |
| Example Code            | Excluded from SAST, for demonstration only           |
| Real Code               | Not permitted in this repository                     |
| Secrets                 | Must use repo/org-encrypted secrets, never committed |
| Workflows               | Must use approved GitHub Actions only                |
| Vulnerability reporting | Private internal channels only                       |
