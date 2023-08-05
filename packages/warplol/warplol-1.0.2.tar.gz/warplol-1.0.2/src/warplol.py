from requests import get

class WarpLol:
    def __init__(self):
        pass

    def getshort(self, url: str) -> str:
        if url.startswith('https://') or url.startswith('http://'):
            url = get(f'https://warp.lol/api/short?url={url}').text
            return f"https://warp.lol/{url}"
        else:
            url = 'https://' + url
            url = get(f'https://warp.lol/api/short?url={url}').text
            return f"https://warp.lol/{url}"
    
    def geturl(self, key: str) -> str:
        if len(key) > 4:
            if key.startswith('https://warp.lol/') or key.startswith('http://warp.lol/') or key.startswith('warp.lol/'):
                key = key.replace('https://warp.lol/', '')
                url = get(f'https://warp.lol/api/url?short={key}').text
                return url
            else:
                return "Invalid URL"
        
        if len(key) == 4:
            url = get(f'https://warp.lol/api/url?short={key}').text
            return str(url)


        