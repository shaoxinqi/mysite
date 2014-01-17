#! /bin/sh
if [ -f log.txt ] ; then
    awk -F " " '{ print $1 }' log.txt > ip_tmp
    cat ip_tmp | sort -u
    total=`sort ip_tmp -u | wc -l`
    echo "There are $total IP addresses in log."
else
    echo "Can not find log.txt!"
fi
