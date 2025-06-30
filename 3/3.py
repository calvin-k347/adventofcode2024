import re
pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
pattern2 = re.compile("\d+")

with open("3input.txt") as f:
    matches = re.search(pattern , f.read())
    dos = re.search("do()")
    donts = re.search("don't()")
print(matches)
sum = 0
if (next_do_dont == dos[0]):
    dos = dos[1:len(dos)]
else:  
    donts = donts[1:len(dos)]
do = True
for index in matches:
    if dos[0] < index:

    elif donts[0] < index:

    if do:
        mul = f.read()[index:]
        sum += int(m[0]) * int(m[1])



for x in matches:
    m = re.findall(pattern2, x)
    sum += int(m[0]) * int(m[1])
print(sum)