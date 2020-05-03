n = int(input())
List_of_Sizes = list(map(int, input().split()))
Temp = []
for i in List_of_Sizes:
    Temp.append(List_of_Sizes.count(i))
print(max(Temp))