import numpy as np 
import ast

def generate_tweets_list(dataframe_single):
    '''
    Parameters
    ----------
    dataframe_single : dataframe 
        It is a dataset that you collected before. 

    Returns
    -------
    train_x_arr : list 
        Converted version of the argument 
    '''
    train_x_arr = [] 
    for index, row in dataframe_single.iterrows(): 
        for a in row.values: 
            train_x_arr.append(ast.literal_eval(a))
            
    return train_x_arr

def build_freqs(train_x, train_y):
    '''
    Parameters
    ----------
    train_x : list
        list of your X 
    train_y : list 
        List of your Y 
    Returns
    -------
    freqs : dict 
        it returns dictionary that includes key and values like below; 
        (word, label) : number of times appeared 
    '''
    
    yslist = np.squeeze(train_y).tolist()
    
    freqs = {}
    for y, tweet in zip(yslist, train_x):
        for word in tweet:
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1

    return freqs

# -------------------------------- 
# Naive Bayes Functions 


