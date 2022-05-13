# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1872442:UOW / 20211132:IIT
# Date: 30/11/2021

progress_count = trailer_count = retriever_count = excluded_count = 0
#assign empty lists for progress, module trailer, Do not progress - module retriever, Exclude
progress_list = []
trailer_list = []
retriever_list = []
excluded_list = []
#assign empty list for print all inputs
marks_input = []


def main():
    check = 'y'
    while True: #use while loop to repeat score checking process,
        if check == 'y': #check user need to enter another set of data or quit
            check_in()
            check = input("\nWould you like to enter another set of data?\n"
                          "Enter 'y' for yes or 'q' to quit and view results: ")

        elif check == 'q':
            histogram() #call histogram function
            break

        else:
            print("Wrong input so program quit")
            break


def check_in():
    try: #if user doesn't input integer it will catch except
        credit_pass = int(input("Please enter your credit at pass: "))
        if credit_pass % 20 == 0 and credit_pass <= 120:
            credit_defer = int(input("Please enter your credit at defer: "))

            if credit_defer % 20 == 0 and credit_defer <= 120:
                credit_fail = int(input("Please enter your credit at defer: "))

                if credit_fail % 20 == 0 and credit_fail <= 120:
                    total = credit_pass + credit_defer + credit_fail

                    if total != 120: #check total equal 120 or not
                        print("Total incorrect")

                    else: #call other functions
                        progress(credit_pass, credit_defer, credit_fail)
                        progress_mod(credit_pass, credit_defer, credit_fail)
                        do_not_progress(credit_pass, credit_defer, credit_fail)
                        exclude(credit_pass, credit_defer, credit_fail)

                else:
                    print("out of range")
            else:
                print("out of range")
        else:
            print("out of range")

    except:
        print("Integer required")


def progress(credit_pass, credit_defer, credit_fail):
    if credit_pass == 120:
        global progress_count #call global progress_count variable
        marks_input.append("Progress: " + str(credit_pass) + "," + str(credit_defer) + "," + str(credit_fail)) #append mark input list
        print("Progress")
        progress_count += 1 #counting progress sets
        progress_list.insert(0, "*") #if progress has a count it insert list as "*"

    else:
        progress_list.append(" ") #if progress doesn't has value it append " "


def progress_mod(credit_pass, credit_defer, credit_fail):
    if credit_pass == 100:
        global trailer_count #call global trailer_count variable
        marks_input.append("Progress (module trailer): " + str(credit_pass) + "," + str(credit_defer) + "," + str(credit_fail)) #append mark input list
        print("Progress (module trailer)")
        trailer_count += 1 #counting trailer_count sets
        trailer_list.insert(0, "*") #if progress_mod has a count it insert list as "*"

    else:
        trailer_list.append(" ") #if progress_mod doesn't has value it append " "


def do_not_progress(credit_pass, credit_defer, credit_fail):
    if 0 <= credit_pass <= 80 and credit_fail <= 60:
        global retriever_count #call global retriever_count variable
        marks_input.append("module retriever: " + str(credit_pass) + "," + str(credit_defer) + "," + str(credit_fail)) #append mark input list
        print("Do not progress - module retriever")
        retriever_count += 1 #counting retriever_count sets
        retriever_list.insert(0, "*") #if do_not_progress has a count it insert list as "*"
    else:
        retriever_list.append(" ") #if do_not_progress doesn't has value it append " "


def exclude(credit_pass, credit_defer, credit_fail):
    if credit_pass <= 40 and credit_fail >= 80:
        global excluded_count #call global excluded_count variable
        marks_input.append("Exclude: " + str(credit_pass) + "," + str(credit_defer) + "," + str(credit_fail)) #append mark input list
        print("Exclude")
        excluded_count += 1 #counting excluded_count sets
        excluded_list.insert(0, "*") #if exclude has a count it insert list as "*"

    else:
        excluded_list.append(" ") #if exclude doesn't has value it append " "


def histogram():

    print("progress : ", "*" * progress_count)
    print("Trailer  : ", "*" * trailer_count)
    print("Retriever: ", "*" * retriever_count)
    print("Excluded : ", "*" * excluded_count)
    total_out = progress_count + trailer_count + retriever_count + excluded_count
    print("\n", total_out, " outcomes in total")

    number_list = [progress_count, trailer_count, retriever_count, excluded_count]
    max_value = max(number_list) #use max value because find the length of rows
    print('progress {} Trailer {} Retriever {} Excluded {}'.format(progress_count, trailer_count, retriever_count, excluded_count))

    for x in range(max_value):
        print(f'{progress_list[x]:>6}', end=" ")  #use f-string and make 6 spaces
        print(f'{trailer_list[x]:>9}', end=" ")   #use f-string and make 9 spaces
        print(f'{retriever_list[x]:>10}', end=" ") #use f-string and make 10 spaces
        print(f'{excluded_list[x]:>10}')           #use f-string and make 10 spaces

    print("\n", total_out, " outcomes in total\n")
    
    for i in marks_input:
        print(i) #read all mark inputs


if __name__ == '__main__':
    main()
