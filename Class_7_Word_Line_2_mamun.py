

def count_words_and_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Read all lines from the file
            num_lines = len(lines)    # Count the number of lines
            num_words = 0
            
            for line in lines:
                words = line.split()  # Split the line into words
                num_words += len(words)  # Add the number of words in the line to the total count
            
            #  num_words = sum(len(line.split()) for line in lines)  # Total words count

            return num_lines, num_words
    
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None, None

# Example usage
file_path = 'G:\\test2.txt'   # Replace with the path to your file
lines, words = count_words_and_lines(file_path)

if lines is not None:
    print(f"Total Lines: {lines}")
    print(f"Total Words: {words}")


