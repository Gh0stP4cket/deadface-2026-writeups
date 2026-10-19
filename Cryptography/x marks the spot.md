# X Marks the Spot Created By: @syyntax

## description:
Zero Trace's network sensors picked up this outbound packet from a host registered to Spectre Technology. The payload is hex-encoded. Decrypt it to find what spookyboi is hiding.

02362b2964302c2164372c25202b3337642b226417342127303621641021272c2a2b282b233d7e6420212520222527213f3c2b361b751b263d30771b70301b701b3075297739
Submit the flag as deadface{flag-text}.

## solutions:
Looks like we got a hex-encoded so I tried with hex decoder and other bases decoder to see if we get anything out of it.
![try_decoded](/Cryptography/pic/x-mark-solving1.png)

It's a bunch of nonsense so I come to think of could it be XOR but also we don't know the key to do it. So I visited my old friend again. The dcode.fr.
https://www.dcode.fr/xor-cipher

I let it bruteforce the key and I got the flag out of it. With hexadecimal key: 44 -> which is 'D'
![solved](/Cryptography/pic/x-mark-solved.png)

## flag:
From the shadows of Spectre Technology: deadface{xor_1_byt3_4t_4_t1m3}