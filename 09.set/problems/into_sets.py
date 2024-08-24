def average(array):
    sum_distinct_heights = sum(set(array))
    no_of_distinct_height = len(set(array))
    
    avg = round(sum_distinct_heights/no_of_distinct_height, 3)
    
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)