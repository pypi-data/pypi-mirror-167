# WebFiles
Download files hosted on the internet and parse with python


### Core class construct:

```python
import wget

class WebFile:
    def __init__(self, http_address, local_path=None):
        
        self.http_address = http_address
        if local_path:
            self.local_path = local_path
        else:
            self.local_path = os.path.basename(http_address)
            
    def download(self):
        if not os.path.exists(self.local_path):
            wget.download(self.http_address, self.local_path, bar=False)
            
```
