with open('input.txt', 'r') as f:
    lines = f.readline().strip()

for i in range(len(lines)):
    if len(set(lines[i:i+14])) == 14:
        print(i+14)
        break

