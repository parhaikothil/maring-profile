# Sentinel's Journal

## 2024-10-24 - CSP Implementation
**Vulnerability:** Missing Content Security Policy (CSP) allowed potential loading of malicious scripts if XSS vulnerabilities were present.
**Learning:** For static sites with heavy reliance on third-party scripts (GTM, GA, Fonts), crafting a CSP requires careful enumeration of all external domains (Google Fonts, GTM, etc.) and allowing 'unsafe-inline' for existing architecture.
**Prevention:** Implemented a strict CSP meta tag to whitelist only trusted domains and 'self'.
