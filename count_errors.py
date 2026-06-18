error_count = 0
with open("app.log","r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
print("Total Errors:",error_count)
