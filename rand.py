import sys
import os
import random

"""That need to have two file in the same dir of tool file . That file name is not fucking care.Happy coding
   """

print("This is the name of the program:", sys.argv[0])
print("Argumen list:", str(sys.argv))

def fileread(x , y):
    if not os.path.exists(x):
            print(f"Error: File '{input_path}' not found.")
            return
            
    with open(x, 'r') as x_read:
        content = x_read.readlines()
                
    if not content:
        print("Warning: Input file is empty.")
        return
    content_list = list(content)
    random.shuffle(content_list)
    randomized = ''.join(content_list)


    with open(y, 'w') as outfile:
            outfile.write(randomized)
    
    print(f"Randomized content written to '{y}'.")
    
        
       
fileread(sys.argv[1], sys.argv[2])
