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

# 3. 計算剩餘天數並扣 1 天（確保今天精準顯示 77 天）
remaining_days = str((target_date - current_date).days - 1)

# 4. 開啟底圖
image_path = 'base.jpg'
img = Image.open(image_path)
width, height = img.size
draw = ImageDraw.Draw(img)

# 5. 自動尋找伺服器內建字型，並設定大小 (size=90)
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

# 6. 【微調對齊紅框左側】將方框範圍稍微向右下方微調 (x軸向右、y軸向下)
box_x1, box_y1, box_x2, box_y2 = 350, 370, 530, 520

# 取得數字的寬高 bbox
bbox = font.getbbox(remaining_days)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# 自動計算數字在紅框左側區域內的置中座標
x = box_x1 + ((box_x2 - box_x1 - text_width) / 2)
y = box_y1 + ((box_y2 - box_y1 - text_height) / 2)

# 7. 僅繪製數字「77」
draw.text((x, y), remaining_days, fill=(255, 255, 255), font=font)

# 8. 儲存輸出圖片
img.save('output_countdown.jpg')
print(f'成功更新倒數數字，目前天數：{remaining_days}')
