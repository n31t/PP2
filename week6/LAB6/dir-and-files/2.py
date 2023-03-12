import os
print('Path exists:', os.access(
    r'/Users/adilovamir/Desktop/PP2', os.F_OK))
print('Path readable:', os.access(
    r'/Users/adilovamir/Desktop/PP2', os.R_OK))
print('Path writable:', os.access(
    r'/Users/adilovamir/Desktop/PP2', os.W_OK))
print('Path executable:', os.access(
    r'/Users/adilovamir/Desktop/PP2', os.X_OK))
