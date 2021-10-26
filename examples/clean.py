import os

files = [(i) for i in os.listdir("examples") if "blockMeshDict"  in i]
for file in files:
    separatedByUnderscore = file.split('_')
    fileNameCorrected = ''
    for name in separatedByUnderscore:
        if(name != 'system' and name != '' and name != 'blockMeshDict'):
            fileNameCorrected += name+'_'
    fileNameCorrected = fileNameCorrected[0:len(fileNameCorrected)-1]
    os.rename("examples\\"+file,"examples\\"+fileNameCorrected)    
    print(fileNameCorrected)