string = input()
dic = [-1 for i in range(ord('a'), ord('z')+1)]
for index, char in enumerate(string):
    if dic[ord(char)-ord('a')] == -1:
        dic[ord(char) - ord('a')] = index

for i in dic:
    print(i,end=' ')