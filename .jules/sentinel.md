## 2024-05-23 - Content Security Policy
**Vulnerability:** Missing Content Security Policy (CSP) allowed potential XSS attacks.
**Learning:** Even static sites benefit from CSP to prevent execution of unauthorized scripts, especially when using external resources like Google Analytics and Fonts.
**Prevention:** Added a strict CSP meta tag and moved inline scripts to external files to avoid 'unsafe-inline' for scripts.
