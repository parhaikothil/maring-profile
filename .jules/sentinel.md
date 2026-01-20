# Sentinel Journal

## 2024-05-23 - Content Security Policy & Inline Constraints
**Vulnerability:** Missing Content Security Policy (CSP) allowed potential loading of malicious scripts/styles from unauthorized domains.
**Learning:** Static single-file architecture (`index.html` with inline CSS/JS) necessitates `unsafe-inline` in CSP. This weakens protection against XSS but is a required trade-off for this architecture without a build step/refactor.
**Prevention:** Future architectural improvements should separate CSS/JS into external files to remove `unsafe-inline` and strictly enforce source allowlists.
