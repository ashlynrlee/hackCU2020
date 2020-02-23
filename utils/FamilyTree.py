import pandas as pd
from utils.DataFile import *

def searchTree(df, memberData) :
    toSearch = [memberData]
    searched = []
    while (len(toSearch) != 0) :
        member = toSearch.pop()
        memberName = member['First'][0] + ' ' + member['Last'][0]
        searched.append(member)
        results = df.query('Big == @memberName or Little == @memberName').to_dict(orient='list')
        for i in range(len(results['First'])) :
            familyName = results['First'][i] + ' ' + results['Last'][i]
            if not contains(familyName, searched) :
                toSearch.append({'First': results['First'][i], 'Last': results['Last'][i], 'Email': results['Email'][i], 'Grad_Date': results['Grad_Date'][i], 'Big': results['Big'][i], 'Little': results['Little'][i], 'In_Program': results['In_Program'][i], 'Seeking_Little': results['Seeking_Little'][i], 'Seeking_Big': results['Seeking_Big'][i], 'Mentor_Lead': results['Mentor_Lead'][i], 'Notes': results['Notes'][i]})
            
        return searched
    
def contains(find, search) :
    for s in search :
        name = s['First'][0] + ' ' + s['Last'][0]
        if name == find :
            return True
    return False
        
