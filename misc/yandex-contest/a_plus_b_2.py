
with open('input.txt', 'r') as f:
    first, second = map(int, f.read().split())
    result = first + second

    with open('output.txt', 'w') as nf:
        nf.write(str(result))
