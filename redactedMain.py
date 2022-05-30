# CITY AND DATE INFORMATION WAS REDACTED TO OBSCURE AND ANONYMISE DATA.

import pandas as pd
import matplotlib.pyplot as plt
import numpy

def runCode():
    # Input data
    dataSet = pd.read_csv("input.csv")
    # Filter out people who have not finished the survey.
    onlyComplete = dataSet.loc[dataSet['completed'] == 1]
    # Save
    onlyComplete.to_csv("output.csv")

    # Collect all responses from CITY, and alternative spellings found.
    onlyInCITYwangen = onlyComplete.loc[
        (onlyComplete['Question 5'] == "CITY") |
        (onlyComplete['Question 5'] == "CITY") |
        (onlyComplete['Question 5'] == "CITY") |
        (onlyComplete['Question 5'] == "CITY") |
        (onlyComplete['Question 5'] == "CITY")
    ]
    # Save
    onlyInCITYwangen.to_csv("onlyInCITY.csv")

    # Excluding students that are in CITY (Students not in CITY)
    notInCITYwangen =  onlyComplete.loc[
        (onlyComplete['Question 5'] != "CITY") &
        (onlyComplete['Question 5'] != "CITY") &
        (onlyComplete['Question 5'] != "CITY") &
        (onlyComplete['Question 5'] != "CITY") &
        (onlyComplete['Question 5'] != "CITY")
    ]
    # Save
    notInCITYwangen.to_csv("notInCITY.csv")

    # Students after covid, DATE
    afterCovid = onlyComplete.loc[
    (onlyComplete['Question 10 '] == 'DATE') |
    (onlyComplete['Question 10 '] == 'DATE')
    ]
    # Save
    afterCovid.to_csv("afterCovid.csv")

    # Excluding students from after covid (during covid) DATE (Sorry if I caused any flashbacks :)
    duringCovid = onlyComplete.loc[
    (onlyComplete['Question 10 -'] != 'DATE') &
    (onlyComplete['Question 10 -'] != 'DATE')
    ]
    # Save
    duringCovid.to_csv("duringCovid.csv")


def readMultiChoice(wordsToFind, csvToRead):
    # Allows multi choice questions to be read.
    import pandas as pd
    import numpy

    # Input
    inputData = pd.read_csv(csvToRead)
    # search for columns starting with inputted keyword.
    search = inputData.filter(like=wordsToFind).copy()

    # Name and save output data with input keyword
    search.to_csv(f'{wordsToFind}.csv')

    # Go through each column and replace -1 with NaN, print out column and value.
    for column in search.columns:
        removeN1Joined = search[column].replace(to_replace="-1", value=numpy.NaN)
        print("\n" + column)
        print(removeN1Joined.count())

def readSingle(wordToFind, csvToRead):
    import pandas as pd
    # Allows single column questions to be read.

    # Input
    inputData = pd.read_csv(csvToRead)
    # Search for column
    search = inputData.filter(like=wordToFind).copy()
    # Save and name
    search.to_csv(f'{wordToFind}.csv')
    # print output
    print("\n" + search.columns)
    print(search.value_counts())


def readRank(wordToFind, csvToRead):
    import pandas as pd
    # Allows rankings to be read.

    # input
    inputData = pd.read_csv(csvToRead)
    # Search for columns.
    search = inputData.filter(like=wordToFind).copy()
    # Go through each column and sum the values
    for column in search.columns:
        print("\n" + column)
        print(search[column].value_counts())


def convertCSV():
    dataset = pd.read_excel("data.xlsx")
    dataset.to_csv("oldDataSet.csv")

if __name__ == '__main__':
    runCode()
    # convertCSV()
    readMultiChoice("Question 9", 'output.csv')

    readMultiChoice('Question 15 ', 'duringCovid.csv')

    readRank("Question 26 ", 'onlyInCity.csv')

    readRank("Question 26 ", 'output.csv')

    readSingle("Question 1 ", 'output.csv')

    readSingle("Question 5 ", 'output.csv')

    readSingle("Question 20 ", 'oldDataSet.csv')

    readSingle("Question 27 ", 'onlyInCITY.csv')

    readSingle("Question 20 ", 'duringCovid.csv')

    readSingle("Question 20 ", 'afterCovid.csv')

    readSingle('Question 5 ', 'duringCovid.csv')

    readSingle('Question 5 ', 'afterCovid.csv')

    readSingle('Question 5 ', 'output.csv')




