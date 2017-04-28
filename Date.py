def main():

   print('Enter a date (mm/dd/yyyy): ', end='')
   date = str(input())

   print('The new date is: ', end='')

   print(date_converter(date))



def date_converter(date):

   date_list = date.split('/')

   list2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
           'November', 'December']

   index = int(date_list[0]) - 1

   month = list2[index]

   new = month + " " + date_list[1] + "," + date_list[2]

   return new

main()
