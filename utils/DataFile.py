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
    df = df.append({'First': first, 'Last': last, 'Email': email}, ignore_index=True)
    return df
    
def searchFirstName(df, first) :
    return df.query('First == @first')

def searchLastName(df, last) :
    return df.query('Last == @last')

def searchEmail(df, email) :
    return df.query('Email == @email')

def searchGradDate(df, gradDate) :
    return df.query('Grad_Date == @gradDate')

def searchBig(df, big) :
    return df.query('Big == @big')

def searchLittle(df, little) :
    return df.query('Little == @little')

def searchInProgram(df) :
    return df.query('In_Program == True')

def searchNotInProgram(df) :
    return df.query('In_Program == False')

def searchSeekingLittle (df) :
    return df.query('Seeking_Little == True')

def searchNotSeekingLittle (df) :
    return df.query('Seeking_Little == False')

def searchNotSeekingBig (df) :
    return df.query('Seeking_Big == False')

def searchMentorLead (df, mentorLead) :
    return df.query('Seeking_Little == @mentorLead')

if __name__=='__main__' :
    df = loadIn()
    df = addNewMember(df, 'Westin','Musser','wstnmssr@gmail.com','S20','','',True,False,False,'','')
    print(searchFirstName(df, 'Sarah'))
    loadOut(df)
    