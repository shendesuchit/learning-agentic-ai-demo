# Custom Middleware

## Idea

Custom middleware is behavior we define ourselves for a particular application requirement.

## Tiny Python example

```python
def middleware(value: str) -> str:
    print("Before execution")
    result = value.strip()
    print("After execution")
    return result

print(middleware("  hello  "))
```

## What I understood

The important idea is not the exact function above. It is the location of the logic in the execution flow.

## Code relationship

The eventual real examples can live under:

`examples/langchain/middleware/`

and documentation can link directly to their GitHub source.
