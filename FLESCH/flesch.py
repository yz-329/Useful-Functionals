import syllapy
import os

def sentence_count(filename):
    file = open(filename, 'r')
    lst = file.read().split(".")
    file.close()

    return len(lst)

def split_words(filename):
    file = open(filename, 'r')
    lst = file.read().split()
    file.close()

    return lst

def word_count(filename):
    return len(split_words(filename))

def syllable_count(filename):
    lst = split_words(filename)

    sum = 0
    for word in lst:
        #print(word)
        s = ""
        if word.isalpha() == False:
            string = word.split()
            for i in range(len(string)):
                if string[i].isalpha:
                    s += string[i]
                else:
                    s += ""
            sum += syllapy.count(s) 
        else:
            sum += syllapy.count(word) 
        
    return sum


def custom_sort(file_name):
        try:
            return int(file_name.split('_')[1].split('.')[0])
        except:
            return 0
    
folder_path = 'path\\to\\folder'

count = 0
new = open("Word Count.txt", "w")
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_list = os.listdir(folder_path)

    file_list.sort(key=custom_sort)

    for file_name in file_list:
        
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            try:
                s_count = sentence_count(file_path)
                w_count = word_count(file_path)
                sylla_count = syllable_count(file_path)
                

                score = round(206.835 - 1.015 * (w_count / s_count) - 84.6 * (sylla_count / w_count), 2)
                read = round(0.39 * (w_count / s_count) + 11.8 * (sylla_count / w_count) - 15.59 , 2)
            except:
                score = 0
                read = 0

            new.write(f"{file_path[27:]}\t{w_count - 1}\n")
            
            if score != 0:
                print(s_count, w_count, sylla_count)
            
new.close()

