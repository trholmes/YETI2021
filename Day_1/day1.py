import hashlib

def brute_force():
    # uses all the ascii characters from 0 to z

    for a in range(48, 123):
        for b in range(48, 123):
            for c in range(48, 123):
                for d in range(48, 123):
                    s = chr(a) + chr(b) + chr(c) + chr(d)
                    md5_string = hashlib.md5(s.encode("utf-8")).hexdigest()

                    if md5_given == md5_string:
                        return s

md5_given = "4002f685108db38f1af9965f3bc869eb"

print("Correct string: ", end='')
print(brute_force())

