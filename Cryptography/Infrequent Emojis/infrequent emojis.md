# Infrequent Emojis Created By: @Cyan

## Challenge description:
While DoomScrolling, our intel team came across a weird coded post with emojis all over it. One of our experts claims that the patterns point to it still being English but we don't know what it means! Can you figure it out?

Submit the answer as deadface{flag_text}

link: https://doomscroll.dctf.io/

## solve:

I went through the website until I found the post that related to emoji which is https://doomscroll.dctf.io/post/252
![emoji-post](/assets/crypto/emoji-chall.png)

I already know the flag format which is deadface{...}. I can interpreate the already known emoji to that letters.

🪦 = d
🕯️ = e
💀 = a
🪦 = d
🩸 = f
💀 = a
⚰️ = c
🕯️ = e 
{
🦉🕸️🕯️💀🌙🕯️_
☣️🔮🧪_
🖤🌩️☣️_
⛓️🧪_
🦇🕯️🔥_
🌙☣️💀🦇🪦💀🔮🪦
}

deadface{--ea-e_---_---_--_-e-_--a-da-d}

The first word could be please
🌙 = s
last word we can interpret standard
☣️ = t, 🦇 = n, 🔮 = r

so now we got deadface{please_tr?_??t_??_ne?_standard}
Now it's readable we know tr? is try for sure and the ne? is new.
deadface{please_try_--- --_new_standard}

now we can fully solve it with command sense
deadface{please_try_out_my_new_standard}

## flag
deadface{please_try_out_my_new_standard}
