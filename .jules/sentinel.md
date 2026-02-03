## 2024-10-18 - [Static Site Security Enhancements]
**Vulnerability:** Missing security headers (CSP, Referrer-Policy) in a static HTML site.
**Learning:** For static sites without server configuration access (like GitHub Pages raw hosting), security headers cannot be set via HTTP response headers.
**Prevention:** Use `<meta>` tags for `Content-Security-Policy` and `Referrer-Policy`. Note that `X-Content-Type-Options` cannot be set via meta tag.
