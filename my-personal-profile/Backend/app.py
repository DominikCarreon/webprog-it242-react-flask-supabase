import os

# ... your other code ...

if __name__ == '__main__':
    # Use the PORT variable provided by Render, default to 5000 for local dev
    port = int(os.environ.get("PORT", 5000))
    # Must bind to 0.0.0.0 for Render to detect the port
    app.run(host='0.0.0.0', port=port)