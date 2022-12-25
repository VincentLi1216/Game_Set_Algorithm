import main

def run_algorithm():
    myCardsSet = set(card_set_list)
    ansArr = []

    num = 0

    isOKToAdd = True
    lenOfAnsArr = 0
    tempLen = 0

    mainArr = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [2, 3, 1], [3, 2, 1]]
    numArr = []
    colorArr = []
    shapeArr = []
    shadingArr = []
    cardArr = []
    setArr = []
    temp = 0
    tempArr = []

    for i in range(0, 9):
        for j in range(0, 9):
            for k in range(0, 9):
                for l in range(0, 9):

                    for num in range(0, 3):
                        numArr.append(mainArr[i][num])

                    for color in range(0, 3):
                        colorArr.append(mainArr[j][color])

                    for shape in range(0, 3):
                        shapeArr.append(mainArr[k][shape])

                    for shading in range(0, 3):
                        shadingArr.append(mainArr[l][shading])

    for i in range(0, 19683):
        temp = numArr[i] * 1000 + colorArr[i] * 100 + shapeArr[i] * 10 + shadingArr[i]
        cardArr.append(temp)

    for i in range(0, 19683, 3):

        for j in range(0, 3):
            tempArr.append(cardArr[i + j])

        setArr.append(tempArr)
        tempArr = []

    # print(setArr)


    for i in range(0, 6561):
        tempSet = set(setArr[i])
        tempArr = list(tempSet.intersection(set(card_set_list)))

        if len(tempArr) == 3:

            for i in range(0, lenOfAnsArr):

                if len(set(tempArr).intersection(set(ansArr[i]))) == 3:
                    isOKToAdd = False

            if isOKToAdd:
                ansArr.append(sorted(tempArr))
                lenOfAnsArr += 1
                print(sorted(tempArr))

            isOKToAdd = True














