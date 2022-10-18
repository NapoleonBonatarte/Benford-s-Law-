###
# Author: Tyler Windemuth
# Description: This program is a program that can iterate through a
#              data set and use said data said to determine if the data
#              is following Benford's law. This is done by iterating through
#              a csv file and sorting it, before then taking the newly sorted
#              data and running it through a function to turn the output into a float.
#              This output is then used to determine the beginning number of all of
#              numbers in the data set, which is then tested to determine if it falls
#              within the bounds of Benford's law. The file that is run is a file that
#              is designated by the user.
#

def counter(numbers):
    '''
    This function is a simple functions used to count the numbers of
    occurrences of numbers (1-9) in the beginning entries of a set of
    data. This data is then sent to a dictionary which is then returned.
    :param numbers: This parameter is all of the numbers that appear in the
    csv file that the user selects as the input.
    :return: This function returns a dictionary called dict_num, this dictionary has
    key values ranging from 1-9, with the values of the dictionary being based on the
    occurrences of said keys throughout the data set as the first integer.
    '''
    dict_num = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}  # establishing a dictionary of values
    for i in numbers:  # loop through the numbers data
        b = int(str(i)[0])  # setting the float equal to an integer
        if b:  # if b exists
            dict_num[b] += 1
    return dict_num


def load_file(file_name):
    '''
    This function opens the user specified file and reads data from said file.
    Once the data from this file is read this function then sorts the data by removing
    all of the endlines, and then splitting all of the entries in the data into a series
    of lists.
    :param file_name: This is a string that consists of the name of the file that the user
    enters, which is then used in the function.
    :return: This function returns a list of numbers called numbers, this list consists
    of every number that appears in the data set as long as it starts with an integer.
    '''
    file = open(file_name)  # opens file
    data = []  # established variables
    numbers = []
    for i in file:  # removing endlines and splitting data on ,'s
        data.append(i.strip('\n').split(','))
    for i in range(len(data)):  # works through data and if data is a number, append to data list
        for n in range(len(data[i])):
            if data[i][n][0].isnumeric():
                numbers.append(float(data[i][n]))
    return numbers



def print_plot(dict_num):
    '''
    This function calculates the proper percentages to display to the console,
    while also actually printing the proper chart to the console.
    :param dict_num: This is a dictionary of numbers that contains the key values
    1-9 with value pairs that consist of how many times the number corresponding to
    the key value appear within the initial data set.
    :return: This function returns a dictionary that contains a series of key values
    consisting of numbers between 1 and 9, which have value pairs that relate to the
    percentage of the bar chart that the number takes up.
    '''
    total = 0
    percentages_dict = {}
    for i in dict_num.values():  # counting total numbers in the dictionary
        total += i
    for i in range(len(dict_num)):  # calculating the percentages of each key value
        i += 1
        percentages_dict[i] = int((dict_num[i]/total)*100)
        print(i, "|", '#' * int((dict_num[i]/total)*100))
    return percentages_dict


def check_law(percentages_dict):
    '''
    This function checks the percentages of number that appear and uses
    said percentage to find if the original data set follows Benford's Law.
    :param percentages_dict: This parameter is a dictionary that contains
    key values of 1-9, with corresponding value pairs based off of the relationship
    between the total number of occurrences and the occurrences of that specific number
    relating to the key value of the dictionary, which in simple terms is the percantage
    of occurrences of the key in the data set.
    :return: This function has no return, rather what it does is it prints out
    the relationship of the data set to Benford's Law, in other words it determines
    if the data set follows Benford's Law.
    '''
    benford = True  # establishing variables
    value_list = [30,17,12,9,7,6,5,5,4]  # list containing theoretical values of Benford's law
    i = 0
    for values in percentages_dict.values():  # iterate through all values in dictionary
        if values < value_list[i] - 5 or values > value_list[i] + 10:
            benford = False
        i += 1

    if benford:  # prints if data follows Benford's law
        print('\nFollows Benford\'s Law')
    else:  # prints if data does not follow Benford's Law
        print('\nDoes not follow Benford\'s Law')




def main():
    file_name = input("Data file name:\n\n")  # asks for user input as a file name
    numbers = load_file(file_name)  # calls load file function
    dict_num = counter(numbers)  # calls counter function
    percentages_dict = print_plot(dict_num)  # calls print_plot function
    check_law(percentages_dict)  # calls check law function


main()
