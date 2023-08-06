# fastapi-wraps


## Installation

```shell
pip install fastapi-wraps
```

## Example

```python
def save_request(
    endpoint: Callable[P, Awaitable[RT]],
) -> Callable[P, Awaitable[RT]]:
    @fastapi_wraps(endpoint)
    async def wrapper(
        *args: Any,
        __request: Request = Depends(get_request),
        __db: Db = Depends(get_db),
        **kwargs: Any,
    ) -> RT:
        __db.save(__request)
        response = await endpoint(*args, **kwargs)
        return response

    return wrapper


app = FastAPI()


@app.get("/")
@save_request
async def hello() -> str:
    return "hello"
```

## Why?

To use dependencies provided by FastAPI's DI framework all dependencies have to be declared in the signature of the endpoint.
Hence, the decorator cannot simply use `functools.wraps`, as `functools.wraps` maintains the signature of the wrapped function. The `fastapi_wraps` decorator takes updates the resulting signature by merging parameters from the `wrapper` and the `wrapped` function.
