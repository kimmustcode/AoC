filename = "input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

reports_list = [] 

line_counter = 0 
for line in lines: 
    report = [] 
    num = ''
    for char in line: 
        if char == ' ': 
            report.append(int(num))
            num = ''

        num = num + char
    report.append(int(num))
    reports_list.append(report)

def direction(x, y):
    if x > y: 
        new_direction = -1
    elif x < y: 
        new_direction = 1 
    else:
        new_direction = 0
    return new_direction

def compare_level(report): 
    buffer = 0 
    current_direction = 0 
    i = 0 

    for level in report:
        if i == 0: 
            buffer = level 
            
        else:
            new_direction = direction(buffer, level)

            if i == 1:
                current_direction = new_direction
           
            if new_direction != current_direction:
                return False  
            
            diff = abs(level - buffer)
            
            if diff > 3: 
                return False  
            
            buffer = level
            
        i += 1 
    return True      

unsafe = 0 
safe = 0
i = 0 
for report in reports_list:
    i += 1
    
    safety_level = compare_level(report)
        
    if  safety_level == False:
        
        unsafe += 1 
    elif safety_level == True: 
        print(i, report, "|| SAFE")
        safe += 1 
    
print(safe, unsafe)