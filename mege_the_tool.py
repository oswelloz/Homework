def merge_the_tools(string, k):
    # your code goes here
    # create length of the substring
    # loop through each number/postion in k
    # set position for the first subset [start to end] 
    # split string into different sub strings 
    # create a set of each sub string
    # print out each substring 

    length_subtring = len(string)/k 
    for num in range(k):
        starting_point = int(num * length_subtring)
        end = int((num +1) * length_subtring)
        sub_string = string[starting_point:end]
        print(''.join(set(sub_string)))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)