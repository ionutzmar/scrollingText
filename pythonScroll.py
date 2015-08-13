import wiringpi2 as wiringpi
import sys

cols = [23, 22, 21, 29, 28, 27, 26, 1, 4, 5, 6]
rows = [24, 25, 3, 2, 0, 7]

nrOfLett = 0 #Number of letters
cursor = 0
startIndex = 0
speed = 0.1
initialSpeed = speed
elapsed = 0

a = [
	0, 1, 1, 0,
	1, 0, 0, 1,
	1, 1, 1, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1
]
b = [
	1, 1, 1, 0,
	1, 0, 0, 1,
	1, 1, 1, 0,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 1, 1, 0
]
c = [
	0, 1, 1, 1,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0,
	0, 1, 1, 1
]
d = [
	1, 1, 1, 0,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 1, 1, 0
]
e = [
	1, 1, 1, 1,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 1, 1, 1,
	1, 0, 0, 0,
	1, 1, 1, 1
]
f = [
	1, 1, 1, 1,
	1, 0, 0, 0,
        1, 1, 1, 1,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0
]
g = [
	0, 1, 1, 1,
	1, 0, 0, 0,
        1, 0, 0, 0,
	1, 0, 1, 1,
	1, 0, 0, 1,
	0, 1, 1, 1
]
h = [
	1, 0, 0, 1,
	1, 0, 0, 1,
        1, 0, 0, 1,
	1, 1, 1, 1,
	1, 0, 0, 1,
	1, 0, 0, 1
]

i = [
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0
]
j = [
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	1, 0, 1, 0,
	0, 1, 0, 0
]
k = [
	1, 0, 0, 1,
	1, 0, 1, 0,
	1, 1, 0, 0,
	1, 1, 0, 0,
	1, 0, 1, 0,
	1, 0, 0, 1
]

l = [
	1, 0, 0, 0,
	1, 0, 0, 0,
        1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 1, 1, 1
]
m = [
	1, 0, 0, 0,
	1, 1, 0, 1,
	1, 0, 1, 0,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0
]
n = [
	1, 0, 0, 1,
	1, 1, 0, 1,
	1, 0, 1, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1
]
o = [
	0, 1, 1, 0,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	0, 1, 1, 0

]


p = [
	1, 1, 1, 0,
	1, 0, 0, 1,
	1, 1, 1, 0,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0
]
#q = [
#	0, 1, 0, 0,
#	1, 0, 1, 0,
#	1, 0, 1, 0,
#	1, 0, 1, 0,
#	0, 1, 1, 0,
#	0, 0, 0, 1,
#]
q = [
	0, 1, 1, 0,
	1, 0, 0, 1,
	0, 0, 0, 1,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0
]
r = [
	1, 1, 1, 0,
	1, 0, 0, 1,
	1, 1, 1, 0,
	1, 1, 0, 0,
	1, 0, 1, 0,
	1, 0, 0, 1
]
s = [
	0, 1, 1, 0,
	1, 0, 0, 1,
	1, 0, 0, 0,
	0, 1, 1, 0,
	0, 0, 0, 1,
	1, 1, 1, 0
]
t = [
	1, 1, 1, 1,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0,
]
u = [
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	0, 1, 1, 0

]

v = [
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	1, 0, 0, 1,
	0, 1, 1, 0,
	0, 1, 1, 0
]
w = [
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 0, 0,
	1, 0, 1, 0,
	1, 1, 0, 1,
	1, 0, 0, 0
]
x = [
	1, 0, 0, 1,
	1, 0, 0, 1,
	0, 1, 1, 0,
	0, 1, 1, 0,
	1, 0, 0, 1,
	1, 0, 0, 1
]
y = [
	1, 0, 0, 1,
	1, 0, 0, 1,
	0, 1, 0, 1,
	0, 0, 1, 0,
	0, 0, 1, 0,
	0, 0, 1, 0
]
z = [
	1, 1, 1, 1,
	0, 0, 0, 1,
	0, 0, 1, 0,
	0, 1, 0, 0,
	1, 0, 0, 0,
	1, 1, 1, 1
]
_ = [
    0, 0, 0, 0,
    1, 0, 0, 1,
    0, 0, 0, 0,
    1, 0, 0, 1,
    0, 1, 1, 0,
    0, 0, 0, 0
]
wiringpi.wiringPiSetup()

for pin in cols:
    wiringpi.pinMode(pin, 1)
    wiringpi.digitalWrite(pin, 0)
for pin in rows:
    wiringpi.pinMode(pin, 1)
    wiringpi.digitalWrite(pin, 0)

for words in range(1, len(sys.argv)):
    for letters in sys.argv[words]:
        print letters
        nrOfLett += 1
    print " "

if nrOfLett == 0:
    sys.exit("Give me some words to show!!")

if len(sys.argv) > 2:
    length = nrOfLett * 5 + len(sys.argv) - 2
else:
    length = nrOfLett * 5
    
print length

text = [0] * length * len(rows)

for words in range(1, len(sys.argv)):
    for letters in sys.argv[words]:
        for im in range(0, 6):
            for jm in range(0, 4):
                text[im * length + jm + cursor] = eval(letters + '[' + str(jm + im * 4) + ']')
            if letters == 'm' or letters == 'w':
                text[im * length + 4 + cursor] = 1
            else:
                text[im * length + 4 + cursor] = 0
        cursor += 5
    cursor += 1
        
while True:
    for i in range(0, 6):
        for j in range(0, 11):
            if text[i * length + j + startIndex] == 1:
                wiringpi.digitalWrite(cols[j], 1)
                wiringpi.digitalWrite(rows[i], 1)
                wiringpi.delay(1)
                wiringpi.digitalWrite(cols[j], 0)
                wiringpi.digitalWrite(rows[i], 0)
            if wiringpi.millis() - elapsed > speed * 1000:
                elapsed += speed * 1000
                if startIndex == length - 11:
                    startIndex = 0
                    wiringpi.delay(250)
                else:
                    startIndex += 1
            if startIndex == 0 and  wiringpi.millis() - elapsed > speed * 1000:
                elapsed += speed * 10000
            if startIndex == length - 15 and  wiringpi.millis() - elapsed > speed * 1000:
                elapsed += speed * 10000
        
