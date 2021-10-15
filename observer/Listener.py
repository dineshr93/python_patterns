from event import subscribe
from dataclasses import dataclass as dc


class Listener:
    def someFunc(data: str):
        print(f'This is someFunc {data}')

    def someFunc2(data: str):
        print(f'This is someFunc2 {data}')


def register():
    subscribe('log', Listener.someFunc)
    subscribe('log', Listener.someFunc2)
