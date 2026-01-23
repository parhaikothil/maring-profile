# Sentinel Journal 🛡️

## Security Philosophy
- **Defense in Depth**: We apply multiple layers of protection. Even static sites benefit from security headers like CSP.
- **Fail Securely**: Systems should default to a secure state.
- **Trust Nothing**: Verify all inputs and restrict external resources.

## 2024-05-22 - Static Site Security Hardening
**Vulnerability:** Static sites often lack server-side security headers (CSP, HSTS, etc.) because they are just files served by a basic web server or CDN without complex configuration.
**Learning:** We can simulate some security headers using `<meta>` tags in HTML. While not as comprehensive as server-side headers (e.g., no `X-Frame-Options` support in meta), they provide a critical layer of defense against XSS and data exfiltration.
**Prevention:** Implemented strict `Content-Security-Policy` and `Referrer-Policy` via `<meta>` tags in `index.html`. This whitelists only necessary external domains (Google Analytics/Fonts) and prevents unauthorized scripts from loading.
