
with open('files/input.txt', 'r') as f:
    first, second = map(int, f.read().split())
    result = first + second

    with open('files/output.txt', 'w') as nf:
        nf.write(str(result))
