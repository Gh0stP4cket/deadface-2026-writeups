import os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Challenge')

p = open(os.path.join(base, 'relay-heartbeat.json'), 'rb').read()
c = open(os.path.join(base, 'relay-heartbeat.enc'), 'rb').read()
t = open(os.path.join(base, 'relay-tasking.enc'), 'rb').read()

k = bytes(a ^ b for a, b in zip(p, c))        # recover keystream
print(bytes(a ^ b for a, b in zip(t, k)))     # decrypt tasking