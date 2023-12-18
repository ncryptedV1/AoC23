def custom_hash(text):
    val = 0
    for char in text:
        val += ord(char)
        val *= 17
        val %= 256
    return val

with open("in15.txt", "r") as file:
    sequence = file.readline().strip()
    boxes = {x: [] for x in range(256)}
    label_to_focal_len = {}
    for step in sequence.split(','):
        if '=' in step:
            label = step[:-2]
            focal_len = int(step[-1])
            
            box = custom_hash(label)
            if label not in boxes[box]:
                boxes[box].append(label)
            label_to_focal_len[label] = focal_len
        if '-' in step:
            label = step[:-1]

            box = custom_hash(label)
            if label in boxes[box]:
                boxes[box].remove(label)
    res = 0
    for box, lenses in boxes.items():
        for slot, label in enumerate(lenses):
            res += (box + 1) * (slot + 1) * label_to_focal_len[label]
    print(res)
