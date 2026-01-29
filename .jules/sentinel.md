# 🛡️ Sentinel's Journal

## 2024-05-22 - Content Security Policy Implementation
**Vulnerability:** Missing Content Security Policy (CSP) and security headers in a static HTML site.
**Learning:** Static sites without server-side header control must rely on meta tags for security headers. While `X-Frame-Options` and `X-Content-Type-Options` cannot be set via meta tags, CSP and Referrer-Policy can be, providing significant XSS protection.
**Prevention:** Always include CSP meta tags in static HTML entry points to mitigate XSS risks, especially when using external scripts like Google Analytics.
