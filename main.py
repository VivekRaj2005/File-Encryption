import os
import shutil
import random

def FileWriter(file, content):
    if os.path.exists(f"{file}.file"):
        os.remove(f"{file}.file")
    with open(f'{file}.txt', 'w') as fileRead:
        fileRead.write(f"{content}")
    shutil.copy(f'{file}.txt', f'{file}.file')
    os.remove(f"{file}.txt")

def Reset():
    files = ["Hash_Map.file", "content.file", "sample_space.file"]
    for file in files:
        if os.path.exists(file):
            os.remove(file)
    quit(0)

def FileReader(file) -> str:
    shutil.copy(f'{file}.file', f'{file}.txt')
    with open(f'{file}.txt', 'r') as fileRead:
        content = fileRead.readline()
    os.remove(f"{file}.txt")
    return content

def removeChar(char, string) -> str:
    rt_val =  ""
    for chars in string:
        if char != chars:
            rt_val += chars
    return rt_val


def GenerateHashTable():
    sample_space = FileReader("sample_space")
    sample = sample_space
    rt_val = ""
    for x in range(len(sample) - 1):
        char = random.choice(sample_space)
        rt_val += f"{char}||"
        sample_space = removeChar(char, sample_space)
    rt_val += sample_space[0]
    FileWriter("Hash_Map", rt_val)

def LoadSample() -> []:
    read = FileReader("Hash_Map")
    set_char = read.split("||")
    return set_char

def WriteEncryption(string):
    sample = LoadSample()
    rt_val = ""
    for x in range(len(string) - 1):
        char = string[x]
        index = sample.index(char)
        rt_val += f"{str(sample.index(char))}||"
    char = string[len(string) - 1]
    index = sample.index(char)
    rt_val += f"{str(sample.index(char))}"
    FileWriter("content", rt_val)

def DecodeEncryption(file="content"):
    sample = LoadSample()
    rt_val = ""
    read = FileReader(file)
    space = read.split("||")
    for char in space:
        rt_val += str(sample[int(char)])
    print(rt_val)
    input(">>>")

def Encoder():
    print("USE DEFAULT HASH MAP?[Y / N]")
    a = input(">>>")
    if a.lower() == "y":
        WriteEncryption(input("Enter content:"))
    else:
        a = input("Path")
        if os.path.exists(a) and ".file" in a:
            os.mkdir("Hash_Map")
            shutil.copy("Hash_Map.file", "Hash_Map\\Hash_Map.file")
            os.remove("Hash_Map.file")
            shutil.copy(a, "Hash_Map.file")
            WriteEncryption(input("Enter content:"))
            os.remove("Hash_Map.file")
            shutil.copy("Hash_Map\\Hash_Map.file", "Hash_Map.file")
            os.remove("Hash_Map\\Hash_Map.file")
            os.rmdir("Hash_Map")

def LoadClearer():
    try:
        os.system('cls')
        def clear(): os.system('cls')
        return clear
    except Exception as e:
        FileWriter("Error Log1", e)
    try:
        os.system("clear")
        def clear(): os.system('clear')
        return clear
    except Exception as e:
        FileWriter("Error Log2", e)


def Decoder():
    if os.path.exists("content.file"):
        content_path = input("CONTENT PATH [LEAVE BLANK FOR content.file]")
        if content_path == "":
            content_path = "content.file"
    else:
        content_path = input("CONTENT PATH:")
        if content_path == "":
            print("Incorrect Path")
            input("<<<")
            return
    print("USE DEFAULT HASH MAP?[Y / N]")
    inp = input(">>>")
    if inp.lower() == "y":
        DecodeEncryption()
    else:
        path = input("Path:")
        if os.path.exists(path) and ".file" in path:
            os.mkdir("Hash_Map")
            shutil.copy("Hash_Map.file", "Hash_Map\\Hash_Map.file")
            os.remove("Hash_Map.file")
            shutil.copy(path, "Hash_Map.file")
            DecodeEncryption()
            os.remove("Hash_Map.file")
            shutil.copy("Hash_Map\\Hash_Map.file", "Hash_Map.file")
            os.remove("Hash_Map\\Hash_Map.file")
            os.rmdir("Hash_Map")
            input("<<<")



if __name__ == '__main__':
    Clearer = LoadClearer()
    if os.path.exists("sample_space.file") is False:
        alpha = "abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM"
        numeric = "1234567890"
        special = "!@#$%^&*()_+{}:\',./[];\"|\\<>? "
        FileWriter("sample_space", alpha+numeric+special)
    while True:
        # Title
        print("Welcome to Encrypt.")
        # Menu
        print(" 1 > ENCRYPT CONTENT")
        print(" 2 > DECODE CONTENT")
        print(" 3 > GenerateHashTable")
        print(" 4 > Reset")
        print(" 5 > EXIT")
        option = int(input("<<<"))
        if option == 4:
            print("WARNING :YOU ARE ABOUT RESET ENCRYPT")
            input("<<<")
            Reset()
            Clearer()
        elif option == 3:
            print("WARNING :PLEASE SAVE THE EXISTING HASH TABLE FOR PAST ENCRYPTIONS")
            input("<<<")
            GenerateHashTable()
            Clearer()
        elif option == 5:
            print("THANK YOU FOR USING ENCRYPT")
            input(">>>")
            quit(0)
            Clearer()
        elif option == 2:
            Decoder()
            Clearer()

        elif option == 1:
            Encoder()
            Clearer()
        else:
            print("WRONG OPTION")
