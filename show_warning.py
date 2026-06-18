with open("app.log","r") as file:
    for line in file:
        if "WARNING" in line:
            print(line)
