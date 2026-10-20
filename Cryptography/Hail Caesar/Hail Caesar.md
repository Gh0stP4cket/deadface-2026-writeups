# Hail Caesar created By: @syyntax

## challenge description
One of the faculty at Night Veil University thought it would be clever to write 
sensitive information on notes by their computer. This sensitive information includes 
a very easy-to-decipher password hint. Judging by the drawing of a dog on the photo, 
we assume the password hint is the name of the individual's dog.

Submit the flag with the dog's name as: deadface{dog's name}

attachments: ![pass_hint](/assets/crypto/pass_hint.png)

# solution

I typed out the text first which is 
'Zl qbt'f anzr vf Srgpu'

After typed out I noticed that it's ROT-13. So, I visited my old friend which is
https://www.dcode.fr/rot-cipher and put the message through it.

![solve](/assets/crypto/Hail-caesar-solve.png)

We got 'My dog's name is Fetch so I take that and put in for the flag.

# flag
deadface{Fetch}