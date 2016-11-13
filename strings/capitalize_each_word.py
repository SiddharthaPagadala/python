#You are given a string . Your task is to capitalize each word of .
input_string = ' '.join([str.capitalize() for str in input().strip().split(' ')])
print(input_string)