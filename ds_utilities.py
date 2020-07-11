import pandas as pd

def insert_row(df, row_number, row_value): 
    '''

    param:
        df :: a <pandas.DataFrame> object with a numerical index
        
        row_number :: The index in which the new row will take

        row_value :: <List> object of the new row to be placed

    returns:
        A <pandas.DataFrame> object with the newly inserted row

    '''

   
    # Define the upper half of the DataFrame 
    start_upper = 0
    end_upper = row_number 
   
    # Define the lower Half of the DataFrame
    start_lower = row_number 
    end_lower = df.shape[0] 
   
    # Create lists of each halfs' index index 
    upper_half = [*range(start_upper, end_upper, 1)] 
    lower_half = [*range(start_lower, end_lower, 1)] 
   
    # Increment the value of lower half by 1 
    lower_half = [x.__add__(1) for x in lower_half] 
   
    # Combine the two lists 
    index_ = upper_half + lower_half 
   
    # Update the index of the dataframe 
    df.index = index_ 
   
    # Insert a row at the end 
    df.loc[row_number] = row_value 
    
    # Sort the index labels 
    df = df.sort_index() 
   
    return df

if __name__ == '__main__':

    import pandas as pd

    data = {'A':[2,2,3,3,4], 'B':[1,2,4,6,7], 'C': [2,3,5,7,8]}
    df = pd.DataFrame(data)
    print(df)

    df = insert_row(df, 2, ['ADD','ADD','ADD'])
    print(df)

