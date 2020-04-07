read n
function printer
{
    x=$((2**$((6-$1))))
    y=$(($((2**$1))-1))
    lim=$(($((99-x*y))/2))
    if(( $1 > $n))
    then 
        for ((i=0;i<$x;i++))
        do 
            for ((j=0; j<100; j++))
            do
                printf "_"
            done
            echo ""
        done
        printer $(($1-1))
        return
    fi
    for ((i=0;i<$x;i++))
    do 
        for ((j=0;j<$lim;j++))
        do
            printf "_"
        done
        flag=1
        for ((j=0;j<=$((x*y));j++))
        do
            if((i<$((x/2))))
            then
                if (( $((j % x)) == $i || $((j % x)) == $((x-i)) ));
                then
                    if (( flag == "1" || flag == "2" || i == "0"));
                    then
                        flag=$(($((flag+1))%4))
                        printf "1"
                    else
                        flag=$(($((flag+1))%4))
                        printf "_"
                    fi        
                else
                    printf "_"
                fi
            else
                if (( $((j % $((x/2)))) == "0" && $((j % x)) != "0" ));
                then   
                    if (( flag == "1"));
                    then
                        flag=0    
                        printf "1"
                    else
                        flag=1
                        printf "_"
                    fi
                else
                    printf "_"
                fi    
            fi    
        done
        for ((j=0;j<=$lim;j++))
        do
            printf "_"
        done    
        echo ""
    done
    if (( "$1" == "1" ));
    then
        return
    fi
    printer $(($1-1))
    return
}
printer 5
