from collections import namedtuple
import typing as t


Event = namedtuple("Event", ["start", "end"])
Endpoint = namedtuple("Endpoint", ["start", "is_start"])

def find_max_simultaneous_events(array: t.List[Event]):
    events = [Endpoint(e.start, True) for e in array] + [Endpoint(e.end, False) for e in array]
    events.sort(key=lambda x: x.start)

    num_events = 0
    max_events = 0
    for event in events:
        if not event.is_start:
            num_events -= 1
        else:
            num_events += 1
        max_events = max(num_events, max_events)
    return max_events


def main():
    array = [Event(1,5), Event(6,10), Event(11,13), Event(14,15), Event(2,7), Event(8,9), Event(12,15), Event(4,5), Event(9,17)]
    print(find_max_simultaneous_events(array))


if __name__ == "__main__":
    main()
 