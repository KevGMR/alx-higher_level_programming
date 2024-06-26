#!/usr/bin/python3

HEIGHT = 2
WIDTH = 4

# result = (for _ in range(width))

RESULT = ("\n".join(["".join(["#" for _ in range(WIDTH)])
                     for _ in range(HEIGHT)]))
print(RESULT)
