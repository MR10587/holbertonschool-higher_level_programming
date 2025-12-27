#!/usr/bin/python3
class VerboseList(list):

    def append(self, value):
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, value):
        super().extend(item for item in value)
        print(f"Extended the list with [{len(value)}] items.")

    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, value=-1):
        item = self[value]
        print(f"Popped [{item}] from the list.")
        return super().pop(value)


vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)
