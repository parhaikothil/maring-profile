## 2024-05-22 - Static Site Security Constraints

**Vulnerability:** Inability to set HTTP security headers (CSP, X-Frame-Options, HSTS) on the server side due to the static nature of the deployment (implied GitHub Pages or similar simple hosting).
**Learning:** Relying solely on `<meta>` tags for security headers is limited. `Content-Security-Policy` works via meta tag, but `X-Frame-Options` and `Strict-Transport-Security` do not. This leaves the site potentially vulnerable to Clickjacking if not mitigable by CSP `frame-ancestors` (which is also not supported in `<meta>` tags).
**Prevention:** For static sites requiring high security, use a CDN or hosting provider that allows header configuration (e.g., Netlify `_headers`, Vercel `vercel.json`, or Cloudflare Workers), rather than relying purely on HTML meta tags. In this specific repo, we accept the limitation and use `<meta>` for CSP.
