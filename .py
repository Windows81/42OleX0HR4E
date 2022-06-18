from random import Random
from typing import Dict

BEGIN = 0.0
END = 162.0
RANDOM = Random()
SHIFTS: Dict[float, Dict[float, float]] = {
    55.1: {+10: True},
    77.8: {+10: True},
    87.5: {+10: True},
    91.9: {-10: True},
    115.7: {+10: True},
    127.9: {+10: True, -10: True},
    132.1: {+10: True},
    135.3: {-10: True},
    142.1: {-10: True},
}

CODA = [
    (152.0, 152.5),
    (142.5, 143.0),
    (133.0, 133.5),
    (123.5, 124.0),
    (114.0, 114.5),
    (104.5, 105.0),
    (95.0, 95.5),
    (85.5, 86.0),
    (76.0, 76.5),
    (66.5, 67.0),
    (57.0, 57.5),
    (47.5, 48.0),
    (38.0, 38.5),
    (28.5, 29.0),
    (19.0, 19.5),
    (9.5, 10.0),
]


def determine(k: float, last: float) -> bool:
    # return len(SHIFTS[k]) == 1 # True for all shifts, except for the one with the animatronic clone.
    return RANDOM.randint(0, 1) > 0  # Random selection.


def find(v: float) -> float:
    return next((k for k in SHIFTS if k > v), None)


def select(k: float, last: float) -> float:
    if not determine(k, last):
        return 0
    v = SHIFTS[k]
    if v.get(last, False):
        return last
    rest = [d for d, b in v.items() if b and d != last]

    l = len(rest)
    if last != 0 and l >= 2:
        return RANDOM.choice(rest)
    elif l == 1:
        return rest[0]
    return 0


def process():
    s = 0
    l = []
    b = e = BEGIN
    while True:
        while True:
            e = find(e)
            if len(l) > 0x100 or e is None:
                l.extend([(b, END), *CODA])
                return l
            s = select(e, s)
            if s != 0:
                break
        l.append((b, e))
        b = e = e + s


with open(".txt", "w") as f:
    p = [i for _ in range(127) for i in process()]
    a = [
        f"{i}\n"
        for (b, e) in p
        for i in ["file cr.mp4", f"inpoint {b}", f"outpoint {e}"]
    ]
    f.writelines(a)
