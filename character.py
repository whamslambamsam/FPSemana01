## Variables/Lists
names = []
attackValue = []
defenseValue = []

## Character 1
name1 = input()
names.append(name1)

attackValue1 = input()
attackValue1 = int(attackValue1)
attackValue.append(attackValue1)

defenseValue1 = input()
defenseValue1 = int(defenseValue1)
defenseValue.append(defenseValue1)

## Character 2
name2 = input()
names.append(name2)

attackValue2 = input()
attackValue2 = int(attackValue2)
attackValue.append(attackValue2)

defenseValue2 = input()
defenseValue2 = int(defenseValue2)
defenseValue.append(defenseValue2)

## Character 3
name3 = input()
names.append(name3)

attackValue3 = input()
attackValue3 = int(attackValue3)
attackValue.append(attackValue3)

defenseValue3 = input()
defenseValue3 = int(defenseValue3)
defenseValue.append(defenseValue3)

## Group stat variables into tuples
stats1 = (attackValue1, defenseValue1)
stats2 = (attackValue2, defenseValue2)
stats3 = (attackValue3, defenseValue3)

## 2D array
characters = [
    [names[0], stats1],
    [names[1], stats2],
    [names[2], stats3]
]

## Print the characters - supposed output: "['name', (atk, def)]"
print(characters)

## Prepare and define variables/arrays for highest stats
highestAtk = []
highestDef = []
AtkID = []
DefID = []

highestAtk.append(max(attackValue))
highestDef.append(max(defenseValue))

for i in range(3):
    if int(attackValue[i]) >= (highestAtk[0]):
        AtkID.append(i)

for i in range(3):
    if int(defenseValue[i]) >= (highestDef[0]):
        DefID.append(i)

AtkID = int(AtkID[0])
DefID = int(DefID[0])

print("Ataque", names[AtkID], highestAtk[0])
print("Defesa", names[DefID], highestDef[0])