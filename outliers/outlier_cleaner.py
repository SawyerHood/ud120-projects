#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    ### your code goes here
    cleaned_data = [(x[1], x[2], x[0]-x[2]) for x in zip(predictions, ages, net_worths)]
    cleaned_data = sorted(cleaned_data, lambda x,y: cmp(x[2], y[2]), reverse=True)
    return cleaned_data[int(len(cleaned_data) * 0.1):]
