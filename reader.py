import nltk.data
import os.path
import cv2
import sys
import json
import imghdr
import imutils

try: sent_tokenizer = nltk.data.load('punkt.pickle')
except:
    print("File 'punkt.pickle' missing.")
    sys.exit()
    
while True:
    imgname = input("Enter Image Filename: ")
    if os.path.exists(imgname) == False or not imghdr.what(imgname):
        print("Please supply a valid image file for decryption.")
        continue
    break

img = cv2.imread(imgname)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, img) = cv2.threshold(img, 215, 255, cv2.THRESH_BINARY)
img = imutils.resize(img, height=350)

jumpsb = []
jumpst = []
linesb = []
linest = []
out = []
outplace = []
prev = 0

for i in range(int(img.shape[1])):
    if img[int(img.shape[0]-10), i] == 0:
        linesb.append(i)

for i in range(int(img.shape[1])):
    if img[60, i] == 0:
        linest.append(i)
for line in linesb:
    if line - prev > 10 or line == 10:
        jumpsb.append(line)
    prev = line

prev = 0
for line in linest:
    if line - prev > 10 or line == 10:
        jumpst.append(line)
    prev = line

for jumpb in jumpsb:
    for jumpt in jumpst:
        if jumpb - 50 <= jumpt <= jumpb + 50:
            out.append(1)
            out.append(jumpb)
            break
    else:
        out.append(0)
        out.append(jumpb)
    continue

with open("bars.json", 'r') as f: bars = json.load(f)
byte = []
output = ""
for i, bit in enumerate(out):
    if i % 2 != 0: continue
    byte.append(bit)
    if len(byte) % 5 != 0:
        continue
    for bar in bars:
        if byte == bar[1:]:
            output += bar[0]
            continue
    byte = []

img = cv2.copyMakeBorder(img, 100, 0, 0, 0, cv2.BORDER_CONSTANT)
for i, bit in enumerate(out):
    if i % 2 != 0: continue
    cv2.putText(img, str(bit), (out[i + 1]-15, 85), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 10)
sentences = sent_tokenizer.tokenize(output)
sentences = [sent.capitalize() for sent in sentences]

print(' '.join(sentences))

cv2.imshow("Bars", imutils.resize(img, height=75))
cv2.waitKey(0)