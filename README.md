# Gain Miles Group 線上測驗

> 此專案是 Gain Miles Group 的線上測驗。

## 功能

**測試帳號密碼**

```
帳號： superadmin
密碼： 1qaz@WSX3edc
```

### 主要功能介紹
* 商品(commodity)：包含基本 crud 功能，用於管理商品，包含可設定各商品之代號、名稱、價錢、庫存以及其的類型、顏色與尺寸。

* 類型(category)：包含基本 crud 功能，用於管理類型資料表。

* 顏色(color)：包含基本 crud 功能，用於管理顏色資料表。

* 尺寸(size)：包含基本 crud 功能，用於管理尺寸資料表。

## 安裝

以下將引導你如何安裝此專案到你的 Linux 主機上。

### 取得專案
```
git clone https://github.com/rivet9658/GainMiles_Online_Test.git
```

### 移動到專案內
```
cd GainMiles_Online_Test
```

### 運行專案
輸入以下指令來運行專案，會自動執行資料遷移並創建一超級使用者，帳密詳情請參考上方測試帳號密碼部分
```
sh deploy.sh
```

### 開啟專案
在瀏覽器網址列輸入以下即可看到 swagger 文檔
```
http://{ip}:8000/swagger/online_test/
```

### 環境變數說明
```env
DB_NAME=gain_miles_online_test_db  # 資料庫名稱
DB_USERNAME=root  # 資料庫登入使用者名稱
DB_PASSWORD=1qaz@WS3edc  # 資料庫登入使用者密碼
DB_HOST=db  # 資料庫 Host
DB_PORT=3306  # 資料庫 Port
WITHOUT_HTTPS_DOMAINS=*  # DOMAIN 設定
DOMAINS=http://0.0.0.0:8000  # DOMAIN 設定
ANONYMOUS_PASSWORD:3edc@WSX1qaz  # django 預設匿名使用者密碼
SUPERADMIN_PASSWORD:1qaz@WSX3edc  # django 預設超級使用者密碼
```

### 專案技術
* Python: 3.7.9
* Django 3.2.20
* MariaDB: 10.11.4

## 聯絡作者
- gmail: bo.chen.lin8831@gmail.com
