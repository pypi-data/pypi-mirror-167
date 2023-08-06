# A simple yet powerful SDK for warp.lol

## Short a URL

```py
from warplol import WarpLol

url = WarpLol().Shortcut().getrandom(URL, full=True) 
print(url)
```
URL is the url that you want to short, with or without https://.
The `full` argument is optional; with `full=True`, full warp.lol URL is returned (https://warp.lol/BbSg); with `full=False`, only the warp.lol redirect key is returned (BbSg).

## Get a custom redirect URL
```py
from warplol import WarpLol

url = WarpLol().Shortcut().getcustom(URL, full=True, name="123abc") 
print(url)
```
URL is the url that you want to short, with or without https://.
The `full` argument is optional; with `full=True`, full warp.lol URL is returned (https://warp.lol/BbSg); with `full=False`, only the warp.lol redirect key is returned (BbSg).
`name` is the custom shortcut URL (like https://warp.lol/123abc)

## Get shorted url redirect

```py
from warplol import WarpLol

url = WarpLol.Shortcut().destination(URL)
print(url)
```

`URL` is the warp.lol URL. It can both be the full url (https://warp.lol/BbSg, with or without https://) or the last part (BbSg)
