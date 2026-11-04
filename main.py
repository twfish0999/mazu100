from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# 1. 計算距離 2027年1月22日 剩餘天數
target_date = datetime(2027, 1, 22)
today = datetime.now()
remaining_days = (target_date - today).days

# 2. 開啟剛剛上傳的底圖
base_image_path = "base.jpg"
img = Image.open(base_image_path)
draw = ImageDraw.Draw(img)

# 3. 設定字型與繪製天數
try:
  font = ImageFont.truetype(
      "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90
  )
except:
  font = ImageFont.load_default()

text = f"{remaining_days}"

# 4. 繪製天數於指定位置 (x, y)
draw.text((360, 230), text, fill=(255, 255, 255), font=font)

# 5. 輸出結果圖
output_path = "output_countdown.jpg"
img.save(output_path)
print(f"今日倒數完成，剩餘：{remaining_days} 天")
