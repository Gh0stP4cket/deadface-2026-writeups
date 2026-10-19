# Uninvited Guest Created By: @syyntax

## challenge description:
Nathan's workstation asked the local network to resolve a file-server name. Which corporate IPv4 address supplied the suspicious answer?

Submit the flag as deadface{IP}.

## solve:

I checked the protocol hierarchy first and saw it's mostly IPv4 -> SSH and ARP

![protcol](/De%20Monne%20Breach/pic/protocol-hier-uninvited.png)

Then next I went to check the conversation. We can see that 10.77.10.24 communicated to each other a lot.
![conversation](/De%20Monne%20Breach/pic/conversation-uninvited.png)

so challenge asked for the IPv4 address supplied the suspicious:
10.77.10.66 since it's appears to commnicate a lot with other ips too.

## flag:
deadaface{10.77.10.66}