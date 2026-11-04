from datetime import datetime, timezone, timedelta
from PIL import Image, ImageDraw, ImageFont

# 1. 設定台灣時區 (UTC+8) 計算精準剩餘天數
tz_tw = timezone(timedelta(hours=8))
today = datetime.now(tz_tw).date()
target_date = datetime(2027, 1, 22).date()
remaining_days = (target_date - today).days

# 2. 開啟剛才上傳的乾淨底圖
base_image_path = "base.jpg"
img = Image.open(base_image_path)
draw = ImageDraw.Draw(img)

# 3. 設定字型與載入
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
except:
    font = ImageFont.load_default()

# 4. 在紅色方塊的「天」字左側繪製動態天數數字
text = str(remaining_days)
# 註解：(360, 245) 為數字繪製座標，若執行後位置需微調可隨時修改此處數字
draw.text((360, 245), text, fill="white", font=font)

# 5. 儲存產出最終圖片
img.save("output_countdown.jpg")
print(f"成功更新！台灣時間今日：{today}，倒數天數：{remaining_days} 天")
