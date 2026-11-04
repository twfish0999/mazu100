from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 計算剩餘天數
days_left = (target_date.date() - now.date()).days
print(f"目前計算剩餘天數: {days_left}")

# 開啟乾淨底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 強制載入字型（使用 Pillow 內建的高解析字型，保證絕不會失敗）
try:
  # 嘗試放大字型，讓數字夠大夠清楚
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

# 座標精準對齊紅框（水平置中再往左微調 70 像素，垂直高度 800）
x = (img_w - text_w) / 2 - 70
y = 800

# 繪製白色粗體數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果並覆蓋檔案
img.save("output_countdown.jpg")
print("數字已成功渲染並寫入 output_countdown.jpg！")
