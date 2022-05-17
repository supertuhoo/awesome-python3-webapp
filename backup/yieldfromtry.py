def accumulate():
    tally = 0
    while True:
        next = yield
        if next is None:
            return tally
        tally += next


def grouper(tallies):
    while True:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []
acc = grouper(tallies)
next(acc)   # run generator
for i in range(4):
    acc.send(i)
acc.send(None)

