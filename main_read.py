
def readfile(filename):
    # readfile
    with open("./story.txt", "r") as openfile:
        read_file = openfile.read()
        # print(read_file)
        # print("This file is exist")
    return read_file


def countword():
    text = readfile("./story.txt")
    split_text = text.split()
    #print(split_text)
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print(countword())
