def bubble_sort(my_list):
          for i in range(len(my_list)-1,0,-1):
                    for j in range(i):
                              if my_list[j]>my_list[j+1]:
                                        temp = my_list[j]
                                        my_list[j] = my_list[j+1]
                                        my_list[j+1] = temp
          print(my_list)

bubble_sort([4,2,1,3,6,5])          
