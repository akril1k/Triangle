
    
def uslov(a, b, c):
    result=""
    if a <= 0 or b <= 0 or c <= 0:
        result= "There are no such triangles"
    if a!=b!=c:
        result= result+"Scalene "
    if a == b or a == c or b == c:
        if a == b == c:
            result= result+"Equilateral "
        else:
            result= result+"Isosceles "
    if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
        result= result+"Right "
        
    return result

#Enter only numbers.
try:   
    print  ('Enter the values of the sides a,b,c respectively')
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    
#Checking that a triangle can be built.
    if a + b > c and a + c > b and b + c > a: 
        print("It's a triangle and it's :") 
        print(uslov(a,b,c))   
    else:
        print("ДИЧ!!!! Are you from our dimension? There are no such triangles!") 

except ValueError:
    print("Please enter only numbers\n")


