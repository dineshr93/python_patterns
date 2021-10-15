subscriber = dict()


def subscribe(name: str, fn):
    if name not in subscriber:
        subscriber[name] = []
    subscriber[name].append(fn)


def provider(name: str, data: str):
    for fn in subscriber[name]:
        fn(data)
