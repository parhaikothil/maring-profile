## 2024-05-23 - Static Site CSP Constraints
**Vulnerability:** Missing Content Security Policy (CSP) in static HTML application.
**Learning:** Implementing strict CSP (blocking `unsafe-inline`) is challenging in pure static sites without a build system to generate nonces or hashes for inline scripts/styles.
**Prevention:** When restricted to static files, use `unsafe-inline` but strictly whitelist external domains (e.g., Google Analytics, Fonts) to maintain some level of protection against malicious external script injection.
