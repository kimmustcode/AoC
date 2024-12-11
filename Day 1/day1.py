def dist(x, y):
    return max(x,y) - min(x,y)

def similar(test_num, arr):
    total = 0 

    for i in range(len(arr)):
        if arr[i] > test_num: 
            return test_num * total  
        elif arr[i] == test_num:
            total += 1
            i += 1  
        else:
            i += 1 
    


filename = "input.txt"  
sim_sum = 0
dist_sum = 0 
l1 = []
l2 = [] 

with open(filename) as file:
    lines = [line.rstrip() for line in file]

for line in lines: 
    text_num1 = ''
    text_num2 = ''
    switch_to_num2 = False

    for char in line: 
        if char == ' ': 
            switch_to_num2 = True
        
        if switch_to_num2 == False: 
            text_num1 = text_num1 + char

        else: 
            text_num2 = text_num2 + char 

    l1.append(int(text_num1))
    l2.append(int(text_num2))

l1.sort()
l2.sort()

for num in l1: 
    sim_sum += similar(num, l2)

for i in range(len(l1)):
    dist_sum += dist(l1[i], l2[i])


print(sim_sum, dist_sum)