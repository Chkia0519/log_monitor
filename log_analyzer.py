import sys
from datetime import datetime,timedelta

#可依需求更動偵測分鐘數
minute=2

try:
    with open("system.log", "r", encoding="utf-8") as file:
        logs = file.readlines()

except FileNotFoundError:
    print("找不到 system.log，請確認 Log 檔案是否存在")
    sys.exit()
    
#篩選最近指定分鐘log    
recent_logs = []

ten_minutes_ago = datetime.now() - timedelta(minutes=minute)

for log in logs:
    try:
        time_text = log.split(" - ")[0]

        log_time = datetime.strptime(
            time_text,
            "%Y-%m-%d %H:%M:%S,%f"
        )

        if log_time >= ten_minutes_ago:
            recent_logs.append(log)

    except ValueError:
        continue

# Log 分級計數器
info_count = 0
warning_count = 0
error_count = 0
critical_count = 0 


for log in recent_logs:
    if "INFO" in log:
        info_count += 1

    elif "WARNING" in log:
        warning_count += 1

    elif "ERROR" in log:
        error_count += 1
        
    elif "CRITICAL" in log:
        critical_count += 1
        

print("INFO 數量：", info_count)
print("WARNING 數量：", warning_count)
print("ERROR 數量：", error_count)
print("CRITICAL 數量：", critical_count)



# 判斷 Log 等級

if critical_count > 0:
    print("Log 狀態：嚴重異常")

elif error_count > 0:
    print("Log 狀態：異常")

elif warning_count > 0:
    print("Log 狀態：警告")

else:
    print("Log 狀態：正常")

    
# 計算重大異常總數

abnormal_count = error_count + critical_count    
    
if abnormal_count > 0:
    print(f"\n系統存在 {abnormal_count} 筆重大異常")
    
    # 關鍵字搜尋

    keyword = input("\n請輸入要搜尋的關鍵字(如毋須查詢請輸入：q)：")
    if keyword != 'q' :
        search_count = 0
        
        for log in recent_logs:
            if keyword in log:
                print(log.strip())
                search_count += 1
        
        if search_count == 0:
            print("查無符合的 Log 紀錄")
        else:
            print(f"\n共找到 {search_count} 筆紀錄")
            
    else:
        sys.exit()
else:
    print("系統目前無重大異常")
    
    
