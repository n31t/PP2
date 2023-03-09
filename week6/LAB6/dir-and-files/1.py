import os
location1 = r'/Users/adilovamir/Desktop/PP2'
print([name for name in os.listdir(location1)])  # everything
print([name for name in os.listdir(location1) if os.path.isdir(
    os.path.join(location1, name))])  # only directories
print([name for name in os.listdir(location1) if not os.path.isdir(
    os.path.join(location1, name))])  # only files
