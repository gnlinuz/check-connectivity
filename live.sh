#!/bin/bash
c=0
con_dead=false
while true
do
	ping -c1 $1 > /dev/null 2>&1
	case $? in 
	0)
		echo is alive
		if $con_dead ; then
			echo send SMS line back online...
		fi
 	  	sleep 4
		con_dead=false
	;;
	*)
		((c++))
		if (($c>3)); then
			if ! $con_dead ; then	
			  echo line is dead...	
	  	 	  echo send SMS connection dead..
			  c=0
			  con_dead=true
			fi
	  	fi
	  	sleep 2
	;;
	esac		
done

