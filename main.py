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

# 嘗試載入字型，若失敗則使用 Pillow 預設字型
try:
  font = ImageFont.truetype("GenWanGothic-M.ttf", 110)
except Exception:
  font = ImageFont.load_default()

text = str(days_left)
img_w, img_h = img.size

# 計算字體寬高（相容各種版本）
try:
  bbox = draw.textbbox((0, 0), text, font=font)
  text_w = bbox[2] - bbox[0]
  text_h = bbox[3] - bbox[1]
except Exception:
  text_w, text_h = 80, 100

# 設定紅框內的精確座標（水平置中再往左微調 70 像素，垂直高度 820）
x = (img_w - text_w) / 2 - 70
y = 820

# 繪製白色數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果
img.save("output_countdown.jpg")
