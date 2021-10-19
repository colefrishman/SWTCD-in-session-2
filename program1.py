def read_sum_write(filename):
    
    if(type(filename) != str):
        raise TypeError("The filename must be a string")

    sum = 0
    with open(filename, 'r') as f:
        while (line := f.readline()):
            sum+=int(line)
        f.close()
    with open(filename, 'a') as f:
        f.write("\n"+str(sum))
        f.close()
    return sum
