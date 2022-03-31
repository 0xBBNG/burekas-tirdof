### search DB ###

#SQL
sqldump1 = 'intitle%3A"index+of"+"dump.sql"+in+url%3A'
sqldump2 = 'filetype%3Asql+intext%3A+"sql+dump'
sqldump3 = 'inurl%3Awp-content%2Fuploads%2Fdump.sql'
test_search = 'test_search'

sql_searches = [
    sqldump1,
    sqldump2,
    sqldump3,
    # test_search,
]

#Passwords
domain = ""
password_search = "site:{} 'password' filetype:doc | filetype:pdf | filetype:docx | filetype:xls | filetype:dat | filetype:log"
passwd_searches = [
    password_search
]

#Buckets
domain = ""
bucket = 'site:.s3.amazonaws.com ' + domain
bucket_searches = [
    bucket,
]

