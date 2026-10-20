# Name to a Face Created By: @syyntax

## challenge description:
A poisoned name answer prompted an SMB authentication attempt. Which username did the workstation send?

Submit the flag as deadface{username}.

Use the PCAP from *Uninvited Guest.

## solve
So use the same file from uninvited Guest. So we need to find the username that the workstation send. So I tried out http filter first to see what it contains.
![](/assets/De%20Monne%20Breach/pic/name-to-face.png)

It seems like there's NTLMSSP. At the packet 2133 I clicked it to see the Authorization tag to find the username and here it is.
![](/assets/De%20Monne%20Breach/pic/name-to-face-solve.png)

## flag
deadface{nkessler}