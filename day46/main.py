import os
if(not os.path.exists("data")):
    os.mkdir("data")
for i in range(0,100):
    # Create a new folder
    # os.mkdir(f"data/day{i+1}")
    
    # rename folder
    os.rename(f"data/day{i+1}", f"data/tutorial {i+1}")