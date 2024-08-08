# zip() function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.



N, X = input().split()
subjects = []

for _ in range(int(X)):
    subjects.append(list(map(float, input().split())))
    
for x in zip(*subjects):
    print(sum(x)/len(x))
