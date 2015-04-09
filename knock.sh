#!/bin/bash

PORT=`ss -nplt | grep ssh | gawk  -F: '{ print $2 }' | awk '/^[0-9]+/ {print $1}'`
#Create chains and policy
iptables -N ssh-enter
iptables -N inputExt
#Port rules
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -d 127.0.0.1/8 -j DROP
iptables -I INPUT 2 -m state --state ESTABLISHED,RELATED -m recent --rcheck --name ssh-enter -j ACCEPT
iptables -I INPUT 3 -p tcp --dport 3331 -j inputExt
iptables -I INPUT 4 -p tcp --dport 333 -j inputExt
iptables -I INPUT 5 -p tcp --dport 334 -j inputExt
iptables -I INPUT 6 -p tcp --dport $PORT -j inputExt
iptables -A INPUT -m state --state NEW -m recent --name ssh-ability --remove -j DROP

#Chain inputExt rules
iptables -A inputExt -m pkttype --pkt-type broadcast -j DROP
iptables -A inputExt -j DROP
#MOVED TO INPUT //iptables -I inputExt 2 -m state --state ESTABLISHED,RELATED -m recent --rcheck --name ssh-enter -j ACCEPT//
iptables -I inputExt 2 -m state --state NEW -p tcp --dport $PORT -m recent  --rcheck --name ssh-enter -j ACCEPT
iptables -I inputExt 3 -m state --state NEW -p tcp --dport 3331 -m recent --set --name ssh-ability -j DROP
iptables -I inputExt 4 -m state --state NEW -p tcp --dport 3331 -m recent --set --name ssh-ability -j LOG --log-prefix "PortKNOCK Ability has: "
##iptables -I inputExt 4 -m state --state NEW -p tcp --dport 333 -m recent --rcheck --name ssh-ability -j ssh-enter
# MOVED TO INPUT //iptables -I inputExt 6 -m state --state NEW -m recent --name ssh-ability --remove -j DROP//
iptables -I inputExt 5 -m state --state NEW -p tcp --dport 334 -m recent --name ssh-enter --remove -j DROP

#Chain ssh-enter rules
iptables -A ssh-enter -m recent --set --name ssh-enter -j DROP


#Logging(optional)
iptables -I ssh-enter -j LOG --log-prefix "PortKNOCK open FOR: "
