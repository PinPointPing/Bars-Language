import numpy as np
import json
import cv2
import sys

with open('bars.json', 'r') as f: bars = json.loads(f.read())

while True:
    text = input("Enter Text: ")
    if not text:
        print("Please supply text for encryption.")
        continue
    break

encoded = []
for char in list(map(str, text.lower())):
    for bar in bars:
        if char == bar[0]:
            encoded += bar[1:]
            continue

out = ""
for i in range(len(encoded)):
    out += str(encoded[i])
    if (i+1) % 5 == 0:
        print(out)
        out = ""

gap = 100
img = np.zeros((300,len(encoded)*gap +10, 1), np.uint8)
img.fill(255)

for i, encode in enumerate(encoded):
    if encode == 1: cv2.line(img,(i*gap +10, 300),(i*gap +10, 0), 0, 25)
    if encode == 0: cv2.line(img,(i*gap +10 ,150),(i*gap +10, 300), 0, 25)


if input("Would you like to save image to file (y/n)? ") == "y": cv2.imwrite("generated.png", img)