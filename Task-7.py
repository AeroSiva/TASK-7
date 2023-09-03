# Q1. Write a Python program using Function to which will do the following.:-
    # a) The function will create a text file with the timestamp.
    # b) the file content should have the content of the current timestamp.


def create_txt_w_ts ():
    import datetime
    time = datetime.now.strftime("%d-%m-%y  %H:%M:%S")
    with open("Text_file_w_ts.txt", mode="w") as file:
        file.write(time)

    print("Timestamp is written to 'Text_file_w_ts.txt' file.")

create_txt_w_ts ()



# Q2. Write another Python function to read from a text file.
# The function will take take the name of the text file and display the content of the file into the console.

def show_content () :
    fi = 'Text_file_w_ts.txt'
    with open("Text_file_w_ts.txt", mode="r") as file:
        content = fi.read()
    print('The file content is ', content)

show_content()







