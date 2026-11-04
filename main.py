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

# 設定字型與大小
try:
  font = ImageFont.truetype("GenWanGothic-M.ttf", 110)
except:
  font = ImageFont.load_default()

text = str(days_left)

# 取得圖片尺寸
img_w, img_h = img.size

# 計算字體寬高
try:
  bbox = draw.textbbox((0, 0), text, font=font)
  text_w = bbox[2] - bbox[0]
  text_h = bbox[3] - bbox[1]
except AttributeError:
  text_w, text_h = draw.textsize(text, font=font)

# 針對紅框位置精準計算：
# 將 X 軸往左微調大約 70 像素（讓「79」可以跟右邊的「天」字完美並排在紅框中央）
x = (img_w - text_w) / 2 - 70
y = 820  # 調整到紅框內的垂直高度

# 繪製白色數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果
img.save("output_countdown.jpg")
