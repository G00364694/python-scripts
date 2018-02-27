# Francis Adepoju. 28 Feb 2018
# The Iris_flower_data_set program
# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
#
# A Python script that reads in the Iris data set stored in the data subdirectory under
# the current project and then prints the four numerical values on 
# each row in a nice format on the screen. The printed data are for:
# petal length, petal width, sepal length and sepal width. 
# These values should have the decimal places aligned, with a space between the columns.
# 

with open("data/iris.csv") as inputFile:        # Open the input iris data file
    for myData in inputFile:                    # Loop through the file and split the data
        col1 = float(myData.split(',')[0])      # Data are forced to be seen as type float
        col2 = float(myData.split(',')[1])
        col3 = float(myData.split(',')[2])
        col4 = float(myData.split(',')[3])
        col5 = myData.split(',')[4]             # Not used in this program...

        # Data are formatted and printed on the screen as required.
        print('{0:.1f} {1:.1f} {2:.1f} {3:.1f}'.format(col1, col2, col3, col4))
        #print(col5, end='') 
print("End of file processing")                 # End of processing.


