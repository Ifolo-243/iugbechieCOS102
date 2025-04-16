total = 50; # This is global variable.
def sum( agr1, arg2 ):
    # Add both the parameters
    total = arg1 + arg2; # type: ignore
    print ("Inside the function local total : ", total)
    return total;
# Now you acn call sum function
sum( 10, 20);
print ("Outside the function global total : ", total)
