import requests

def send_sms(number, message):
    url = "http://www.duet.ac.bd/sms/index.php"
    data = {"token": "HCH3SU5F7DH7F9I4WO4I3FHN7E9G",
            "number": number,
            "message": message
            }
    response = requests.post(url, data=data, verify=False)
    if response.status_code == 200:
        print("Sent Successfully")
    else:
        print("Sent Failed")
    

name ='Sorwar'
number = '8801621757014'
print(number)
message = f'Dear {name} \n We are very sorry to inform you that your requisition has been canceled. For further information contact transport section.'

send_sms(number,message)