import pandas as pd

data_filepath = '../data.csv'

def loadIn() :
    global data_filepath
    global df
    df = pd.read_csv(data_filepath)
    return df

def loadOut(df) :
    global data_filepath
    #df.write_csv(data_filepath)
    
def addNewMember(df, first, last, email, gradDate, big, little, inProgram, seekingLittle, seekingBig, mentorLead, notes) :
    df = df.append({'First': first, 'Last': last, 'Email': email}, ignore_index=True)
    return df
    
def searchFirstName(df, first) :
    return df.query('First == @first')
    

if __name__=='__main__' :
    df = loadIn()
    df = addNewMember(df, 'Westin','Musser','wstnmssr@gmail.com','S20','','',True,False,False,'','')
    print(searchFirstName(df, 'Sarah'))
    