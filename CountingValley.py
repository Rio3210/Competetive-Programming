
import os
def countingValleys(steps, path):
    cl = 0
    count = 0
    for i in range(steps):
        if path[i] == 'U':
            cl += 1
        elif path[i] == 'D':
            cl -= 1
            if cl == -1:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
