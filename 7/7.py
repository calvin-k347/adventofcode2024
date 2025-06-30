import re 

with open("7pt1.txt") as f:
    for line in f:
        target = int(line[0:line.index(":")])
        nums = [int(n) for n in line[line.index(":")+1:].split()]
        running = 1
        print(nums)
        for n in nums:
            running = running * n
            if running > target:
                running /= n 
                running+= n 
        print(running, " vs ", target)

        