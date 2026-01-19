## 2024-05-22 - [CSP in Single-File Static Sites]
**Vulnerability:** XSS risks in static sites often ignored due to simplicity.
**Learning:** Even simple static sites can benefit from CSP, but single-file architectures (inline JS/CSS) force the use of 'unsafe-inline', weakening the protection.
**Prevention:** For stricter CSP, separate JS/CSS into external files or use nonces/hashes (difficult to maintain manually in static files).
