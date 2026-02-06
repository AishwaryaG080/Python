import os
import hashlib
import time

start = time.time()

try:
    dir_name = input("Enter directory name: ")
    files = os.listdir(dir_name)

    checksum_list = []
    log = open("Log.txt", "w")

    for file in files:
        path = os.path.join(dir_name, file)

        if os.path.isfile(path):
            f = open(path, "rb")
            data = f.read()
            f.close()

            checksum = hashlib.md5(data).hexdigest()

            if checksum in checksum_list:
                log.write("Duplicate deleted: " + file + "\n")
                os.remove(path)
            else:
                checksum_list.append(checksum)

    log.close()
    print("Duplicate files removed. Check Log.txt")

except FileNotFoundError:
    print("Directory not found")

except PermissionError:
    print("Permission denied")

except Exception as e:
    print("Error:", e)

end = time.time()
print("Execution time:", end - start)