import re 
total = 0
with open("7pt1.txt") as f:
    for line in f:
        target = int(line[0:line.index(":")])
        nums = [int(n) for n in line[line.index(":")+1:].split()]
        n = len(nums)
        good = False
        for i in range(1 << n - 1):
            running = nums[0]
            for j in range(1, n):
                op = (i >> (j-1)) & 1
                if op == 1:
                    running += nums[j]
                else:
                    running *= nums[j]
            if running == target:
                good = True
                break
        total += good * running

    print(total)
        