## 2026-01-20 - Static Site CSP Gap
**Vulnerability:** Absence of Content Security Policy (CSP) in a static HTML site.
**Learning:** Even static sites without backends are vulnerable to XSS (e.g. via DOM-based XSS if JS is present) and should enforce CSP. The architecture relies on inline scripts/styles which necessitates 'unsafe-inline', weakening the CSP but still better than nothing.
**Prevention:** Add CSP meta tag by default in HTML templates.
