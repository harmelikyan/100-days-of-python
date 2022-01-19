try:
     file = open("a_file.txt")
     my_dict = {"key": "value"}
     print(my_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message}  does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
