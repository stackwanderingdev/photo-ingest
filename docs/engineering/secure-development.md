# Secure Software Development

Security is part of development, not only a final test. Scope depends on data,
attack surface, exposure, and potential harm.

## Security profile

- Risk rating: `Low | Medium | High | Critical`
- Exposed to untrusted users or networks: `Yes | No`
- Sensitive data: `<NONE OR CLASSIFICATION>`
- Threat model required: `Yes | No, because <REASON>`
- Owner: `<NAME/ROLE>`
- Last reviewed: `<YYYY-MM-DD>`

## Mandatory baseline

- Document trust boundaries and assets.
- Validate input, enforce authorization, and encode output at suitable boundaries.
- Manage secrets externally and never commit them.
- Make dependencies and artifacts reproducible and scannable.
- Detect security-relevant failures without logging sensitive data.
- Give vulnerabilities severity, owner, remediation target, and evidence.
- Publish artifacts only from the verified build pipeline.

## Activated security standards

| Standard/profile | Version | Scope | Target level | Evidence |
|---|---|---|---|---|
| NIST SSDF | `SP 800-218 v1.1` | Development process | `<PRACTICES>` | `<REVIEW/ARTIFACT>` |
| OWASP ASVS | `<VERSION>` | `<WEB APP/API OR NOT APPLICABLE>` | `<LEVEL>` | `<TEST/REPORT>` |
| OWASP MASVS/TCASVS | `<VERSION>` | `<MOBILE/DESKTOP OR NOT APPLICABLE>` | `<PROFILE>` | `<TEST/REPORT>` |

Versionless references are prohibited. Naming a standard is not evidence of
conformance; select, implement, and verify the applicable requirements.

## Threat model

- Assets: `<DATA/FUNCTIONS>`
- Actors: `<TRUSTED/UNTRUSTED>`
- Trust boundaries: `<SYSTEM BOUNDARIES>`
- Significant abuse cases: `<CASES OR DOCUMENT LINK>`
- Mitigations: `<REQ-/NFR-/INV-/TASK REFERENCES>`

Update the threat model for new trust boundaries, sensitive data flows,
authentication paths, or external exposure.

## Supply chain and release

- Dependency/vulnerability scan: `<COMMAND/CI JOB>`
- Secret scan: `<COMMAND/CI JOB>`
- Static/dynamic security test: `<COMMAND/CI JOB OR REASON>`
- SBOM: `<FORMAT AND GENERATION OR REASON>`
- Signing/provenance: `<PROCESS OR REASON>`
- Vulnerability reporting: `<SECURITY.md/CONTACT>`

## Official references

- [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP TCASVS for desktop/thick-client applications](https://owasp.org/TCASVS/)
