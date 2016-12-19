NUM_ELVES = 3012210

class Elf():

    def __init__(self, label):
        self.label = label
        self.presents = True
        self.next = None


first_elf = Elf(1)
cur_elf = first_elf
i = 2
while i <= NUM_ELVES:
    new_elf = Elf(i)
    cur_elf.next = new_elf
    cur_elf = new_elf
    i += 1

cur_elf.next = first_elf

cur_elf = first_elf

while cur_elf.next is not None:
    elim_elf = cur_elf.next
    if elim_elf.next is cur_elf:
        print cur_elf.label
        break
    new_next = elim_elf.next
    cur_elf.next = new_next
    cur_elf = new_next



