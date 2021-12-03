class Pos():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.aim = 0

    def up(self, change: int) -> None:
        self.aim -= change

    
    def down(self, change: int) -> None:
        self.aim += change


    def forward(self, change: int) -> None:
        print(self.aim)
        print(change)
        self.y += change
        self.x -= self.aim * change

with open("input.txt") as input:
    pos = Pos()
    while True:
        line = input.readline()
        if not line:
            break
        parts = line.split(" ")
        callable = getattr(pos, parts[0])
        amt = int(parts[1])
        callable(amt)
print(pos.x)
print(pos.y)
print(abs(pos.x) * pos.y)

#