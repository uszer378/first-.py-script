#hello 

print("hello this a test")

name = input("what is your name?\n")

print(f"hello {name}, and thanks for testing my project\n\n")

any_feed_back = input("any feedback? (yes or no) \n")

if any_feed_back == "yes":
  deide = input("what else should i make " + name + "?\n")

  try:
    with open("ideas.txt", "a") as file:
      file.write(f"\nNew idea: {deide}")
  except FileNotFoundError:
    print("File 'ideas.txt' not found. Creating a new one.")
    with open("ideas.txt", "w") as file:
      file.write(f"New idea: {deide}")

if any_feed_back == "no":
  print("thanks for testing, " + name + "!")

exit()
