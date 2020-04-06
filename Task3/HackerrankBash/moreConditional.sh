read x
read y
read z
 if   (( x != z && x != y && y != z )); 
 then 
    echo "SCALENE"
elif (( x == y && x == z )); 
then 
    echo "EQUILATERAL"
else                                        
    echo "ISOSCELES"
fi
