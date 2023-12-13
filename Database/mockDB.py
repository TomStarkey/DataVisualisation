import pandas as pd
    
columns = ["Checkins",
           "Dates",
           "Names"]
dta = [[12,13,14,15],
        ["12/01/97","15/12/96","21/05/88","05/03/98"],
        ["Bob", "Bill", "Jim", "Timmy"]]




db = pd.DataFrame(dta, columns=columns, index=range(len(dta))) # ValueError: 3 columns passed, passed data had 4 columns
print(db)