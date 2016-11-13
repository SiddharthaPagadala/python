input_string = input().strip()
n = len(input_string)
k = int(input().strip())
import textwrap
s = textwrap.wrap(input_string,k)
print(*["".join(sorted(set(i), key=i.index)) for i in s],sep='\n')

for i in range(0,n,k):
    print("".join(sorted(set(input_string[i:i+k]), key=input_string[i:i+k].index)))