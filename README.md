# health_care_sensor
 
> 使用bluetoothctl取得醫療感測器數據

## ENV
### Device
1. Raspberry pi 3b+(可替換具備藍芽功能的SBC)

### App dependences
1. Python3.6
2. Flask 2

## 可能遭遇問題
> 在執行flask時subprocess回傳的字元長度不相同，如果想要單個檔案進行個別測試，需要將raw data print出來再調整擷取位置。
