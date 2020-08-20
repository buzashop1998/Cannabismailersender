import requests,sys
import time

ok = 0
er = 0

try:

	print "-Cannabis Mail Sender Simple-\n"
	print "Note:Yang bisa dikosongkan cuma Sender Name,Email Priority, Reply-to\n\n"
	Targetssa = raw_input("Input your list : ")
	Targetssax = raw_input("Input your mailer Link : ")
	Targetssaxx = raw_input("Input your  Sender Email : ")
	Targetssaxxx = raw_input("Input your  Sender Name : ")
	Targetssaxxxx = raw_input("Input your  Sender Subject : ")
	Targetssaxxxxx = raw_input("Input your  Reply-to : ")
	print "High :1\nNormal :3\nLow :5\nDefault : (kosong gk ush disi)"
	Targetssaxxxxxxx = raw_input("Input your  Email Priority : ")

	ip_list = open(Targetssa, 'r').read().split('\n')
	for mail in ip_list:
		time.sleep(7)
		datax = {"action":"send", "sendingMethod":"builtin", "senderEmail":Targetssaxx, "senderName":Targetssaxxx, "replyTo":Targetssaxxxxx, "messageSubject":Targetssaxxxx, "messageLetter": open('letter.txt','r').read(), "altMessageLetter":"", "messageType":"html", "encodingType":"UTF-8", "emailPriority":Targetssaxxxxxxx, "recipient":mail, "smtpAcct":""}
		sdk = requests.post(Targetssax,data=datax)
		if "OK" in sdk.text:
			ok = ok + 1
			print "[OK] :"+"   "+mail
			open('send.txt','a').write("[OK] :"+"   "+mail+"\n")
			print "========Waiting For Delay========"
		else:
			er = er + 1
			print "[ER] :"+"   "+mail
			sys.exit()
	print "Done"
	print "OK : "+str(ok)
	print "ER : "+str(er)

except Exception as e:
	print str(e)