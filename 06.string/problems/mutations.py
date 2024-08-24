def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = "".join(lst)
    return string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)