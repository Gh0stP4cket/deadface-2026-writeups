# DECODE-DLE Created By: @G2Gh0st

## challenge description:

One of the junior DEADFACE members left a number puzzle to decipher a 3-digit number combination. 
Do you have the skills to solve the puzzle and open the lock? Follow the clues to decipher 
the 3-digit code needed to "pick" the lock. Enter the code as 3 digits, no spaces or other 
separating characters.

Submit the flag as deadface{###}

attachment:

![decoddle](/assets/crypto/decode-Dle-chal.png)

## solution

so in the picture we have three digits pin that we have to figure out.

1. I looked at the second line first which eliminate 2, 5, and 0 from the pin answer for sure 
2. On the forth line it tells me that one number is correct and in the right place so we excluded the 5 and we have 7 and 3.
3. If number 3 is correct then on the forth line should be in the middle but on first line said if number three is correct but in the wrong place that means the two numbers that it can be is 3 with 6 or 8 but on the third line is said two numbers are correct which included 6 and 8 so, three could not be in the pin.
4. Now we eliminated 2, 3, 5, and 0. And we know now that 7 is in the right spot which is the first digit of the pin.
5. The last line is said two numbers are correct but in the wrong place we know 7 is one of the numbers so possibly it could be 6 or 8. Back at the line three we also know two numbers are correct but in the wrong place. So one can't be the first digit because seven took that already so, if 6 correct then it needs to be at the end of the pin because on the first and last lines told us it's the wrong place.
6. Currently we got 7_6 now we have to find the middle which could be 1 or 8. So the first line we can eliminate 8 since it told use that one number is correct but in the wrong position we know that it's 6. So the remaining spot is for 1.

## flag
deadface{716}