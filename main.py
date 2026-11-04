from datetime import datetime
import pytz
from PIL import Image, ImageDraw, ImageFont

try:
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

  # 設定字型與大小（若找不到字型檔則自動切換為預設字型，絕不報錯）
  try:
    font = ImageFont.truetype("GenWanGothic-M.ttf", 110)
  except Exception as e:
    print(f"載入自訂字型失敗，改用預設字型: {e}")
    font = ImageFont.load_default()

  text = str(days_left)
  img_w, img_h = img.size

  # 計算字體寬高（相容所有 Pillow 版本）
  try:
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
  except Exception:
    try:
      text_w, text_h = draw.textsize(text, font=font)
    except Exception:
      text_w, text_h = 80, 100  # 預設保守寬高

  # 計算紅框內的精確座標（水平置中再往左微調 70 像素，垂直高度 820）
  x = (img_w - text_w) / 2 - 70
  y = 820

  # 繪製白色數字
  draw.text((x, y), text, fill=(255, 255, 255), font=font)

  # 儲存結果
  img.save("output_countdown.jpg")
  print("倒數圖片產出成功！")

except Exception as e:
  print(f"程式執行發生錯誤: {e}")
  raise e
