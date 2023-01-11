from core import DigitalToDigital


data = str(input("enter your digital data : "))
d = DigitalToDigital(data)

print("1 - Unipolar NRZ")
print("2 - Polar NRZL")
print("3 - Polar NRZI")
print("4 - Biphase Manchester")
print("5 - Biphase Diff Manchester")
print("6 - Bipolar AMI")
print("7 - Bipolar Pseudoternary")
print("8 - Exit")
inp = -1
while inp!=8:
    inp = int(input("Which method you want : "))
    if(inp == 1):
        d.unipolarNRZ()
    elif (inp == 2):
        d.polarNRZL()
    elif (inp == 3):
        d.polarNRZI()
    elif (inp == 4):
        d.biphaseManchester()
    elif (inp == 5):
        d.biphaseDifferentialManchester()
    elif (inp == 6):
        d.bipolarAMI()
    elif (inp == 7):
        d.bipolarPseudoTernary()