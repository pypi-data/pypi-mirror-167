from requests import get, post

class WarpLol:
    def __init__(self):
        pass
    
    class Shortcut:
        def __init__(self):
            pass


        def getrandom(self, url: str, **kwargs) -> str:
            if url.startswith('https://') or url.startswith('http://'):
                url = post(f'https://warp.lol/api/v1/shortcut/random', json={"url": url}).text
            else:
                url = 'https://' + url
                url = post(f'https://warp.lol/api/v1/shortcut/random', data={"url": url}).text
            full = kwargs.get("full")
            if full is True or full is None:
                    return f"https://warp.lol/{url}"
            else:
                return url
        
        def getcustom(self, url: str, **kwargs) -> str:
            if kwargs["name"] is None:
                return "No custom name provided"
            else:
                name = kwargs["name"]
                if url.startswith('https://') or url.startswith('http://'):
                    url = post(f'https://warp.lol/api/v1/shortcut/custom', json={"url": url, "name": name}).text
                else:
                    url = 'https://' + url
                    url = post(f'https://warp.lol/api/v1/shortcut/custom', json={"url": url, "name": name}).text
                full = kwargs.get("full")
                if full is True or full is None:
                        return f"https://warp.lol/{url}"
                else:
                    return url

        def destination(self, key: str) -> str:
            if len(key) > 4:
                if key.startswith('https://warp.lol/') or key.startswith('http://warp.lol/') or key.startswith('warp.lol/'):
                    key = key.replace('https://warp.lol/', '')
                    url = get(f'https://warp.lol/api/v1/shortcut/destination?shortcut={key}').text
                    return url
                else:
                    url = get(f'https://warp.lol/api/v1/shortcut/destination?shortcut={key}').text
                    return url
            
            if len(key) == 4:
                url = get(f'https://warp.lol/api/v1/shortcut/destination?shortcut={key}').text
                return str(url)


        