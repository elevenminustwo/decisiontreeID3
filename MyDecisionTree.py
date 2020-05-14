from collections import Counter
import math 

attribute = [['Outlook'],['Temperature'],['Humidity'],['Windy'],['Play']]

data = [['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy'],
       ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
       ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
       ['FALSE','TRUE','FALSE','FALSE','FALSE','TRUE','TRUE','FALSE','FALSE','FALSE','TRUE','TRUE','FALSE','TRUE'],
       ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']]


def unique(list1): 
    unique_list = [] 
    for x in list1:  
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def find_entropy(data):
    entropy = 0 
    values = unique(data)
    value_counts = Counter(data)
    for value in values:
        probability = value_counts[value]/len(data)
        entropy += -probability*math.log(probability,2)
    print("E(s) = " + str(entropy))
    return entropy

def find_entropy_two_attributes(t_data,p_data):
    entropy = 0
    joined_data = []
    values = unique(p_data)
    for value in values:
        for i in range(len(p_data)):
            if(p_data[i]==value):
                joined_data.append(t_data[i]+p_data[i]);
        entropy += find_entropy(joined_data)*(len(joined_data)/len(p_data))
        joined_data.clear()
    print("E(T,X) : " + str(entropy))
    return entropy
def information_gain(data,data2):
    gain = find_entropy(data)-find_entropy_two_attributes(data,data2)
    print("Gain(T,X) : " + str(gain))
    
#TEST
print("Entropy using the frequency table of one attribute:")
find_entropy(data[-1]) #Target class
print("Entropy using the frequency table of two attributes:")
find_entropy_two_attributes(data[-1],data[0]) #Target class + one predictor class
print("Information Gain:")
information_gain(data[-1],data[0])
