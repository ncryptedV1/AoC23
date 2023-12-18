def custom_hash(text):
    val = 0
    for char in text:
        val += ord(char)
        val *= 17
        val %= 256
    return val

with open("in15.txt", "r") as file:
    sequence = file.readline().strip()
    res = 0
    for step in sequence.split(','):
        res += custom_hash(step)
    print(res)
