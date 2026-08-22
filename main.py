import logging

logging.basicConfig(
    filename="sys1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info("系統啟動")
logging.info("使用者登入成功")
logging.warning("API 回應速度過慢")
logging.error("資料庫連線失敗")
logging.critical("系統無法打開")

print("Log 建立完成")
