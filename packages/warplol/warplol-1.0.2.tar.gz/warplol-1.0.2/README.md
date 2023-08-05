# A simple yet powerful SDK for warp.lol

## Short a URL

```py
from warplol import WarpLol

url = WarpLol.getshort(URL) # URL is the url that you want to short, with or without https://
print(url) # return shorted URL
```

## Get shorted url redirect

```py
from warplol import WarpLol

url = WarpLol.geturl(URL) # URL is the warp.lol URL. It can both be the full url (https://warp.lol/BbSg, with or without https://) or the last part (BbSg)
print(url) # return the full redirect (https://google.com for example)
```
