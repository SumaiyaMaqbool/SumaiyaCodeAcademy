def insertionSort(array):
    for step in range (1, len(array)):
        key = array[step]
        j= step -1
        
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j=j-1
        array[j+1] = key        
#array = [6,1,2,5,10]
#insertionSort(array)
#print(array)
def bubblesort(list):
# Swap the elements to arrange in order
   for iter_num in range(len(list)-1,0,-1):
      for idx in range(iter_num):
         if list[idx]>list[idx+1]:
            temp = list[idx]
            list[idx] = list[idx+1]
            list[idx+1] = temp
#list = [19,2,31,45,6,11,121,27]
#bubblesort(list)
#print(list)
def selection_sort(input_list):
   for idx in range(len(input_list)):
      min_idx = idx
      for j in range( idx +1, len(input_list)):
         if input_list[min_idx] > input_list[j]:
            min_idx = j
      # Swap the minimum value with the compared value
      input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
#l = [19,2,31,45,30,11,121,27]
#selection_sort(l)
#print(l)
def sort():
    userAnswer = input ("Hi do you want to enter a list of numbers and sort it? (y/n)\n").lower()
    lstNumbers = []
    while userAnswer=="y":
        size_list= int(input("Enter the length of your list \n"))
        print()
        for i in range (size_list):
            number = int(input("Add a number to your list : "))
            lstNumbers.append(number)
        print ("The Original List: ", lstNumbers)
        print()
        sort_type = input("Select a sorting type, select a,b or c:\n a.Insertion Sort\n b.Selection Sort\n c.Bubble Sort\n").lower()
        #while  sort_type == 'a' or sort_type == 'b' or sort_type == 'c' :
            #try:
        if sort_type == 'a':
             insertionSort(lstNumbers)
             print ("The sorted list : ",lstNumbers, "\nit was sorted by Insertion Sort type which involves finding the right\n place for the given element and sort them by comparing them.\n So it starts with the first two elements and compare them together and then the smallest value will come infront and so on.\n it keeps comparing them and moving them until all the elements in the list have been compared and placed in their right position.\n")
        elif sort_type == 'c':
             bubblesort(lstNumbers)
             print("The sorted list : ",lstNumbers, "\n it was sorted by Bubble Sort which involves dealing with the comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.\n")
        elif sort_type == 'b':
             selection_sort(lstNumbers)
             print("The sorted list : ",lstNumbers, "\n it was sorted by Selection Sort which starts by finding the smallest element and adding it to the list and the exact same thing goes for the other elements.\n the entered element will be compared with the other elements and it will be placed in the right place , starting from the smallest element and acsending.")
        else:
            if userAnswer == 'n':
                print("Okay, see you next time!")
                break
        #except:
                #continue
            
        userAnswer = input ("Do you want to enter a list of numbers and sort it again? (y/n)\n")
        lstNumbers=[]
  
    print("Okay, see you next time!")          
        
sort()
        
        
    