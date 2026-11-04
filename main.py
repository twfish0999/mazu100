from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 設定目標日期（2027年1月22日）
target_date = datetime(2027, 1, 22, 0, 0, 0)
tz = pytz.timezone("Asia/Taipei")
now = datetime.now(tz)

# 計算剩餘天數
delta = target_date - now.date() - datetime.now(tz).date() + datetime.now(tz).date()  # 確保只算日期差
# 簡單精確計算天數差
days_left = (target_date.date() - now.date()).days

# 開啟底圖
img = Image.open("base.jpg")
draw = ImageDraw.Draw(img)

# 設定字型與大小（請確保環境有支援的字型，或使用預設字型）
try:
  font = ImageFont.truetype(
      "GenWanGothic-M.ttf", 120
  )  # 依您專案中的字型調整
except:
  font = ImageFont.load_default()

text = str(days_left)

# 取得圖片尺寸以計算置中座標
img_w, img_h = img.size

# 計算文字寬高來達到置中效果（您可以手動微調 offsets）
# 這裡假設紅框大約在圖片中央偏下方，我們用 textbbox 來精準計算置中
bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# 調整這裡的 X 軸與 Y 軸座標讓數字完美落在紅框中央
# 假設紅框中心點大約在水平正中央，您可以透過調整減去的數值來微調左右
x = (img_w - text_w) / 2 - 10  # 稍微往左或往右微調
y = 1120  # 依您的紅框高度垂直位置調整

# 繪製白色數字
draw.text((x, y), text, fill=(255, 255, 255), font=font)

# 儲存結果
img.save("output_countdown.jpg")
