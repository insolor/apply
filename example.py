from apply import apply, Partial

items = list(range(10))

print(
    items @ apply
    | filter @ Partial(lambda item: item % 2 == 0)
    | map @ Partial(lambda item: item // 2)
    > sum
)
