# #Question 2.
def frequencyOfWords(sentence):
    wordStore = {}
    words = sentence.split()

    for i in words:
        wordStore[i] = wordStore.get(i, 0) + 1

    # returning the frequency of words stored in wordStore
    return wordStore

def file_processing(input_file, output_file):
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        # Read all lines from the input file and concatenate them into a single string
        sentences = ' '.join(line.strip() for line in input_file)

        # for calculating the word count:
        wordStore = frequencyOfWords(sentences)

        # writing the original sentence in output file:
        output_file.write("Input sentence is: " + sentences + "\n" + "\n")
        output_file.write("Frequency of words:" + "\n" + "\n")

        # writing the word count for each word
        for word, count in wordStore.items():
            output_file.write(f"{word}: {count}" + "\n")

        output_file.write("\n")

# starts the file processing for finding the frequency of words
file_processing('input.txt', 'output.txt')
