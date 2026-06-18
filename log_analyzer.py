error_count = 0
info_count = 0
warning_count = 0

with open("app.log","r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1
        if "INFO" in line:
            info_count += 1
        if "WARNING" in line:
            warning_count += 1

print("INFO Messages:", info_count)
print("ERROR Messages:", error_count)
print("WARNING Messages:", warning_count)
