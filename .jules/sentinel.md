## 2024-05-23 - [Static Site Header Limitations]
**Vulnerability:** Inability to set certain security headers (specifically X-Content-Type-Options) in a purely static environment without server config access.
**Learning:** HTML `<meta>` tags are limited in which headers they can emulate. `X-Content-Type-Options: nosniff` is ignored by browsers when set via meta tag.
**Prevention:** Do not implement `X-Content-Type-Options` via meta tags. Focus on CSP and Referrer-Policy which are supported.
