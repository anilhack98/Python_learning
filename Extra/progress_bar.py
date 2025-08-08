from tqdm import tqdm
import time
files=['file1.zip','file2.zip','file3.zip']
print("Starting the downloads...\n")
for file in tqdm(files,desc="Downloading",unit="file"):
    time.sleep(1)
    print(f"(file) downloaded")
    print("\n All files downloaded successfully")