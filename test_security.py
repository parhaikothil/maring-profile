import sys

def verify_csp():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        if '<meta http-equiv="Content-Security-Policy"' not in content:
            print("❌ CSP Meta tag not found in index.html")
            sys.exit(1)

        print("✅ CSP Meta tag found")

        # Check specific directives
        csp_start = content.find('content="') + 9
        csp_end = content.find('"', csp_start)
        csp_content = content[csp_start:csp_end]

        directives = [
            "default-src 'self'",
            "script-src 'self' https://www.googletagmanager.com",
            "style-src 'self' https://fonts.googleapis.com 'unsafe-inline'",
            "font-src 'self' https://fonts.gstatic.com"
        ]

        for directive in directives:
            if directive in content:
                print(f"✅ Directive found: {directive}")
            else:
                print(f"❌ Directive missing: {directive}")
                # Don't exit yet, check all

        # Check script externals
        if '<script src="analytics.js"></script>' in content:
             print("✅ analytics.js linked")
        else:
             print("❌ analytics.js link missing")
             sys.exit(1)

        if '<script src="script.js"></script>' in content:
             print("✅ script.js linked")
        else:
             print("❌ script.js link missing")
             sys.exit(1)

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_csp()
