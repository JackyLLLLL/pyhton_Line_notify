import requests


message = "Error，引用模組未成功"

def line_notify(message):

    

    token = "GUELsALl3sUxhv2TqBy3phEsiNKISKTyhGoURIKIdWo"
    #message = "Hello! 這是測試文字!"
    
    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    resp=requests.post(url=line_url, headers=line_header, data=line_data)

    if resp.status_code == 200:
        print("訊息傳送成功")
    else:
        print("訊息傳送失敗")


if __name__ == '__main__':
    line_notify("\n"+message)
 
