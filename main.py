from datetime import datetime
import os
import pytz
from PIL import Image, ImageDraw, ImageFont

# 1. 設定目標日期 (2027 年 1 月 22 日)
target_date = datetime(2027, 1, 22)

# 2. 取得台灣時區的當前日期
taipei_tz = pytz.timezone('Asia/Taipei')
now = datetime.now(taipei_tz)
current_date = datetime(now.year, now.month, now.day)

# 3. 自動計算相差天數（今天是 78 天）
remaining_days = str((target_date - current_date).days)

# 4. 開啟底圖
image_path = 'base.jpg'
img = Image.open(image_path)
draw = ImageDraw.Draw(img)

# 5. 自動尋找伺服器內建字型，並設定適合紅框的大小 (size=90)
font_paths = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    'arial.ttf',
]
font = None
for path in font_paths:
  if os.path.exists(path):
    try:
      font = ImageFont.truetype(path, size=90)
      break
    except:
      continue

if font is None:
  font = ImageFont.load_default()

# 6. 調整座標，將數字精準移到紅框內「天」字的左側
x = 440  # 左右位置（數字越大越靠右）
y = 490  # 上下位置（數字越小越靠上，拉進紅框內）

# 7. 繪製白色數字
draw.text((x, y), remaining_days, fill=(255, 255, 255), font=font)

# 8. 儲存輸出圖片
img.save('output_countdown.jpg')
print(f'成功更新倒數圖片，目前天數：{remaining_days}')
