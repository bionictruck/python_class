text = "X-DSPAM-Confidence:    0.8475";

pos1 = text.find('0')
pos2 = text[pos1:pos1+6]
nm = float(pos2)

print nm