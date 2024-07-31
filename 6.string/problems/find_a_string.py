def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)