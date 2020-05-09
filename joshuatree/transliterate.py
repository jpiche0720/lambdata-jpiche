

# abbreviation dictionaries

def state_abbreviations(X):
    '''    
    parameters: 
                - list/series of USA state abbreviations
    return: 
                - a pandas.Series object of the spelled out state names
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
    
    
    X = X.copy()
    X = X['abbrev'].str.lower()
    X = X.map(state_abv_dict)
    return X

if __name__ == '__main__':
    from pandas import DataFrame
    from pandas import Series
    df = DataFrame({'abbrev':["CA","CO","CT","DC","TX"]})
    print(df.head())
    
    df2 = state_abbreviations(df)
    print(df2.head())