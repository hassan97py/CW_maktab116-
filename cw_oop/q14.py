import urllib.parse

class URLHandler:
    @classmethod
    def parse_url(cls, url):
        parsed_url = urllib.parse.urlparse(url)
        
        url_components = {
            "protocol": parsed_url.scheme,
            "domain": parsed_url.netloc,
            "path": parsed_url.path,
            "query_params": urllib.parse.parse_qs(parsed_url.query)
        }
        
        return url_components
    
url = "https://www.example.com/search?q=python&page=2"
url_components = URLHandler.parse_url(url)
print(url_components)

