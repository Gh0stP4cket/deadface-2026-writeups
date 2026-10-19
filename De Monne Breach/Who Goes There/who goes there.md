# Who Goes There? Created By: @syyntax

## challenge description:
DEADFACE managed to slip a rogue Kali device onto De Monne Financial’s corporate network. Shortly afterward, someone used a legitimate employee account to access the company file share and steal sensitive documents.

One of those documents later surfaced in Ghost Town, confirming that the breach was more than just suspicious network activity.

ZeroTrace recovered a packet capture and a memory image from the affected environment. Your first task is to identify the De Monne Financial employee account that DEADFACE compromised.

What is the username of the compromised employee? Submit the flag as deadface{username}.

attachment with memory file: memory.7z
## solve:
So, I used volatility workbench to be the tools to see what's going on in there.

I used `windows.consoles.consoles` to be the filter.
![output](/De%20Monne%20Breach/pic/who-goes-there-solve.png)

We can see the username there.
```

Windows PowerShell

Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\nkessler> Test-Path C:\ProgramData\WindowsCache\telemetry.ps1

False

PS C:\Users\nkessler> dir C:\ProgramData\WindowsCache\


```

## flag:
deadface{nkessler}