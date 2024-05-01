var1 = eval(input('Enter First Number : '))
var_oper = input('Enter an operator to perform operation : ')
var2 = eval(input('Enter Second Number : '))
if var_oper == '*':
    print('The multiplication of your num is : ',var1*var2)
elif var_oper == '+':
    print('The addition of your num is : ',var1+var2)
elif var_oper == '-':
    print('The subtraction of your num is :',var1-var2)
elif var_oper == '/':
    print('The division of your num is : ',var1/var2)
elif var_oper == '%':
    print('The mod of your num is : ',var1%var2)
else:
    print('Plz Enter +,-,/,*,% .operator to perform operation on it.')    