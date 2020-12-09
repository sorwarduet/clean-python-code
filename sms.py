
import urllib3

def sent_sms(contact, msg):
    http = urllib3.PoolManager()
    r = http.request('GET','http://isms.zaman-it.com/smsapi?api_key=C20000985e667bc09605a1.17321561&type=text&contacts='+contact+'&senderid=8809612451697&msg='+msg)
    print(r.status)
    print(r.data)
    print(r.headers)
    if r.status == 200:
        print('Successfully Sent')
    else:
        print('Succesfully did not sent')



def sms_sent(contact, msg):
    http = urllib3.PoolManager()
    end_point ='http://www.duet.ac.bd/sms/index.php'
    token = 'HCH3SU5F7DH7F9I4WO4I3FHN7E9G'
    data ={
        'token' : token,
        'number': contact,
        'message' : msg
    }
    r= http.request('POST',end_point, fields=data)
    print(r.status)






name ='Sorwar'
id= '3'
contact ='01621757014'
message = f'Dear {name} \n We are very sorry to inform you that your requisition{id} has been canceled. For further information contact transport section.'

sms_sent(contact,message)

        #sms = SmsSystem()
#sent_sms(contact,message)

url ='http://www.duet.ac.bd/sms/index.php'
token = 'HCH3SU5F7DH7F9I4WO4I3FHN7E9G'
data ={
        'token' : token,
        'number': contact,
        'message' : msg
    }
resp = requests.post(url,json=data, verify=False,)
