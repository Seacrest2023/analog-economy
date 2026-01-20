# Security Policy

## Reporting a Vulnerability

The Analog Economy takes security seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, please email: **security@analogeconomy.com**

Include the following information:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes (optional)

### What to Expect

- **Acknowledgment**: Within 48 hours of your report
- **Initial Assessment**: Within 7 days
- **Resolution Timeline**: Depends on severity (see below)
- **Credit**: With your permission, we'll credit you in our security advisories

### Severity Levels & Response Times

| Severity | Description | Target Resolution |
|----------|-------------|-------------------|
| Critical | Data breach, RCE, auth bypass | 24-48 hours |
| High | Significant data exposure, privilege escalation | 7 days |
| Medium | Limited data exposure, DoS | 30 days |
| Low | Minor issues, hardening | 90 days |

## Security Practices

### Data Protection

- All player data is anonymized before storage
- PII is never exported to buyers
- End-to-end encryption for sensitive data
- Regular security audits

### Gaian Governance

The Gaian engine enforces strict ethical boundaries:
- No facial recognition training data
- No actionable terrorism content
- No bioweapon synthesis information
- Human review for sensitive exports

### Infrastructure

- All services run as non-root users
- Network isolation between components
- Secrets managed via secure vault
- Regular dependency updates

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x.x   | Yes       |
| < 1.0   | No        |

## Bug Bounty

We are currently developing a bug bounty program. Details coming soon.

## Contact

- Security issues: security@analogeconomy.com
- General inquiries: contact@analogeconomy.com
