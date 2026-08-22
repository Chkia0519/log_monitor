with open("system.log", "r", encoding="utf-8") as file:
    logs = file.readlines()

info_count = 0
warning_count = 0
error_count = 0

error_logs = []

for log in logs:
    if "INFO" in log:
        info_count += 1

    elif "WARNING" in log:
        warning_count += 1

    elif "ERROR" in log:
        error_count += 1
        error_logs.append(log.strip())

print("INFO 數量：", info_count)
print("WARNING 數量：", warning_count)
print("ERROR 數量：", error_count)

if error_count > 0:
    print(f"\n系統存在 {error_count} 筆異常")
else:
    print("系統目前無 ERROR")
    
keyword = input("\n請輸入要搜尋的關鍵字：")

search_count = 0

for log in logs:
    if keyword in log:
        print(log.strip())
        search_count += 1

if search_count == 0:
    print("查無符合的 Log 紀錄")
else:
    print(f"\n共找到 {search_count} 筆紀錄")