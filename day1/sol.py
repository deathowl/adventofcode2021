larger = 0
with open("input.txt") as input:
    previous = int(input.readline())
    while True:
        try:
            curr = int(input.readline())
            if curr > previous:
                larger+=1
            previous = curr
        except ValueError: # '' cannot be parsed to int, and wil raise
            break
print(larger)