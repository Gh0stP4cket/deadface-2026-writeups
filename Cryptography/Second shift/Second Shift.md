# Second Shift Created By: @syyntax

## challenge description:
ZeroTrace recovered several files from a DEADFACE relay server shortly before the host went offline. The relay appears to have been used by mort1cia to exchange operational messages with other DEADFACE members.

One routine transmission was preserved both before and after processing by the relay. A second outbound transmission was recovered only in its processed form.

Determine what DEADFACE was preparing to do next and recover the flag.

Submit the flag as deadface{flag-text}.

## analysis:
So inside the zip file it contained:
1. relay-heartbeat.enc
2. relay-heartbeat.json
3. relay-tasking.enc

The heartbeat.json is a plaintext heartbeat message (251 bytes), heartbeat.enc is the same heartbeat after relay processing and the relay tasking is the second transmission.

inside json:
```
{"type":"heartbeat","host":"relay-07","user":"mort1cia","status":"ok","queue":3,"channel":"ops","timestamp":"2026-10-16T23:41:08Z","message":"No anomalies detected. Continuing scheduled relay checks.","build":"relay-agent-3.8.14","region":"us-south"}
{"type":"heartbeat","host":"relay-07","user":"mort1cia","status":"ok","queue":3,"channel":"ops","timestamp":"2026-10-16T23:41:08Z","message":"No anomalies detected. Continuing scheduled relay checks.","build":"relay-agent-3.8.14","region":"us-south"}
````

1. The two .enc files are in similar size (250 & 220 bytes) the processing is length-preserving. So it's the xor encryption.
2. Both of the files start with the same 9 bytes which are the shared plaintext prefix {"type":". So the same plaintext at the same position -> reuse nonce and using the same keystream.
![show-bytes](/Cryptography/pic/hex-second-shift.png)
3. Now we have to just recover the keystream by xor the plaintext with the ciphertext then recover teh tasking_plaintext by xor keystream with teh relay-tasking.enc

## code
``` python
import os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Challenge')

p = open(os.path.join(base, 'relay-heartbeat.json'), 'rb').read()
c = open(os.path.join(base, 'relay-heartbeat.enc'), 'rb').read()
t = open(os.path.join(base, 'relay-tasking.enc'), 'rb').read()

k = bytes(a ^ b for a, b in zip(p, c))        # recover keystream
print(bytes(a ^ b for a, b in zip(t, k)))     # decrypt tasking
```

![solved](/Cryptography/pic/second-shift-solved.png)

b'{"type":"tasking","target":"aurora-vpn","action":"stage-access","window":"00:30Z","operator":"mort1cia","note":"Use the backup tunnel. Archive bundle under DEADFACE{ctr_nonce_reuse_breaks_confidentiality} before exfil."}'

## flag:
deadface{ctr_nonce_reuse_breaks_confidentiality}