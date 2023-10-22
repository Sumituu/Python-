#Create a program that prompts the user to enter numbers until they enter 'q'
to quit, then calculate the sum.sum = 0

while True:
  number = input("Enter a number (q to quit): ")

  if number == "q":
    break


  number = float(number)


  sum += number


print("The sum is:", sum)
