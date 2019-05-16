with open("files.txt", "w") as first_file:
    first_file.write("Writing files is great\n")
    first_file.write("Here's another line of text\n")
    first_file.write("Closing now, goodbye!")

    first_file.write("Here's one more file\n")
    first_file.write("What about the older one?\n")
    first_file.write("Let's go check it out")
with open("lol.txt", "w") as file:
    file.write("haha" * 50)