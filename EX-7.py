#Candidate Elimination Algorithm
import csv  
with open("trainingdata.csv", "r") as file:  
  data = list(csv.reader(file))  
training_data = data[1:]  
attributes = header[:-1]  
domains = []   
for i in range(len(attributes)):     
  values = set(row[i] for row in training_data)    
  domains.append(values) 
S = ['0'] * len(attributes)  
G = [['?'] * len(attributes)]  
print("Initial S:", S)  
print("Initial G:", G)  
for example in training_data:   
   x = example[:-1]      
   target = example[-1]        
   if target == "Yes":           
      G = [     
         g for g in G      
         if all(       
           g[i] == '?' or g[i] == x[i]     
           for i in range(len(x)) 
         )     
     ]       
    for i in range(len(S)):   
            if S[i] == '0':      
            S[i] = x[i]        
       elif S[i] != x[i]:     
             S[i] = '?'  
    else:          
         new_G = []           
         for g in G:           
             covers = all(     
             g[i] == '?' or g[i] == x[i]          
             for i in range(len(x))    
          )       
       if covers:   
               for i in range(len(x)):            
                       if g[i] == '?':           
                    for value in domains[i]:           
                        if value != x[i]:       
                           new_hypothesis = g.copy()          
                           new_hypothesis[i] = value                    
                          # Must be more general than S     
                          valid = True       
                          for j in range(len(x)):       
                              if S[j] != '0' and \        
                                 S[j] != '?' and \  
                                  new_hypothesis[j] != '?' and \                            
                                 S[j] != new_hypothesis[j]:          
                                 valid = False       
                           if valid:             
                              new_G.append(new_hypothesis)       
       else:       
           new_G.append(g)   
       G = new_G   
        print("\nExample:", x)      
        print("Target:", target)  
        print("S =", S)  
        print("G =", G) print("\n==============================")  
        print("FINAL VERSION SPACE")  
        print("==============================")   
        print("\nSpecific Boundary (S):") 
        print(S)  
        print("\nGeneral Boundary (G):")  
        for g in G:     
        print(g) 
