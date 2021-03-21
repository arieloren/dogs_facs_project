import pandas as pd

data=pd.read_csv("D:/Amir/Machine_Learning_Course_Primrose/Final_Project/solomon_coder_trial/Mowgli3_F_2.csv")

motions={'inner brow raiser':1,
         'lips part':2,
         'Ears flattener':3}

motions_categories=['upper face AU',
                    'Lips part',
                    'Ears flattener']

def annotation_file_preprocessing(data,motions,motions_categories):
    #drop the first 3 lines from dataframe
    new_dataframe=data.iloc[3:,:]

    #initialize the columns
    new_dataframe=new_dataframe.reset_index()
    new_dataframe=new_dataframe.drop(["index"],axis=1)
    new_dataframe=new_dataframe.rename(columns=new_dataframe.iloc[0])

    #set time samples as indices
    new_dataframe=new_dataframe.iloc[1:,:]
    new_dataframe["Time"]=new_dataframe["Time"].str.replace(',','.', regex=True)
    new_dataframe["Time"]=new_dataframe["Time"].astype('float')
    new_dataframe=new_dataframe.set_index(["Time"])

    #keep only the demanded motions category
    new_dataframe=new_dataframe[motions_categories]

    #fill missing values. replace string values to numerical values
    new_dataframe=new_dataframe.fillna(0)
    for motion in motions:
        new_dataframe=new_dataframe.replace(motion,motions[motion])

    new_dataframe=new_dataframe.apply(pd.to_numeric, errors='coerce')
    new_dataframe = new_dataframe.fillna(0)
    new_dataframe[motions_categories]=new_dataframe[motions_categories].astype(int)
    return new_dataframe


new_dataframe=annotation_file_preprocessing(data,motions,motions_categories)
z=0
new_dataframe.to_csv("Mowgli3_F_2_preprocessed.csv")
print(new_dataframe)
