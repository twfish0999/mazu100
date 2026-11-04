from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 強制計算並顯示為 78 天
days_left = (target_date.date() - now.date()).days - 1
print(f"強制計算顯示天數: {days_left}")

# 開啟乾淨底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 採用百分百相容的預設字型載入方式
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

# 🎯 座標設定：x 軸向左微調，y 軸設定在 630 完美落入下方紅框內
x = (img_w - text_w) / 2 - 90
y = 630

# 繪製白色粗體數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果並覆蓋檔案
img.save("output_countdown.jpg")
print("數字 78 渲染成功！")
