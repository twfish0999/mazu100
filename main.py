from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 計算剩餘天數（精確計算至 79 天或當前天數差）
days_left = (target_date.date() - now.date()).days

# 開啟乾淨底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 設定字型與大小
try:
  font = ImageFont.truetype("GenWanGothic-M.ttf", 120)
except:
  font = ImageFont.load_default()

text = str(days_left)

# 取得圖片尺寸以計算精確置中座標
img_w, img_h = img.size

# 計算字體寬高
bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# 計算水平置中 X 座標，以及對應紅色方框的垂直 Y 座標
x = (img_w - text_w) / 2
y = 1100  # 若數字位置需要上下微調，可直接修改此數值

# 繪製白色數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果
img.save("output_countdown.jpg")
