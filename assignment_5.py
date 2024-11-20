def lab_1():
  num_scores = int(input("Enter the number of scores: "))
  scores_list = []
  for i in range(num_scores):
    score = float(input(f"Enter score number {i+1}: "))
    scores_list.append(score)
  print(scores_list)
  avg_score = sum(scores_list)/len(scores_list)
  if avg_score >= 90:
    print("A", avg_score)
  elif avg_score >= 80 and avg_score < 90:
    print("B", avg_score)
  elif avg_score >= 70 and avg_score < 80:
    print("C", avg_score)
  elif avg_score >= 60 and avg_score < 70:
    print("D", avg_score)
  else:
    print("F", avg_score)

lab_1() 

def lab_2():
  even_list = []
  odd_list = []
  nums = input("Enter multiple integers separated by spaces ")
  nums_list = nums.split(" ")
  for num in nums_list:
    if int(num)%2 == 0:
        even_list.append(num)
    else:
      odd_list.append(num)
  print("Number of even integers: ",len(even_list))
  print("Number of odd integers: ",len(odd_list))
    
lab_2()

def lab_3():
  list_one = input("Enter one list of integers separated by spaces " )
  list_two = input("Enter a second list of integers separated by spaces " )
  list_one_nums = list_one.split(" ")
  list_two_nums = list_two.split(" ")
  list_one = [int(num) for num in list_one_nums]
  list_two = [int(num) for num in list_two_nums]
  for num in list_one:
    if num in list_two:
      list_two.remove(num)
  print("Here's your merged list without duplicates: ",list_one + list_two)

lab_3()