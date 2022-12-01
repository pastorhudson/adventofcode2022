with open('day1.txt') as f:
    richest_elf = 0
    lines = f.read()

    for elf in lines.split("\n\n"):
        int_enf = [float(i) for i in elf.split("\n")]
        if sum(int_enf) > richest_elf:
            richest_elf = sum(int_enf)

    print(f"The richest Elf has {richest_elf} calories.")