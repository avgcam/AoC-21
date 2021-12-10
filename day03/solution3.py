import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

input_file = open('input3.txt').read().splitlines()

def part1():
    y = [[z[i] for z in input_file] for i in range(len(input_file[0]))]
    gamma = int(''.join([max(x, key = x.count) for x in y]),2)
    epsilon = int(''.join([min(x, key = x.count) for x in y]),2)

    return print('Part1 Answer: ', gamma*epsilon)
    
def part2():
    ogr = input_file.copy()
    idx = 0  
    while len(ogr) > 1:
        grouped_by_idx = [num[idx] for num in ogr]
        max_index = str(int(grouped_by_idx.count('1') >= grouped_by_idx.count('0')))
        ogr = [num for num in ogr if num[idx] == str(max_index)]
        idx += 1
    ogr = int(''.join(ogr[0]),2)
    
    co2 = input_file.copy()
    idx = 0 
    while len(co2) > 1:
        grouped_by_idx = [num[idx] for num in co2] 
        min_index = str(int(grouped_by_idx.count('1') < grouped_by_idx.count('0')))
        co2 = [num for num in co2  if num[idx] == min_index]
        idx +=1 
            
    co2 = int(''.join(co2[0]),2)
    
    return print('Part2 Answer: ', ogr*co2)

def main():
    part1()
    part2()
 
if __name__ == '__main__':
    main()