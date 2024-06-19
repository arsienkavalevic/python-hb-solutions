petia = int(input())
vasia = int(input())
tolia = int(input())
if tolia > petia > vasia:
    print("1. Толя")
    print("2. Петя")
    print("3. Вася")
elif tolia > vasia > petia:
    print("1. Толя")
    print("2. Вася")
    print("3. Петя")
elif petia > vasia > tolia:
    print("1. Петя")
    print("2. Вася")
    print("3. Толя")
elif petia > tolia > vasia:
    print("1. Петя")
    print("2. Толя")
    print("3. Вася")
elif vasia > petia > tolia:
    print("1. Вася")
    print("2. Петя")
    print("3. Толя")
elif vasia > tolia > petia:
    print("1. Вася")
    print("2. Толя")
    print("3. Петя")