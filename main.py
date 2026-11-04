from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 計算剩餘天數
days_left = (target_date.date() - now.date()).days

# 開啟乾淨底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 使用 Python 內建預設字型，避免任何找不到檔案的錯誤
font = ImageFont.load_default()

text = str(days_left)
img_w, img_h = img.size

# 簡單計算置中與紅框座標
text_w, text_h = 80, 100
x = (img_w - text_w) / 2 - 70
y = 820

# 繪製白色數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果
img.save("output_countdown.jpg")
