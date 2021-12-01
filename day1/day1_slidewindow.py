larger = 0
with open("input.txt") as input:
    readings = [int(input.readline()), int(input.readline()), int(input.readline())]
    while True:
        try:
            curr = int(input.readline())
            prev_sum = sum(readings)
            readings.pop(0)
            readings.append(curr)
            curr_sum = sum(readings)
            if curr_sum > prev_sum:
                larger+=1
        except ValueError: # '' cannot be parsed to int, and wil raise
            break
print(larger)