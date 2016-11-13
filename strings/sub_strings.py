input_string = input().strip()
len_input_string = len(input_string)

vowels = ['A','E','I','O','U']
score_Stuart=0
score_Kevin=0

for i in range(len_input_string):
    if input_string[i] in vowels:
        score_Kevin += len_input_string-i
    else:
        score_Stuart += len_input_string-i

if score_Kevin > score_Stuart:
    print('Kevin',score_Kevin)
elif score_Kevin < score_Stuart:
    print('Stuart',score_Stuart)
else:
    print('Draw')