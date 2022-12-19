class cargo:
    def __init__(self, numberCrates):
        self.numberCrates = numberCrates
        self.crates = [crateStack() for _ in range(numberCrates)]

    def add_blocks_to_crates(self, items):
        for crate, value in zip(self.crates, items):
            if value != ' ':
                crate.add_block_on_top(value)

    def move_blocks(self, amount, source, target, moveMultiple):
        movingCrates = self.crates[source].take_x_crates(amount, moveMultiple)
        self.crates[target].add_crates(movingCrates)

    def get_top_stacks(self):
        return_message = ""
        for crate in self.crates:
            return_message += crate.get_top_content()
        return return_message    

class crateStack:
    def __init__(self) -> None:
        self.content = []

    def add_block_on_top(self, item):
        self.content.append(item)

    def take_x_crates(self, x, move_multiple):
        returnCrates = self.content[-x:]
        self.content = self.content[:-x]
        if move_multiple:
            return returnCrates
        else:
            return reversed(returnCrates)
    
    def add_crates(self, newCrates):
        self.content += newCrates

    def get_top_content(self):
        return self.content[-1] if len(self.content) > 0 else ""


def follow_Inputs(fileName, part2=False):
    with open(fileName, 'r') as f:
        lines = f.readlines()
        lines = [entry for entry in lines]

    numberCrates = len(lines[0])//4
    cargoBay = cargo(numberCrates)

    crate_lines = lines[:lines.index('\n')-1]

    for line in reversed(crate_lines):
        values = list(line)[1:-1:4]
        cargoBay.add_blocks_to_crates(values)
    
    moving_lines = lines[lines.index('\n')+1:]
    for line in moving_lines:        
        amount, source, target = [int(entry) for entry in line.strip().split(' ') if entry.isdigit()]
        cargoBay.move_blocks(amount, source-1, target-1, part2)
    
    print(cargoBay.get_top_stacks())

if __name__ == "__main__":
    follow_Inputs('input.txt',part2=False)
    follow_Inputs('input.txt',part2=True)


