# DIAMBRA™ Arena Engine API Client

This packages provides a low level API client for the DIAMBRA™ Arena Engine API.

Most users will want to use the higher level [diambra-arena](https://pypi.org/project/diambra-arena/) package instead.

## Usage
```python
import diambra.arena.engine

client = diambra.arena.engine.Client("127.0.0.1:49154")

client.Shutdown(diambra.arena.engine.model.Empty())
```
