def main():

   print('The new date is:', date_converter())



def date_converter():
   print('Enter a date (mm/dd/yyyy): ', end='')
   date = str(input())

   date_list = date.split('/')

   list2 = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
           'November', 'December']

   index = int(date_list[0]) - 1

   month = list2[index]

   new = print(month, " ", date_list[1], ",", date_list[2], sep='')

   return new

main()
