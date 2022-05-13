# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1872442:UOW / 20211132:IIT
# Date: 30/11/2021

progress_count = trailer_count = retriever_count = excluded_count = 0

def main():
    check = 'y'
    while True:  #use while loop to repeat score checking process,
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
                        progress(credit_pass)
                        progress_mod(credit_pass)
                        do_not_progress(credit_pass, credit_fail)
                        exclude(credit_pass, credit_fail)

                else: print("out of range")
            else: print("out of range")
        else: print("out of range")

    except: print("Integer required")


def progress(credit_pass):
    if credit_pass == 120:
        global progress_count #call global progress_count variable
        print("Progress")
        progress_count += 1 #counting progress sets


def progress_mod(credit_pass):
    if credit_pass == 100:
        global trailer_count #call global trailer_count variable
        print("Progress (module trailer)")
        trailer_count += 1 #counting trailer_count sets


def do_not_progress(credit_pass, credit_fail):
    if 0 <= credit_pass <= 80 and credit_fail <= 60:
        global retriever_count #call global retriever_count variable
        print("Do not progress - module retriever")
        retriever_count += 1 #counting retriever_count sets


def exclude(credit_pass, credit_fail):
    if credit_pass <= 40 and credit_fail >= 80:
        global excluded_count #call global excluded_count variable
        print("Exclude")
        excluded_count += 1 #counting excluded_count sets


def histogram():
    print("progress : ", "*"*progress_count)
    print("Trailer  : ", "*"*trailer_count)
    print("Retriever: ", "*"*retriever_count)
    print("Excluded : ", "*"*excluded_count)
    total_out = progress_count + trailer_count + retriever_count + excluded_count
    print("\n", total_out, " outcomes in total")


if __name__ == '__main__':
    main()
