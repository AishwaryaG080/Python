import os, shutil

print("1.Search  2.Rename  3.CopyAll  4.CopyExt")
ch = input("Choice: ")

try:
    if ch == "1":
        d = input("Dir: "); e = input("Ext: ")
        for f in os.listdir(d):
            if f.endswith(e):
                print(f)

    elif ch == "2":
        d = input("Dir: "); e1 = input("Old ext: "); e2 = input("New ext: ")
        for f in os.listdir(d):
            if f.endswith(e1):
                os.rename(d+"/"+f, d+"/"+f.replace(e1, e2))

    elif ch == "3":
        s = input("Source: "); t = input("Target: ")
        os.makedirs(t, exist_ok=True)
        for f in os.listdir(s):
            if os.path.isfile(s+"/"+f):
                shutil.copy(s+"/"+f, t)

    elif ch == "4":
        s = input("Source: "); t = input("Target: "); e = input("Ext: ")
        os.makedirs(t, exist_ok=True)
        for f in os.listdir(s):
            if f.endswith(e):
                shutil.copy(s+"/"+f, t)

    else:
        print("Invalid choice")

except FileNotFoundError:
    print("Directory not found")

except PermissionError:
    print("Permission denied")

except Exception as e:
    print("Error:", e)