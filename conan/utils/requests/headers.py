import random


def generate():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/117.0 Safari/537.36",
    ]

    accept_languages = [
        "en-US,en;q=0.9"
        # atleast understable..
    ]

    headers = {
        "User-Agent": random.choice(user_agents),  # Random User-Agent
        "Accept-Language": random.choice(accept_languages),  # Language preferences
        "Referer": "https://www.google.com/",  # Referrer for added legitimacy
        "Accept-Encoding": "gzip, deflate, br",  # Compression support
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",  # MIME types
        "Connection": "keep-alive",  # Persistent connections
        "Upgrade-Insecure-Requests": "1",  # Indicates HTTPS preference
        "Sec-Fetch-Site": "same-origin",  # Origin of the request
        "Sec-Fetch-Mode": "navigate",  # Request mode
        "Sec-Fetch-User": "?1",  # User navigation intent
        "Sec-Fetch-Dest": "document",  # Request destination
        "Cache-Control": "no-cache",  # Cache behavior
        "Pragma": "no-cache",  # HTTP/1.0 cache control
    }

    return headers
