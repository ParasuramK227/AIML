#Decision Tree based ID3 Algorithm
import pandas as pd 
import numpy as np 
from math import log2 
def entropy(target_col): 
elements,counts=np.unique(target  _col, return_counts=True) 
    entropy_value = np.sum([ 
       -(counts[i] / np.sum(counts))* 
        log2(counts[i] / np.sum(counts)) 
        for i in range(len(elements)) 
    ]) 
def info_gain(data, split_attribute, target_name="Play"): 
    total_entropy = entropy(data[target_name]) 
    vals, counts = np.unique(data[split_attribute], return_counts=True) 
    weighted_entropy = np.sum([ 
        (counts[i] / np.sum(counts)*)
                entropy(data.where(data[split_attribute] == vals[i]).dropna()[target_name]) 
                for i in range(len(vals)) 
        ]) 
    return total_entropy - weighted_entropy 
def id3(data, originaldata, features, target_attribute_name="Play", parent_node_class=None): 
    if len(np.unique(data[target_attribute_name])) <= 1: 
        return np.unique(data[target_attribute_name])[0] 
   elif len(data) == 0: 
        return np.unique(originaldata[target_attribute_name])[ 
        np.argmax(np.unique(originaldata[target_attribute_name], 
            return_counts=True)[1]) 
        ] 
   elif len(features) == 0: 
        return parent_node_class 
 
   else: 
        parent_node_class = np.unique(data[target_attribute_name])[ 
            np.argmax(np.unique(data[target_attribute_name], 
            return_counts=True)[1]) 
        ] 
        item_values = [info_gain(data, feature, target_attribute_name) 
                       for feature in features] 
        best_feature_index = np.argmax(item_values) 
        best_feature = features[best_feature_index] 
        tree = {best_feature: {}} 
        features = [i for i in features if i != best_feature] 
        for value in np.unique(data[best_feature]): 
            sub_data = data.where(data[best_feature] == value).dropna() 
            subtree = id3( 
                sub_data,   
                originaldata, 
                features, 
                target_attribute_name, 
                parent_node_class 
            ) 
            tree[best_feature][value] = subtree 
        return tree 
data = { 'Outlook':['Sunny','Sunny','Overcast','Rain','Rain', 
                'Rain','Overcast','Sunny','Sunny','Rain',       
              'Sunny','Overcast','Overcast','Rain'], 
 'Temperature':['Hot','Hot','Hot','Mild','Cool', 
                    'Cool','Cool','Mild','Cool','Mild', 
                         'Mild','Mild','Hot','Mild'], 
  'Humidity': ['High','High','High','High','Normal', 
                      'Normal','Normal','High','Normal','Normal', 
                      'Normal','High','Normal','High'], 
 'Wind':['Weak','Strong','Weak','Weak','Weak', 
             'Strong','Strong','Weak','Weak','Weak', 
             'Strong','Strong','Weak','Strong'], 
    'Play': ['No','No','Yes','Yes','Yes', 
             'No','Yes','No','Yes','Yes', 
             'Yes','Yes','Yes','No'] 
} 
df = pd.DataFrame(data) 
features = df.columns[:-1].tolist() 
tree = id3(df, df, features) 
print("Decision Tree:") 
print(tree) 
