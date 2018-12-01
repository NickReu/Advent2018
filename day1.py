data = open("input1").read().split()

#test = "+7, +7, -2, -7, -4"
#data = test.split(", ")

sum = 0
prev_sums = [0]
done = False
while(not done):
    for i in data:
        if i[0] == "+":
            sum += int(i[1:])
        else:
            sum -= int(i[1:])
        if sum not in prev_sums:
            prev_sums.append(sum)
        else:
            done = True
            break

print(sum)
