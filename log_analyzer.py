with open("system.log", "r", encoding="utf-8") as file:
    logs = file.readlines()

info_count = 0
warning_count = 0
error_count = 0

for log in logs:
    if "INFO" in log:
        info_count += 1

    elif "WARNING" in log:
        warning_count += 1

    elif "ERROR" in log:
        error_count += 1

print("INFO 數量：", info_count)
print("WARNING 數量：", warning_count)
print("ERROR 數量：", error_count)