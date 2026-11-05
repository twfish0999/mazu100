from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 1. 設定目標日期 (2027 年 1 月 22 日)
target_date = datetime(2027, 1, 22)

# 2. 取得台灣時區的當前日期
taipei_tz = pytz.timezone('Asia/Taipei')
now = datetime.now(taipei_tz)
current_date = datetime(now.year, now.month, now.day)

# 3. 自動計算相差天數
remaining_days = str((target_date - current_date).days)

# 4. 開啟底圖
image_path = 'base.jpg'
img = Image.open(image_path)
draw = ImageDraw.Draw(img)

# 5. 調整文字座標（將數字移到上方紅框內「天」字的左側）
x = 420  # 數值越小越靠左，越大越靠右
y = 650  # 數值越小越靠上，越大越靠下

# 若有字型檔可在此載入：font = ImageFont.truetype("arial.ttf", size=150)
draw.text((x, y), remaining_days, fill=(255, 255, 255))

# 6. 儲存輸出圖片
img.save('output_countdown.jpg')
print(f'成功更新倒數圖片，目前天數：{remaining_days}')
