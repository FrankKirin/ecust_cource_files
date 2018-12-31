import hashlib
import secrets

word = "apple"
baidu_app_id = "20181231000253646"
baidu_translate_key = "74NojDxYw72wEv6KvuDo"
salt = "1435660289"

#def generate_salt():
	#salt = secrets.token_bytes(16)
	#return salt

def generate_md5():
	#salt = generate_salt()
	print("salt is " + salt)
	req_content = baidu_app_id+word+salt+baidu_translate_key
	md5_code = hashlib.md5(req_content.encode('utf-8')).hexdigest()
	return md5_code

if __name__ == '__main__':
	code = generate_md5()
	print(code)

