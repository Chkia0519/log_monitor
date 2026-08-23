import time

#LOG檔名
LOG_FILE = "system.log"

#監測秒數
CHECK_INTERVAL = 3

def read_logs():
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        return file.readlines()

#所有的Log
logs = read_logs()

#已處理的Log數量
processed_count = len(logs)

print("開始監控 system.log...")
try:
    while True:

        try:
            current_logs = read_logs()
            
        except FileNotFoundError:
            print("找不到 system.log，等待 Log 檔案恢復...")
            time.sleep(3)
            continue
        
        if len(current_logs) < processed_count:
            processed_count = 0
    
        if len(current_logs) > processed_count:
            new_logs = current_logs[processed_count:]
    
            for log in new_logs:
                if "CRITICAL" in log:
                    print(f"[嚴重異常] {log.strip()}")
    
                elif "ERROR" in log:
                    print(f"[異常] {log.strip()}")
    
                elif "WARNING" in log:
                    print(f"[警告] {log.strip()}")
    
            processed_count = len(current_logs)
    
        time.sleep(CHECK_INTERVAL)
    
except KeyboardInterrupt:
    print("\n監控已停止")