# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

count = 0
spam_total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    num = line.find(":")
    spam = float(line[num+1:])
    spam_total = spam_total + spam
confidence = spam_total / count

print("Average spam confidence: {0: >1.12f}".format(float(confidence)))
