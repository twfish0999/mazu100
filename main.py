from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

# 1. 設定目標日期 (2027 年 1 月 22 日)
target_date = datetime(2027, 1, 22)

# 2. 取得台灣時區的當前日期
taipei_tz = pytz.timezone('Asia/Taipei')
now = datetime.now(taipei_tz)
current_date = datetime(now.year, now.month, now.day)

# 3. 自動計算相差天數（今天是 77 天，明天會自動變成 76 天...以此類推）
remaining_days = str((target_date - current_date).days)

# 4. 開啟底圖
image_path = 'base.jpg'
img = Image.open(image_path)
draw = ImageDraw.Draw(img)

# 5. 設定字型與座標位置（若有需要微調 x 或 y 數字可以修改這裡）
# 如果您有上傳自訂字型檔可以寫入路徑，若無可使用預設
# font = ImageFont.truetype("arial.ttf", size=150)

x = 500  # 左右位置調整
y = 830  # 上下位置調整

# 6. 繪製倒數數字
draw.text((x, y), remaining_days, fill=(255, 255, 255))

# 7. 儲存輸出圖片
img.save('output_countdown.jpg')
print(f'成功更新倒數圖片，目前距離 2027年1月22日 還剩 {remaining_days} 天')
