## 2024-10-24 - [Legacy Inline Scripts Constrain CSP]
**Vulnerability:** Lack of Content Security Policy allowing potential XSS.
**Learning:** The application architecture relies heavily on inline scripts (analytics, scroll animations) and styles within `index.html`. This necessitates `unsafe-inline` in the CSP, reducing its effectiveness against XSS but still providing defense against external script injection.
**Prevention:** Future refactoring should extract inline JS/CSS to separate files to allow a stricter CSP (`script-src 'self'`).
