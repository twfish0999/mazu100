from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 強制固定顯示為 78 天
days_left = 78
print(f"強制顯示天數: {days_left}")

# 開啟底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 載入字型
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

# 🎯 調整座標：x 軸置中微調，y 軸調大到 830 讓數字往下落
x = (img_w - text_w) / 2 - 90
y = 830

# 繪製白色粗體數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存圖片
img.save("output_countdown.jpg")
print(f"數字 {text} 渲染成功！")
