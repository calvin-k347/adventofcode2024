puzzle_input  = "2333133121414131402"
convert = ""
id = 0 
checksum = 0
for i in range(len(puzzle_input)):
    if i % 2 == 0:
        convert += str(id) * int(puzzle_input[i])
        id += 1
    else:
        convert += "." * int(puzzle_input[i])
convert = list(convert)
print("".join(convert))
i = 0
j = len(convert) - 1
while j > i :
    if convert[j] == ".":
        j-=1
    if convert[i] == ".":
        temp = convert[i]
        convert[i] = convert[j]
        convert[j] = temp
        j -=1 
    i +=1
for id, file in enumerate(convert):
    if file == ".":
        break
    checksum += id * int(file)
    
print("".join(convert))
print(checksum)