## 2024-05-22 - Static Site Security Header Constraints
**Vulnerability:** Inability to set standard HTTP security headers (HSTS, X-Frame-Options, X-Content-Type-Options) due to static architecture.
**Learning:** This repository is a single HTML file served statically. We cannot configure server-side headers. Security controls are limited to what HTML meta tags support (CSP, Referrer-Policy).
**Prevention:** Future security enhancements must rely on client-side controls (meta tags, JS validation) or require infrastructure changes (deployment config) outside this repo's scope.
