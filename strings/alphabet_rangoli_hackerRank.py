#You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
#
#Sample Input
#
#5
#Sample Output
#
#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------
n = int(input().strip())
alphabets = list(map(chr,range(97,123)))
comp_list_1 = [alphabets[i] for i in range(n-1,-1,-1)]
comp_list_2 = [alphabets[i] for i in range(1,n)]
comp_list = comp_list_1 + comp_list_2

len_comp_list = len(comp_list)
for i in range(0, n):
    print(('-'.join(comp_list[:i]+comp_list[len_comp_list-i-1:])).center(len_comp_list*2-1,'-'))
for i in range(n-2, -1,-1):
    print(('-'.join(comp_list[:i] + comp_list[len_comp_list - i - 1:])).center(len_comp_list * 2 - 1, '-'))