[![Gitlab Pipeline](https://gitlab.com/campfiresolutions/public/gnista.io-python-library/badges/main/pipeline.svg)](https://gitlab.com/campfiresolutions/public/gnista.io-python-library/-/pipelines)  [![Python Version](https://img.shields.io/pypi/pyversions/gnista-library)](https://pypi.org/project/gnista-library/)  [![PyPI version](https://img.shields.io/pypi/v/gnista-library)](https://pypi.org/project/gnista-library/)  [![License](https://img.shields.io/pypi/l/gnista-library)](https://pypi.org/project/gnista-library/)  [![Downloads](https://img.shields.io/pypi/dm/gnista-library)](https://pypi.org/project/gnista-library/) 

# gnista-library
A client library for accessing gnista.io

## Tutorial
### Create new Poetry Project
Navigate to a folder where you want to create your project and type
```shell
poetry new my-gnista-client
cd my-gnista-client
```

### Add reference to your Project
Navigate to the newly created project and add the PyPI package
```shell
poetry add gnista-library
``` 

### Your first DataPoint
Create a new file you want to use to receive data this demo.py

```python
from gnista_library import KeyringGnistaConnection, GnistaDataPoint, GnistaDataPoints

connection = KeyringGnistaConnection()

data_point_id = "56c5c6ff-3f7d-4532-8fbf-a3795f7b48b8"
data_point = GnistaDataPoint(connection=connection, data_point_id=data_point_id)

data_point_data = data_point.get_data_point_data()

print(data_point_data)
```

You need to replace the `DataPointId` with an ID from your gnista.io workspace.

For example the DataPointId of this DataPoint `https://aws.gnista.io/secured/dashboard/datapoint/4684d681-8728-4f59-aeb0-ac3f3c573303` is `4684d681-8728-4f59-aeb0-ac3f3c573303`

### Run and Login
Run your file in poetry's virtual environment
```console
$ poetry run python demo.py
2021-09-02 14:51.58 [info     ] Authentication has been started. Please follow the link to authenticate with your user: [gnista_library.gnista_connetion] url=https://aws.gnista.io/authentication/connect/authorize?client_id=python&redirect_uri=http%3A%2F%2Flocalhost%3A4200%2Fhome&response_type=code&scope=data-api%20openid%20profile%20offline_access&state=myState
```
In order to login copy the `url` into your Browser and Login to gnista.io or, if allowed a browser window will open by itself.

### Keystore
Once you loggedin, the library will try to store your access token in your private keystore. Next time you run your programm, it might request a password to access your keystore again to gain access to gnista.io
Please take a look at [Keyring](https://pypi.org/project/keyring/) for details.

## Advanced Example
### Show received Data in a plot
```shell
poetry new my-gnista-client
cd my-gnista-client
poetry add gnista-library
poetry add structlib
poetry add matplotlib
```

```python
import matplotlib.pyplot as plt
from structlog import get_logger

from gnista_library import KeyringGnistaConnection, GnistaDataPoint, GnistaDataPoints

log = get_logger()

connection = KeyringGnistaConnection()

data_point_id = "56c5c6ff-3f7d-4532-8fbf-a3795f7b48b8"
data_point = GnistaDataPoint(connection=connection, data_point_id=data_point_id)

data_point_data = data_point.get_data_point_data()
log.info("Data has been received. Plotting")
data_point_data.plot()
plt.show()

```

### Filter by DataPoint Names
```shell
poetry new my-gnista-client
cd my-gnista-client
poetry add gnista-library
poetry add structlib
poetry add matplotlib
```

```python
import matplotlib.pyplot as plt
from structlog import get_logger

from gnista_library import KeyringGnistaConnection, GnistaDataPoint, GnistaDataPoints

log = get_logger()

connection = KeyringGnistaConnection()

dataPoints = GnistaDataPoints(connection=connection)
data_point_list = list(dataPoints.get_data_point_list())

for data_point in data_point_list:
    log.info(data_point)

# Find Specific Data Points
filtered_data_points = filter(
    lambda data_point: data_point.name.startswith("371880214002"), data_point_list
)
for data_point in filtered_data_points:
    # get the data
    data_point_data = data_point.get_data_point_data()
    log.info(data_point_data)
    data_point_data.plot()
    plt.show()

```



## Links
**Website**
[![gnista.io](https://www.gnista.io/assets/images/gnista-logo-small.svg)](gnista.io)

**PyPi**
[![PyPi](https://pypi.org/static/images/logo-small.95de8436.svg)](https://pypi.org/project/gnista-library/)

**GIT Repository**
[![Gitlab](https://about.gitlab.com/images/icons/logos/slp-logo.svg)](https://gitlab.com/campfiresolutions/public/gnista.io-python-library)