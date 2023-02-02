
import pandas as pd


filename = 'CrossWord.jsonl'
csvFilePath = 'your_csv_file_path'

# append mode
# r	Open a file for reading. (default)
# w	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# x	Open a file for exclusive creation. If the file already exists, the operation fails.
# a Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# t	Open in text mode. (default)
# b	Open in binary mode.
# +	Open a file for updating (reading and writing)
openMode = 'a' 
df = pd.read_csv(csvFilePath, encoding='latin1')

file_object = open(filename, openMode)
for i in range(len(df)):
  file_object.write('{{"prompt":"{} ->", "completion":" {}###"}}\n'.format(df.Word[i],df.Clue[i]))
file_object.close()