read expression
x=`echo "$expression" | bc -l`
printf "%0.3f" $x