# A. 資料庫
1. 請說明SQL與No-SQL的差異，並說明兩者的運用場景
SQL是一種用於關聯式資料庫的語言，可以用來管理關聯式資料庫。相反的No-SQL就是非關聯式資料庫。關聯式資料庫必須經過正規化，但是經過正規化就會產生較多的資料表，且擴展性較差。非關聯式資料庫的設計可以比較靈活，在一筆資料中可以相容更多元的情況，且對於使用JSON傳輸的情況下No-SQL在格式上具有較大的優勢，可以避免SQL需要JOIN多個資料表的情況，在資料量龐大的情況下No-SQL也比較有效率。
SQL所適合的場景為: 穩定、資料之間有一致性或關聯性、資料較不會變化、規模較小、資料之間的關係較單純。
No-SQ更適合: 龐大的資料量、需要進行調整、資料間有複雜的關係。
2. 請說明何謂資料庫正規化]
   正規化可以將資料中的資料整理成一致性的一套標準，通常我們會做到第三正規化。  
   * 第一正規化 1NF:  
     除重複的資料，一個欄位只能有一個值，新增主鍵並且讓所有欄位都相依於此。  
   * 第二正規化 2NF:  
     解決部分相依的問題，將部分相依的內容獨立成一個資料表。  
   * 第三正規化 3NF:  
     將遞移相依的內容獨立，遞移相依就表示部分欄位並不存在跟主鍵直接的關係，反而是跟其他的鍵值或欄位有相依。  

# B. Django
1. 使用virtualenv
2. Python版本3.8.10
3. 需安裝的module在requirements.txt中

## a. 登入登出
1. 建立一組帳號密碼  
   Username: admin  
   Password: admin  
2. startapp 建立login的app，裡面有登入和登出的功能

## b. 操作頁面
1. startapp 建立 show，主要處理跟題目有關的功能
2. 將上一題做好得資料庫inspectdb將資料匯入model
3. 在app show裡面建立show template可以用來操作功能
4. 點選選單裡的UID或是在文字方塊中輸入UID可以進行操作
5. 新增search template顯示查詢結果
6. 新增edit template修改資料
7. 資料刪除
   * DELETE /operation/delete 可以刪除資料  
     在body中以JSON 傳入 uid
8. 資料查詢
   * GET /operation/search  
     在params傳入uid會得到搜尋結果的頁面
9. 資料修改
   * GET /operation/editPage 會回傳編輯頁面  
   * POST /operation/editShow 可以編輯show的資料  
     以JSON傳入 uid, title, categroyID, showUnit, descriptioFilterHtml, discountInfo, imageUrl, webSales, sourceWebPromote, comment, sourceWebID, startDate, endDate  
     Response 會有 msg告知是否完成修改
   * POST /operation/editMaster 可以更新主辦單位的資料  
     傳入 masterUnitID, unitName Response一樣會有msg
   * POST /operation/editSub, POST /operation/editSupport, POST /operation/editOther，分別可以修改協辦單位 、贊助單位、其他單位
10. 在路徑 / 會接轉跳到登入頁面
11. 若要在還沒登入時查詢，可以直接前往/operation/show/
12. 未登入時只有「資料查詢」的按鈕，即使透過API也無法操作其他功能
## c.自動更新
1. mongoDB在伺服器的port 27017
2. 透過 GET /update 抓取政府資料開放平台的資料: 「各縣(市)領有各級漁船幹部船員執業證書人數」
3. https://data.gov.tw/dataset/41392
4. 在專案中有一個.sh 檔(在django_prj資料夾中)，透過crontab 設定每天1:00執行shellscript，這個shellscript會觸發 /update

# C. 伺服器部屬
使用GCP，ssh資訊在資料夾內(未上傳github)
SSH Key: ssh-key-gcp