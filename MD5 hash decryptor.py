# MD5 hash decryptor
import hashlib
print('\t \t \t PASSWORD CRACKER')
pass_found = 0
input_hash = input("Enter The Hashed Password:")
pass_doc = input("\n Enter passwords filename including path(/root/home/):")
# pass_doc="encryptions/rockyou.txt"
try:
    pass_file = open(pass_doc, 'r', errors='ignore')
except:
    print("Error!!!")
    print(pass_doc, "is not found .\n Please give the path of the file correctly ")
    quit()

for word in pass_file:
    enc_word = word.encode('utf-8')
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()
    if digest == input_hash:
        print("Password found.\n The password is:", word)
        pass_found = 1
        break
if not pass_found:
    print("Password was not found in the", pass_doc, "file")
    print("\n")
    print("\t\t\t Thank You")
