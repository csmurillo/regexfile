import re

outputContent=[]
pattern='\(([^)]*)\)[^(]*$'

# open file
with open('input.txt') as f:
    # remove brackets from the file
    line = f.readline()
    mod_str=re.sub(pattern,'',line)
    outputContent.append(mod_str+'\n')
    while line:
        line = f.readline()
        mod_str=re.sub(pattern,'',line)
        outputContent.append(mod_str+'\n')

# write to file
with open('output.txt','w') as f:
    for outputLine in outputContent:
        f.write(outputLine)

