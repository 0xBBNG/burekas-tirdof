### SQL ###
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

### Passwords ###
domain = ""
password_search1 = "site:{} 'password' filetype:doc | filetype:pdf | filetype:docx | filetype:xls | filetype:dat | filetype:log"
password_search2 = 'intitle:Index.of etc shadow'
password_search3 = 'site:*/etc/passwd inurl"/etc/passwd"'
password_search4 = 'ext:xls intext:/etc/passwd | inurl:password'
passwd_searches = [
    password_search1,
    password_search2,
    password_search3,
    password_search4,
]

### Buckets ###
domain = ""
bucket = 'site:.s3.amazonaws.com ' + domain
bucket_searches = [
    bucket,
]

### Robots.txt ###
robots1 = 'inurl: /wp-content/uploads/ inurl:"robots.txt" "Disallow:" filetype:txt'
robots2 = 'inurl:robots.txt + intext:password'
robots_searches = [
    robots1,
    robots2,
]

### Admin ###
admin1 = '	inurl:adminpanel'
admin2 = 'intitle:"index of" *.csv'
admin3 = 'inurl:wp-admin'
admin4 = 'inurl:/admin/login'
admin5 = 'intext:"index of/" "top secret"'
admin6 = 'intitle:"index of" "passwords"'
admin_searches = [
    admin1,
    admin2,
]