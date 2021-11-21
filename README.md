# Apply

Some experiments with chaining of function calls, somewhat similar to [JulienPalard/Pipe](https://github.com/JulienPalard/Pipe), but without need to rewrite each function to a `Pipe` class, and you can just use standard `map` and `filter` functions (and also I don't like using of SQL-like keywords in unnatural order, and `select` doesn't associates with mapping IMO).

```python
from apply import apply, Partial

items = list(range(10))

print(
    items @ apply
    | filter @ Partial(lambda item: item % 2 == 0)
    | map @ Partial(lambda item: item // 2)
    > sum
)

# Output: 10
```

This construction:

```python
items @ apply
| filter @ Partial(lambda item: item % 2 == 0)
| map @ Partial(lambda item: item // 2)
> sum
```

Is equivalent to

```python
sum(map(lambda item: item // 2, filter(lambda item: item % 2 == 0, items)))
```

In short, `apply` (`Applicator` object) applies to the object at the left of `@` operator all following functions divided with `|` operator (each `apply | func` returns new `Applicator` object which contains `func(apply.value)` value), and returns result of a function preceded with `>` operator (`apply > func` returns `func(apply.value)`, not another `Applicator`).

`Partial` object just wraps a function to the left of the `@` operator into `partial`:

```python
filter @ Partial(lambda item: item % 2 == 0)
# equivalent to
partial(filter, lambda item: item % 2 == 0)
```

