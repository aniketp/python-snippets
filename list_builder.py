
def final_sent(*args):
    sentence = ''

    for i in args:
        sentence = sentence + str(i)+ ' '

    print(sentence)


input_list = []

print("Enter the words of the sentence")
print("Hit 'Enter' to stop")

test_input = input()


while(test_input!=''):
    input_list.append(test_input)

    test_input = input()


final_sent(*input_list)

#print(input_list)
    

