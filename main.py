from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 計算剩餘天數（目前為正確的 79 天）
days_left = (target_date.date() - now.date()).days
print(f"目前計算剩餘天數: {days_left}")

# 開啟乾淨底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 強制載入字型並放大
try:
  font = ImageFont.load_default(size=120)
except Exception:
  try:
    font = ImageFont.truetype("DejaVuSans-Bold.ttf", 120)
  except Exception:
    font = ImageFont.load_default()

text = str(days_left)
img_w, img_h = img.size

# 計算字體寬高
try:
  bbox = draw.textbbox((0, 0), text, font=font)
  text_w = bbox[2] - bbox[0]
  text_h = bbox[3] - bbox[1]
except Exception:
  text_w, text_h = 70, 90

# 微調 x 軸與 y 軸，讓「79」完美置中於上方紅框內
x = (img_w - text_w) / 2 - 10
y = 135

# 繪製白色粗體數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果並覆蓋檔案
img.save("output_countdown.jpg")
print("數字 79 已完美置中渲染！")
