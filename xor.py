import os

with open("input.jpg", "rb") as file:
    data = file.read()

for key in range(256):
    xored_data = bytearray(b ^ key for b in data)
    if xored_data[:4] == b"\x64\x65\x78\x0A":
        with open("output.dex", "wb") as output_file:
            output_file.write(xored_data)
        print("Found dex xor key:", hex(key))
    if xored_data[:4] == b"\xFF\xD8\xFF\xE1":
        with open("output.jpg", "wb") as output_file:
            output_file.write(xored_data)
        print("Found jpg xor key:", hex(key))
    if xored_data[:4] == b"\x50\x4B\x03\x04":
        with open("output.zip", "wb") as output_file:
            output_file.write(xored_data)
        print("Found zip xor key:", hex(key))
    
