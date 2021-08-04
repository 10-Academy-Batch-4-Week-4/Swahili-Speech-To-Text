import os
def load_data(dataset_path):
    labels=[]
    # dictionary to store files
   
    # loop through all sub-folders
    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):

        # ensure we're processing at sub-folder level
        if dirpath is not dataset_path:

            # save label (i.e., sub-folder name) in the mapping eg SWH-05-20101106
            label = dirpath.split("/")[-1]

            # process all audio files in the sub-directory
            for f in filenames:

		        # load audio file
                filename="wav/"+label+"/"+f
                labels.append(filename)
    return labels
if __name__ == "__main__":
    load_data(dataset_path)                 