#Given an integer, , print the following values for each integer  from  to :
#
#Decimal
#Octal
#Hexadecimal (capitalized)
#Binary
#The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .

input_int = int(input().strip())

bin_length = len(format(input_int,'b'))

l = [ [format(i,'d').rjust(bin_length),format(i,'o').rjust(bin_length),format(i,'x').upper().rjust(bin_length),format(i,'b').rjust(bin_length)]for i in range(1,input_int+1)]

for s in l:
    print(*s,sep=" ")