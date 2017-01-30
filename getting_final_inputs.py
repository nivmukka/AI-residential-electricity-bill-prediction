import csv 

with open('finalinputs.csv', 'wb') as csv1:     
    writer = csv.DictWriter(csv1, fieldnames=["TYPEHUQ","HDD30YR","CDD30YR","BEDROOMS","NCOMBATH","TOTROOMS","CELLAR","GARGHEAT","HEATROOM","ACROOMS","USECENAC","TEMPNITEAC","TOTSQFT","TOTHSQFT","TOTCSQFT","KWH","KWHCOL","KWHRFG","KWHOTH","DOLELCOL","DOLELWTH","DOLELRFG","DOLELOTH","DOLLAREL"])
    
    writer.writeheader()
         
    with open('output2.csv', 'r') as csv2:      
        reader = csv.DictReader(csv2)         
        for row in reader:      
            writer.writerow({'TYPEHUQ':row['TYPEHUQ'],'HDD30YR':row['HDD30YR'],'CDD30YR':row['CDD30YR'],'BEDROOMS':row['BEDROOMS'],'NCOMBATH':row['NCOMBATH'],'TOTROOMS':row['TOTROOMS'],'CELLAR':row['CELLAR'],'GARGHEAT':row['GARGHEAT'],'HEATROOM':row['HEATROOM'],'ACROOMS':row['ACROOMS'],'USECENAC':row['USECENAC'],'TEMPNITEAC':row['TEMPNITEAC'],'TOTSQFT':row['TOTSQFT'],'TOTHSQFT':row['TOTHSQFT'],'TOTCSQFT':row['TOTCSQFT'],'KWH':row['KWH'],'KWHCOL':row['KWHCOL'],'KWHRFG':row['KWHRFG'],'KWHOTH':row['KWHOTH'],'DOLELCOL':row['DOLELCOL'],'DOLELWTH':row['DOLELWTH'],'DOLELRFG':row['DOLELRFG'],'DOLELOTH':row['DOLELOTH'],'DOLLAREL':row['DOLLAREL']})