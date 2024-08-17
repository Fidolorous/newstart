from urllib.parse import urlparse

url = "https://www.cmkarting.cz/"
parsed_url = urlparse(url)
hostname = parsed_url.hostname

print(hostname)  # Output: www.example.com
