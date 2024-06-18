petia = int(input())
vasia = int(input())
tolia = int(input())
if tolia < petia > vasia:
    print("Петя")
elif petia < vasia > tolia:
    print("Вася")
elif petia < tolia > vasia:
    print("Толя")