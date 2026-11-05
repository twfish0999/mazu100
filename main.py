from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 1. 設定目標日期 (2027 年 1 月 22 日)
target_date = datetime(2027, 1, 22)

# 2. 取得台灣時區的當前日期 (確保每天早上自動執行時時間準確)
taipei_tz = pytz.timezone('Asia/Taipei')
now = datetime.now(taipei_tz)
current_date = datetime(
    now.year, now.month, now.day
)  # 取到當天日期（去除時分秒影響）

# 3. 自動計算相差天數
remaining_days = (target_date - current_date).days

# （接下來就是原本繪製圖片與寫入文字的邏輯...）
print(f'距離 2027年1月22日 還剩 {remaining_days} 天')
