nrs = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("in1.txt", "r") as file:
    input = file.readlines()
    res = 0
    for line in input:
        first = None
        last = None
        idx = 0
        while idx < len(line):
            # check numeric first
            found_nr = None
            if line[idx].isdigit():
                found_nr = line[idx]
            else:
                for text, nr in nrs.items():
                    final_idx = idx + len(text)
                    if final_idx >= len(line):
                        continue
                    if line[idx:final_idx] == text:
                        found_nr = str(nr)
                        break

            if found_nr is not None:
                if first is None:
                    first = found_nr
                last = found_nr
            idx += 1
        res += int(first + last)

    print(res)
