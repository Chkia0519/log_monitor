import logging


logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info("使用者登入成功")
logging.warning("API 回應速度過慢")
logging.error("資料庫連線失敗")
logging.critical("核心服務停止")

print("Log 建立完成")

logging.shutdown() #把 logging 使用中的檔案處理器關閉，釋放 Log 檔案。