print(max(sum(map(int,i.split()))
for i in open('input.txt').read().split('\n\n')))

print(sum(sorted(sum(map(int,j.split()))
for j in open('input.txt').read().split('\n\n'))[-3:]))