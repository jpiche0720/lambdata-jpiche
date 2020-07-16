

# abbreviation dictionaries

def state_abbreviations(df, state_col):
    '''    
    param: 
        df :: A pandas.DataFrame object

        state_col :: A pandas.Series object containing the abbreviations to transliterate
                     

    return: 
        A new pandas.DataFrame object with the of the spelled out state names
    '''
    
    state_abv_dict = {'al':'Alabama','ak':'Alaska','az':'Arizona','ar':'Arkansas','ca':'California',
                      'co':'Colorado','ct':'Connecticut','de':'Delaware','dc':'District of Columbia',
                      'fl':'Florida','ga':'Georgia','hi':'Hawaii','id':'Idaho','il':'Illinois',
                      'in':'Indiana','ia':'Iowa','ks':'Kansas','ky':'Kentucky','la':'Louisiana',
                      'me':'Maine','md':'Maryland','ma':'Massachusetts','mi':'Michigan','mn':'Minnesota',
                      'ms':'Mississippi','mo':'Missouri','mt':'Montana','ne':'Nebraska','nv':'Nevada',
                      'nh':'New Hampshire','nj':'New Jersey','nm':'New Mexico','ny':'New York',
                      'nc':'North Carolina','nd':'North Dakota','oh':'Ohio','ok':'Oklahoma','or':'Oregon',
                      'pa':'Pennsylvania','ri':'Rhode Island','sc':'South Carolina','sd':'South Dakota',
                      'tn':'Tennessee','tx':'Texas','ut':'Utah','vt':'Vermont','va':'Virginia',
                      'wa':'Washington','wv':'West Virginia','wi':'Wisconsin','wy':'Wyoming','pr':'Puerto Rico'}
    
    # Create working copy
    converted_df = df.copy()
    # Lowercase the series
    converted_df['state'] = state_col.str.lower()
    # Map the values 
    converted_df['state'] = converted_df['state'].map(state_abv_dict)
    
    return converted_df

if __name__ == '__main__':
    from pandas import DataFrame
    from pandas import Series
    df = DataFrame({'state':["CA","CO","CT","DC","TX"]})
    print(df.head())
    
    df2 = state_abbreviations(df, df['state'])
    print(df2.head())