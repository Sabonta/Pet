def main():

    list = [1, 2, 5, 10]

    n = 2

    larger(list, n)


def larger(my_list, n):

    print('The numbers grater than n are:')

    for num in my_list:
        if num > n:
           print(num)

main()