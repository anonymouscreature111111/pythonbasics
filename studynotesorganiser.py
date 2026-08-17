import os 
science_notes = [
    "Plants need sunglight and water",
    "The Earth moves around the sun",
    "Water can change into ice and steam"
]
maths_notes = [
    "Addition menas finding the total",
    "Subtraction means taking away",
    "Multiplication is repeated addition"
]
with open("science-notes.txt", "w") as f:
    f.writelines(science_notes)
with open("maths-notes.txt", "w") as f:
    f.writelines(maths_notes)


print("Science Notes")
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("maths-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words:", line.strip())

merged_file = "all-study-notes.txt"
if os.path.exists(merged_file):
    print(merged_file, "already exists")
else:
    print(merged_file, "does not exist")

if os.path.exists(merged_file):
    os.remove(merged_file)
    print("Old merged file removed")
else:
    print("No merged file to remove")

with open(merged_file, "w") as output:
    with open("science-notes.txt", "r") as science:
        output.write(science.read())
    with open("maths-notes.txt", "r") as math:
        output.write(math.read())

print("Maths and science notes merged successfully")
print("Merged notes")
with open(merged_file, "r") as f:
    for line in f:
        print(line.strip)



