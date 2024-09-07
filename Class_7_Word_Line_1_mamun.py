
import re , os
os.system('cls')
print()


def count_words_lines(filename):

    with open(filename, 'r' , encoding='utf-8' ) as file: # 

        lines = file.readlines()  # return list value of lines 
        num_lines = len(lines)    # Total lines count
        num_words = sum(len(line.split()) for line in lines)  # Total words count

        file.seek(0)
        wc=0
        for line  in lines:  
            for x in line.split():
              wc+=1 
 
        #num_words2 
        for line in lines:
                words = line.split()     # Split the line into words
                num_words2 += len(words)  # Add the number of words in the line to the total count


        print ("List/Lines : ", lines )
        print ("WC : ", wc , "\n")

    return num_lines, num_words, str(file.read())

# Program Start here 
filename = 'G:\\test2.txt'  
lines, words , file_content  = count_words_lines(filename)
print(f"Total lines:: {lines}")
print(f"Total words:: {words}")

print(f"File Content :: {file_content}")


