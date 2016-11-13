#user enters a string and a substring.
#prints the number of times that the substring occurs in the given string. 

#Sample Input
#
#ABCDCDC
#CDC
#Sample Output
#
#2

input_string = input().strip()
input_sub_string = input().strip()
sub_string_len = len(input_sub_string)
count=0
match_list = [input_string[i:i+sub_string_len] for i in range(0,len(input_string)-sub_string_len+1) if input_string[i:i+sub_string_len]==(input_sub_string)]
print(len(match_list))