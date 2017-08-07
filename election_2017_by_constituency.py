import matplotlib.pyplot as plt

file = open("election_data", 'r')

data = file.read()

split_data = data.split("\n")

const = input("Which Constituency Result Would You Like To See? (Does NOT Include Northern Ireland): ")

const_data = ""

for line in split_data:
    if const in line:
        const_data = line
        break

final_data = []
data_storer = ""

if ',' in const:
    commas = 1
else:
    commas = 0
char_count = 0

for char in const_data:
    char_count += 1
    if char == ',':
        commas += 1
        char_count = 1
    if commas == 22 or commas == 24 or commas == 26 or commas == 28 or commas == 30 or commas == 32\
            or commas == 34 or commas == 36:
        data_storer += char
    elif commas == 23 and char_count == 1 or commas == 25 and char_count == 1 or commas == 27 and char_count == 1\
            or commas == 29 and char_count == 1 or commas == 31 and char_count == 1 or commas == 33 \
            and char_count == 1 or commas == 35 and char_count == 1 or commas == 37:
        final_data.append(data_storer.replace(",", ""))
        data_storer = ""

for x in range(len(final_data) - 8):
    final_data.remove("")

try:
    final_data[0] = int(final_data[0])
    final_data[1] = int(final_data[1])
    final_data[2] = int(final_data[2])
    final_data[3] = int(final_data[3])
    final_data[4] = int(final_data[4])
    final_data[5] = int(final_data[5])
    final_data[6] = int(final_data[6])
    final_data[7] = int(final_data[7])
except IndexError:
    print("Constituency Not Found!")
    exit(1)

parties = []
final_final_data = [0,0,0,0,0,0,0,0]
colours = ()

if final_data[0] != 0:
    parties.append("Conservatives")
    final_final_data[0] = final_data[0]
if final_data[2] != 0:
    parties.append("Labour")
    final_final_data[1] = final_data[2]
if final_data[3] != 0:
    parties.append("Liberal Democrats")
    final_final_data[2] = final_data[3]
if final_data[6] != 0:
    parties.append("SNP")
    final_final_data[3] = final_data[6]
if final_data[5] != 0:
    parties.append("Plaid Cymru")
    final_final_data[4] = final_data[5]
if final_data[7] != 0:
    parties.append("UKIP")
    final_final_data[5] = final_data[7]
if final_data[1] != 0:
    parties.append("Green")
    final_final_data[6] = final_data[1]
if final_data[4] != 0:
    parties.append("Other")
    final_final_data[7] = final_data[4]

if final_final_data[0] != 0:
    colours += ('b',)
if final_final_data[1] != 0:
    colours += ('r',)
if final_final_data[2] != 0:
    colours += ('#FFC200',)
if final_final_data[3] != 0:
    colours += ('y',)
if final_final_data[4] != 0:
    colours += ('#3F8428',)
if final_final_data[5] != 0:
    colours += ('#70147A',)
if final_final_data[6] != 0:
    colours += ('g',)
if final_final_data[7] != 0:
    colours += ('#696969',)

for x in range(final_final_data.count(0)):
    final_final_data.remove(0)

fig1, ax1 = plt.subplots()

ax1.pie(final_final_data, labels=parties, autopct='%1.1f%%', startangle=270, colors=colours)

ax1.axis('equal')

plt.title(const)

plt.show()