import csv


temp = open("./mnist_train.csv", 'r')
trainfile = csv.reader(temp)
temp = open("./mnist_test.csv", 'r')
testfile = csv.reader(temp)



def turntomatrix(numbers): #turns pic file into matrix of pixels (28*28)
    matrix = []
    rownum = 0
    row = []
    for i in range (28):
        row = []
        for i in range(28):
            row.append(int(numbers[i+rownum*28]))
        rownum +=1
        matrix.append(row)
    return matrix







def findverticalstart(picture):  #returns the y position of the highest written pixel (where the number starts)
    rownum=0
    for row in picture:
        rownum +=1
        for pixel in row:
            if pixel>100:
                return rownum

def findverticalend(Picture):   #returns the y position of the lowest written pixel (where the number ends)
    picture = reversed(Picture)
    rownum=0
    for row in picture:
        rownum +=1
        for pixel in row:
            if pixel>100:
                return 28-rownum

numberavgdensities = [[0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,], [0, 0, 0, 0,]]
for i in range(0): #data gaining function, turned off currently. 
    Pic = trainfile.__next__() #format of each picture file is: what number the picture represents, followed by 28*28 numbers that each represent a pixel, being a number between 0-255 (0 is white, 255 is black.)
    answer = Pic.pop(0)

    pic = turntomatrix(Pic)

    start = findverticalstart(pic)
    end = findverticalend(pic)
    size = end-start
    print(i)
    topdensity = 0
    middensity = 0
    bottomdensity = 0
    for row in pic[start:start+size//3]:
        for pixel in row:
            if pixel>100:
                topdensity+=1
    for row in pic[start+size//3+1:start+size//3*2+size%3]:
        for pixel in row:
            if pixel>100:
                middensity+=1
    for row in pic[start+size//3*2+size%3+1:end]:
        for pixel in row:
            if pixel>100:
                bottomdensity+=1
    
    numberavgdensities[int(answer)][0]+=topdensity
    numberavgdensities[int(answer)][1]+=middensity
    numberavgdensities[int(answer)][2]+=bottomdensity
    numberavgdensities[int(answer)][3]+=1


for i in (numberavgdensities): #calculates average score of all results for each section of pic
    i[0] = i[0]/i[3]
    i[1] = i[1]/i[3]
    i[2] = i[2]/i[3]


print(numberavgdensities)




data = [[47.55741127348643, 34.085594989561585, 43.17118997912317], [19.865008880994672, 17.074600355239788, 16.966252220248666], [33.846311475409834, 24.32172131147541, 45.260245901639344], [37.99797160243408, 28.32657200811359, 35.00608519269777], [28.8, 42.54205607476636, 15.465420560747663], [35.10138248847926, 25.716589861751153, 29.702764976958527], [20.810379241516966, 31.339321357285428, 42.6686626746507], [46.89272727272727, 19.978181818181817, 15.785454545454545], [41.86147186147186, 31.627705627705627, 31.346320346320347], [41.531313131313134, 29.618181818181817, 15.153535353535354]]

def guessnumber(pic):


    start = findverticalstart(pic)
    end = findverticalend(pic)
    size = end-start
    topdensity = 0
    middensity = 0
    bottomdensity = 0
    for row in pic[start:start+size//3]:
        for pixel in row:
            if pixel>100:
                topdensity+=1
    for row in pic[start+size//3+1:start+size//3*2+size%3]:
        for pixel in row:
            if pixel>100:
                middensity+=1
    for row in pic[start+size//3*2+size%3+1:end]:
        for pixel in row:
            if pixel>100:
                bottomdensity+=1

    densities = [topdensity, middensity, bottomdensity]
    currentguess = -1
    currentguessscore = 999
    for i in range (10):
        totalscore = 0
        for x in range (3):
            score = abs(data[i][x]-densities[x])
            totalscore += score
        if totalscore < currentguessscore:
            currentguess=i
            currentguessscore = totalscore
    print(currentguess)

    return currentguess



correct=0
incorrect=0
for i in range (1000):#turned off currently
    Pic = testfile.__next__()
    answer = int(Pic.pop(0))
    pic = turntomatrix(Pic)
    if (guessnumber(pic) == answer):
        correct+=1
    else:
        incorrect+=1
    
print(correct, incorrect)
