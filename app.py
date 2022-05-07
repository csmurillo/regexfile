import re


pattern='\(([^)]*)\)[^(]*$'


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


# removePattern('input.txt','output.txt',pattern)
removeWhiteSpace('input.txt','output.txt')