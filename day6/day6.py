with open('input.txt', 'r') as f:
    lines = f.readline().strip()

for i in range(len(lines)):
    if len(set(lines[i:i+4]))==4:
        print(i+4)
        break