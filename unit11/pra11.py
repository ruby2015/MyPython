import os

def strip(str):
    return str.strip()

def writeNewFile(lines):
    while True:
        newfile = raw_input("Please enter the new filename: ")
        if os.path.exists(newfile):
            print 'The file exists,try again'
        else:
            break
    with open(newfile,'w') as file:
        for line in lines:
            file.write(line+'\n')

def cleanFile(filename):
    with open(filename) as file:
        return map(strip,file.readlines())
        #return [strip(line) for line in file]

def writeOldFile(lines):
    while True:
        oldfile = raw_input("Please enter the old filename: ")
        if os.path.exists(oldfile):
            break
        else:
            print "the file does not exist,try again"
    with open(oldfile,'w') as file:
        for line in lines:
            file.write(line+'\n')

if __name__=="__main__":
    while True:
        filename = raw_input("Please enter the filename(q to quit): ")
        if filename=='q':
            break
        if os.path.exists(filename):
            lines = cleanFile(filename)
            choice = raw_input("n to new file, or c to cover file: ")
            if choice.lower()=='n':
                writeNewFile(lines)
            else:
                writeOldFile(lines)
        else:
            print 'filename does not exist'