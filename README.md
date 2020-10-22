### Gradient Services API (v.0.1)

### For Development:

Generate and Activate virtual env:
```shell script
python -m venv gradientenv
source gradientenv/bin/activate
```
Install requirements:

```shell script
pip install -r requirements.txt
```

Create `.env` file at root, and add an `API_KEY` for Swagger/ReDoc. To create `API_KEY`, run from Python terminal:
```shell script
import uuid
print(str(uuid.uuid4()))
```
Also, add the following to `.env`:
```shell script
IS_DEBUG=False
DEFAULT_CONFIG_JSON_PATH=/core/config.json
DEFAULT_LOG_PATH=/logs/logs.log
```
For local development, also add the following to `.env`:
```shell script
LOCAL_USER = <LDAP username>
LOCAL_PASSWORD = <LDAP password>
```



#### Final `.env` file should contain the following:

```shell script
API_KEY=<API_KEY>
IS_DEBUG=False
DEFAULT_CONFIG_JSON_PATH=/core/config.json
DEFAULT_LOG_PATH=/logs/logs.log

API_PREFIX=/api/v01
APP_NAME=GRADIENT
APP_VERSION=0.1.0

LOCAL_USER=<LDAP username>
LOCAL_PASSWORD=<LDAP password>
```

### To run locally:
```shell script
uvicorn gradient.main:app
```

### To run tests:
```shell script
python -m pytest tests -v
```


### To run coverage:
```shell script
pytest --cov=gradient tests/
```

#### Note on File Structure and Current Endpoints:

A "relic" endpoint is found at `gradient > api > routes > crawler_content_routes`, which should be treated as a skeleton endpoint for templating.

#### Note on Docs:

Once running (either locally or in production), the Swagger instance may be found at `<BASE_URL>/docs` .