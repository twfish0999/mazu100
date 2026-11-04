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

# 嘗試載入字型，若無則使用預設並放大
try:
  font = ImageFont.truetype("GenWanGothic-M.ttf", 110)
except Exception:
  try:
    # 嘗試尋找系統常見的中文字型
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 110
    )
  except Exception:
    font = ImageFont.load_default()

text = str(days_left)
img_w, img_h = img.size

# 計算字體大小
try:
  bbox = draw.textbbox((0, 0), text, font=font)
  text_w = bbox[2] - bbox[0]
  text_h = bbox[3] - bbox[1]
except Exception:
  text_w, text_h = 60, 90

# 精準對齊紅框中央（水平置中再往左微調 70 像素，垂直高度 820）
x = (img_w - text_w) / 2 - 70
y = 820

# 繪製白色數字（加上明顯的白色確保不透明）
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果
img.save("output_countdown.jpg")
print("圖片產出並強制渲染數字成功！")
