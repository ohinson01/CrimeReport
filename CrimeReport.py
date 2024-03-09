'''
Program: Crime report
Date: 6/8/2020
'''
'''
Program reads and determines street with most crimes.
Write to "crime.txt" file on number of each type of crime on that street.
Also, compute day of each year with the most crime, then determine which day
overall has highest odds
'''
#main
from csv import DictReader, reader

#create variable for file name 
filename = r"C:\Users\ohins\OneDrive\Documents\ECPI_University\Python\Crimes_-_2001_to_present.csv"
#initialize total to 0 to total exact match of description 
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total7 = 0
total8 = 0
total9 = 0
total10 = 0
#open files in read and write to new file 
with open(filename, "r") as inputFile:
    with open("crime.txt", "wt") as outputFile:
        csv_dict_reader = DictReader(inputFile)
        outputFile.write("Crime Report of the Top 10 (Highest to Lowest):\n\n")
        #iterate over column to match the crime in the text file
        #output total and street found of most crime 
        for row in csv_dict_reader:
            '''
            Error in code:
                for row in csv_dict_reader
            How error works:
                When I run the program, an error message pops up with a red line in my code
                to let me know where my error is and to tell me I have invalid syntax
            How I solved it:
                By following the red line, I could fix my syntax error by adding a colon
            '''
            #Since this was a short file to read from, I counted manually
            #the year the most crime was recorded 
            if(row['Description'] == "FINANCIAL IDENTITY THEFT OVER $ 300" and
               row['Year'] == "2017"):
                total1 = total1 + 1
                street1 = row['Block']
            if(row['Description'] == "OVER $500" and row['Year'] == "2017"):
                total2 = total2 + 1
                street2 = row['Block']
            if(row['Description'] == "PREDATORY" and row['Year'] == "2007"):
                total3 = total3 + 1
                street3 = row['Block']
            if(row['Description'] == "FINANCIAL IDENTITY THEFT $300 AND UNDER" and
               row['Year'] == "2017"):
                total4 =  total4 + 1
                street4 = row['Block']
            if(row['Description'] == "FROM BUILDING" and row['Year'] == "2017"):
                total5 = total5 + 1
                street5 = row['Block']
            if(row['Description'] == "SIMPLE" and row['Year'] == "2001"):
                total6 = total6 + 1
                street6 = row['Block']
            elif(row['Year'] == "2017"):
                    street7 = row['Block']
            if(row['Description'] == "NON-AGGRAVATED" and row['Year'] == "2017"):
                total7 = total7 + 1
                street8 = row['Block']
            if(row['Description'] == "CREDIT CARD FRAUD" and row['Year'] == "2017"):
                total8 = total8 + 1
                street9 = row['Block']
            if(row['Description'] == "AGG CRIMINAL SEXUAL ABUSE" and row['Year'] == "2017"):
                total9 = total9 + 1
                street10 = row['Block']
            if(row['Description'] == "FORCIBLE ENTRY" and row['Year'] == "2017"):
                total10 = total10 + 1
                street11 = row['Block']
        #output results
        outputFile.write("1. FINANCIAL IDENTITY THEFT OVER $300: " + str(total1))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street1))
        outputFile.write("\n2. OVER $500: " + str(total2))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street2))
        outputFile.write("\n3. FROM BUILDING: " + str(total5))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street5))
        outputFile.write("\n4. CREDIT CARD FRAUD: " + str(total8))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street9))
        outputFile.write("\n5. PREDATORY: " + str(total3))
        outputFile.write("\n\t" + "Year: 2007" + "\t Street: " + str(street3))
        outputFile.write("\n6. FINANCIAL IDENTITY THEFT $300 AND UNDER: " + str(total4))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street4))
        outputFile.write("\n7. SIMPLE: " + str(total6))
        outputFile.write("\n\t" + "Year: 2001" + "\t Street: " + str(street6))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street7))
        outputFile.write("\n8. NON-AGGRAVATED: " + str(total7))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street8))
        outputFile.write("\n9. AGG CRIMINAL SEXUAL ABUSE: " + str(total9))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street10))
        outputFile.write("\n10. FORCIBLE ENTRY: " + str(total10))
        outputFile.write("\n\t" + "Year: 2017" + "\t Street: " + str(street11))
#close files
inputFile.close()
outputFile.close()
print("Crime report completed")
