## 2026-01-25 - Missing Content Security Policy
**Vulnerability:** The application lacks a Content Security Policy (CSP), allowing scripts and resources to be loaded from any origin, increasing the risk of XSS and data injection.
**Learning:** Even static sites with external dependencies (Google Fonts, GTM) require a CSP to define trusted sources and prevent malicious injections.
**Prevention:** Implement a strict CSP meta tag restricting sources to 'self' and trusted third parties (Google).
