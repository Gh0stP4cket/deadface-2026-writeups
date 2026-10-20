# The Workstation in the Middle Created By: @syyntax

## challenge description:
The compromised De Monne employee was working at a Windows device. What is that device's hostname? Preserve the capitalization shown in memory.

Submit the flag as deadface{COMPUTER-NAME}.

Use the memory dump evidence from Who Goes There?

## solve:
To find the hostname, we can analyze the Windows registry stored in the memory dump using Volatility 3.

The hostname is stored in the Windows SYSTEM registry hive under the following key: `ControlSet001\Control\ComputerName\ComputerName`

So, I use `windows.registry.printkey.PrintKey` with the Key to start from `ControlSet001\Control\ComputerName\ComputerName`

![result](/assets/De%20Monne%20Breach/pic/workstation-in-the-middle.png)


```
2026-09-25 18:33:30.000000 UTC	0xd208254af000	REG_SZ	\REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName	(Default)	mnmsrvc	False

2026-09-25 18:33:30.000000 UTC	0xd208254af000	REG_SZ	\REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\ComputerName\ComputerName	ComputerName	DMF-WS11-042	False
```

The windows.registry.printkey.Printkey plugin revealed the workstation hostname through the Windows registry's ComputerName key. The recovered hostname is DMF-WS11-042.

## flag:
deadface{DMF-WS11-042}