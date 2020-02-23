import pandas as pd

data_filepath = '../data.csv'

def loadIn() :
    global data_filepath
    global df
    df = pd.read_csv(data_filepath)
    return df

def loadOut(df) :
    global data_filepath
    df.to_csv(data_filepath, index=False)
    
def addNewMember(df, first, last, email, gradDate, big, little, inProgram, seekingLittle, seekingBig, mentorLead, notes) :
    df = df.append({'First': first, 'Last': last, 'Email': email, 'Grad_Date': gradDate, 'Big': big, 'Little': little, 'In_Program': inProgram, 'Seeking_Little': seekingLittle, 'Seeking_Big': seekingBig, 'Mentor_Lead': mentorLead, 'Notes': notes}, ignore_index=True)
    return df
    
def searchFirstName(df, first) :
    return df.query('First == @first').to_dict(orient='list')

def searchLastName(df, last) :
    return df.query('Last == @last').to_dict(orient='list')

def searchEmail(df, email) :
    return df.query('Email == @email').to_dict(orient='list')

def searchGradDate(df, gradDate) :
    return df.query('Grad_Date == @gradDate').to_dict(orient='list')

def searchBig(df, big) :
    return df.query('Big == @big').to_dict(orient='list')

def searchLittle(df, little) :
    return df.query('Little == @little').to_dict(orient='list')

def searchInProgram(df) :
    return df.query('In_Program == True').to_dict(orient='list')

def searchNotInProgram(df) :
    return df.query('In_Program == False').to_dict(orient='list')

def searchSeekingLittle (df) :
    return df.query('Seeking_Little == True').to_dict(orient='list')

def searchNotSeekingLittle (df) :
    return df.query('Seeking_Little == False').to_dict(orient='list')

def searchNotSeekingBig (df) :
    return df.query('Seeking_Big == False').to_dict(orient='list')

def searchMentorLead (df, mentorLead) :
    return df.query('Seeking_Little == @mentorLead').to_dict(orient='list')

def searchGraduated (df, currentSemester) :
    data_dict = df.to_dict(orient='list')
    grads = []
    for i in range(len(data_dict['First'])) :
        if (_gradByThisYear(currentSemester, data_dict['Grad_Date'][i]) == 1) :
            grads.append({'First': data_dict['First'][i], 'Last': data_dict['Last'][i], 'Email': data_dict['Email'][i], 'Grad_Date': data_dict['Grad_Date'][i], 'Big': data_dict['Big'][i], 'Little': data_dict['Little'][i], 'In_Program': data_dict['In_Program'][i], 'Seeking_Little': data_dict['Seeking_Little'][i], 'Seeking_Big': data_dict['Seeking_Big'][i], 'Mentor_Lead': data_dict['Mentor_Lead'][i], 'Notes': data_dict['Notes'][i]})
        elif (_gradByThisYear(currentSemester, data_dict['Grad_Date'][i]) == 0 and data_dict['Grad_Date'][i][0:1] == 'F') :
            grads.append({'First': data_dict['First'][i], 'Last': data_dict['Last'][i], 'Email': data_dict['Email'][i], 'Grad_Date': data_dict['Grad_Date'][i], 'Big': data_dict['Big'][i], 'Little': data_dict['Little'][i], 'In_Program': data_dict['In_Program'][i], 'Seeking_Little': data_dict['Seeking_Little'][i], 'Seeking_Big': data_dict['Seeking_Big'][i], 'Mentor_Lead': data_dict['Mentor_Lead'][i], 'Notes': data_dict['Notes'][i]})
    return grads
            
def searchCurrent (df, currentSemester) :
    data_dict = df.to_dict(orient='list')
    grads = []
    for i in range(len(data_dict['First'])) :
        if (_gradByThisYear(currentSemester, data_dict['Grad_Date'][i]) == -1) :
            grads.append({'First': data_dict['First'][i], 'Last': data_dict['Last'][i], 'Email': data_dict['Email'][i], 'Grad_Date': data_dict['Grad_Date'][i], 'Big': data_dict['Big'][i], 'Little': data_dict['Little'][i], 'In_Program': data_dict['In_Program'][i], 'Seeking_Little': data_dict['Seeking_Little'][i], 'Seeking_Big': data_dict['Seeking_Big'][i], 'Mentor_Lead': data_dict['Mentor_Lead'][i], 'Notes': data_dict['Notes'][i]})
        elif (_gradByThisYear(currentSemester, data_dict['Grad_Date'][i]) == 0 and data_dict['Grad_Date'][i][0:1] == 'S') :
            grads.append({'First': data_dict['First'][i], 'Last': data_dict['Last'][i], 'Email': data_dict['Email'][i], 'Grad_Date': data_dict['Grad_Date'][i], 'Big': data_dict['Big'][i], 'Little': data_dict['Little'][i], 'In_Program': data_dict['In_Program'][i], 'Seeking_Little': data_dict['Seeking_Little'][i], 'Seeking_Big': data_dict['Seeking_Big'][i], 'Mentor_Lead': data_dict['Mentor_Lead'][i], 'Notes': data_dict['Notes'][i]})
    return grads
    
def _gradByThisYear (current, grad) :
    currentYear = int(current[1:])
    gradYear = int(grad[1:])
    if (currentYear > gradYear) :
        return 1
    elif (currentYear == gradYear) :
        return 0
    return -1    
    
    
    
if __name__=='__main__' :
    df = loadIn()
    df = addNewMember(df, 'Aislin', 'Jeske', 'aislin.jeske@gmail.com', 'F19', '','Ariana Mims',False,False,False,'','')
    print (searchCurrent(df, 'S20'))
