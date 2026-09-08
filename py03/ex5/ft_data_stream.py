#!/usr/bin/env python3
import random
import typing


def gen_event() -> "typing.Generator":
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events_list: list) -> "typing.Generator":
    while events_list:
        e = random.choice(events_list)
        events_list.remove(e)
        yield e


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action {action}")

    ten_events = [next(events) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
