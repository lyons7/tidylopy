import pandas as pd
import numpy as np


"""Fx to get weighted log odds"""
def get_weighted_log_odds(dataFrame, groupSet, featureName, nCount):
    """
    Fx to get weighted log odds ratio of features depending on their grouping.
    Adapted from https://github.com/juliasilge/tidylo/blob/main/R/bind_log_odds.R
    Input is a dataframe that has columns of your set (groups you are comparing to one another),
    feature (the thing you want to see the weighted log odds of) and the count (n) of
    features per set. This is flexible enough to get weighted log odds of any set, feature
    and count combination.
    """
    alphas = dataFrame.groupby(featureName).sum(nCount).reset_index()[[featureName, nCount]].rename(columns={nCount:'alpha'})  # Get total # of features across whole dataset
    dataFrame_II = dataFrame.merge(alphas, on= featureName, how = 'left')
    dataFrame_II['y_wi'] = dataFrame_II['n'] + dataFrame_II['alpha']  # "y_wi is the pseudo count of word w in group i"
    y_ws = dataFrame_II.groupby(featureName).sum('y_wi').reset_index()[[featureName, 'y_wi']].rename(columns={'y_wi': 'y_w'})  # "y_w is the total count of word w"
    # Actually is sort of an exaggerated count ¯\_(ツ)_/¯
    dataFrame_III = dataFrame_II.merge(y_ws, on=featureName, how='left')
    # Do exaggerated count per set:
    n_is = dataFrame_II.groupby(groupSet).sum('y_wi').reset_index()[[groupSet, 'y_wi']].rename(columns={'y_wi': 'n_i'})
    pseudo_counts = dataFrame_III.merge(n_is, on= groupSet, how = 'left')  # Combine everything together! Now ready to do weighted log odds calc
    pseudo_counts['omega_wi'] = pseudo_counts['y_wi'] / (pseudo_counts['n_i'] - pseudo_counts['y_wi'])  # # odds in group i
    pseudo_counts['omega_w'] = pseudo_counts['y_w'] / (sum(pseudo_counts['y_wi']) - pseudo_counts['y_w'])  # overall odds
    pseudo_counts['delta_wi'] = (np.log(pseudo_counts['omega_wi'])) - (np.log(pseudo_counts['omega_w']))   # eqn 15
    pseudo_counts['sigma2_wi'] = 1 / pseudo_counts['y_wi'] + 1 / pseudo_counts['y_w']           # eqn 18
    pseudo_counts['zeta_wi'] = pseudo_counts['delta_wi'] / (np.sqrt(pseudo_counts['sigma2_wi']))       # eqn 21
    return pseudo_counts.rename(columns={'zeta_wi': 'log_odds_weighted', 'delta_wi': 'log_odds'}).sort_values('log_odds_weighted', ascending = False)
