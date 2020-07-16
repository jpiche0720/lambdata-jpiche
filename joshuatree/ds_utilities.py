import pandas as pd
### CSV downloadlink
from IPython.display import display, FileLink, FileLinks 


def csv_download_link(df, csv_file_name):
    '''
    Display a download link to load a pandas.DataFrame as csv file
    
    param:
        df :: a pandas.DataFrame object

        csv_file_name :: The name the new CSV file will take

    return:
        A download link containing the csv file
    '''
    df.to_csv(csv_file_name, index=False)

    link = display(FileLink(csv_file_name))

    return link


def insert_row(df, row_number, row_value):
    '''
    param:
        X :: A pandas.DataFrame object with a numerical index

        row_number :: The index in which the new row will take

        row_value :: A list object of the new row to be placed

    return:
        A pandas.DataFrame object with the newly inserted row

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


def seperate_dates(df, date_col):
    '''
    Seperate a column of dates in a pandas.DataFrame into respective columns month, day, year 

    param:
        df :: A pandas.DataFrame object

        date_col :: A pandas.Series object 

    return:
        A new DataFrame object with 3 new columns (month, day, year)

    
    '''

    # Create working copy
    converted_df = df.copy()
    # Ensure date column is in datetime format 
    date_col = pd.to_datetime(date_col)
    # Create new columns 
    converted_df['month'] = pd.to_datetime(date_col).dt.month
    converted_df['day'] = pd.to_datetime(date_col).dt.day
    converted_df['year'] = pd.to_datetime(date_col).dt.year

    return converted_df



if __name__ == '__main__':
    import pandas as pd

#     data = {'A':[2,2,3,3,4], 'B':[1,2,4,6,7], 'C': [2,3,5,7,8]}
#     df = pd.DataFrame(data)
#     print(df)

#     df = insert_row(df, 2, ['ADD','ADD','ADD'])
#     print(df)

    # raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
    #             'age': [20, 19, 22, 21],
    #             'favorite_color': ['blue', 'red', 'yellow', "green"],
    #             'grade': [88, 92, 95, 70],
    #             'birth_date': ['01-02-1996', '08-05-1997', '04-28-1996', '12-16-1995']}
    # df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])

    # df = seperate_dates(df, df['birth_date'])

    # print(df)

    # Diplay download link:
    # df = pd.DataFrame({'A':[2,2,2],'B':[3,3,3],'C':[6,6,4]})
    # csv_download_link(df, 'Project.csv')

