import re

pattern='\(([^)]*)\)[^(]*$'

def removeLineWithCharacters(fileName,outputFileName,characters):
    outputContent=[]
    # open file
    with open(fileName) as f:
        line = f.readline()
        if characters not in line:
                outputContent.append(line)
        while line:
            line = f.readline()
            if characters not in line:
                outputContent.append(line)
                

    # write to file
    with open(outputFileName,'w') as f:
        for outputLine in outputContent:
            f.write(outputLine)

def removePattern(fileName,outputFileName, pattern):
    # remove brackets from the file
    outputContent=[]
    # open file
    with open(fileName) as f:
        line = f.readline()
        mod_str=re.sub(pattern,'',line)
        outputContent.append(mod_str+'\n')
        while line:
            line = f.readline()
            mod_str=re.sub(pattern,'',line)
            outputContent.append(mod_str+'\n')

    # write to file
    with open(outputFileName,'w') as f:
        for outputLine in outputContent:
            f.write(outputLine)

def removeWhiteSpace(fileName,outputFileName):
    outputContent=[]
    # open file
    with open(fileName) as f:
        line = f.readline()
        outputContent.append(line)
        while line:
            line = f.readline()

            if "\n" in line and len(line)==2:
                print('yes')
            else:
                outputContent.append(line)

    print(outputContent)

    # write to file
    with open(outputFileName,'w') as f:
        for outputLine in outputContent:
            f.write(outputLine)

def replacePartOfLineContent(fileName,fileToWrite,lineContent,replace,replaceContent):
    outputContent=[]
    # open file
    with open(fileName) as f:
        line = f.readline()
        outputContent.append(line)
        while line:
            line = f.readline()
            if lineContent in line:
                outputContent.append(line.replace(replace,replaceContent))
            else:
                outputContent.append(line)
    # print(outputContent)

    # write to file
    with open(fileToWrite,'w') as f:
        for outputLine in outputContent:
            f.write(outputLine)

# removePattern('input.txt','output.txt',pattern)
# removeWhiteSpace('input.txt','output.txt')
# removeLineWithCharacters('input.txt','output.txt','Series B')
# removeLineWithCharacters('done.txt','done.txt','"low":')
# replacePartOfLineContent('done.txt','done2.txt','"close"','",','"')