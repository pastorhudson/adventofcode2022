with open('day1.txt') as f:
    richest_elf = 0
    second_elf = 0
    third_elf = 0
    lines = f.read()
    for elf in lines.split("\n\n"):
        int_enf = [int(i) for i in elf.split("\n")]
        # print(int_enf)
        if sum(int_enf) > richest_elf:
            third_elf = second_elf
            second_elf = richest_elf
            richest_elf = sum(int_enf)
        elif sum(int_enf) > second_elf < richest_elf:
            third_elf = second_elf
            second_elf = sum(int_enf)
        elif sum(int_enf) > third_elf < second_elf:
            third_elf = sum(int_enf)

    print(f"The richest Elf has {richest_elf} calories.\n"
          f"Second has {second_elf}\n"
          f"Third has {third_elf}\n"
          f"Total: {sum([richest_elf, second_elf, third_elf])}")