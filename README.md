# Python SDK

## Installation

```
pip install plenigo-python
```

## Usage

```python
from collections import OrderedDict
from plenigo.client.http_client import PlenigoApiType
from plenigo.client.http_client import PlenigoHTTPClient
from plenigo.entities.accessRight import accessRight

apiKey = "yourApiKeyGoesHere"

client = PlenigoHTTPClient(PlenigoApiType.LIVE, apiKey)
customerId = "yourCustomerId"
data = OrderedDict()

params = {
    "lifeTimeStart": "2019-01-01T07:53:23.450961Z",
    "lifeTimeEnd": "2020-01-01T07:53:23.450961Z",
    "accessTimeStart": "06:00:00",
    "accessTimeEnd": "18:00:00",
    "maxCacheDate": "2020-01-01T07:53:23.450961Z",
    "accessRightUniqueId": "100000",
    "blocked": False,
}

ar = AccessRight.create(client, customerId, params)
print(ar)
```
