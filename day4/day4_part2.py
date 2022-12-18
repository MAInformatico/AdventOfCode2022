def isIncluded(first_pair, second_pair):
    init_first, end_first = map(int, first_pair.split('-'))
    init_second, end_second = map(int, second_pair.split('-'))
    return init_second <= init_first and end_first <= end_second

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        values = [i.strip() for i in lines]

    count = 0
    overlapped = 0
    for pair in values:
        first_pair, second_pair = pair.split(',')        
        if isIncluded(first_pair, second_pair) or isIncluded(second_pair, first_pair):
            count += 1
        init_first, end_first = map(int, first_pair.split('-'))
        init_second, end_second = map(int, second_pair.split('-'))
        if init_first in range(init_second, end_second+1) or end_first in range(init_second, end_second+1) or  init_second in range(init_first, end_first+1) or end_second in range(init_first, end_first+1):
            overlapped += 1
    
    print(count)
    print(overlapped)