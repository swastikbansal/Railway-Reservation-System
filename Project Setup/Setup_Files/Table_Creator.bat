@echo off
echo --------Creating Tables----------

set /p password= Enter your Password (mysql login) : 

mysql -uroot -p%password% < "Setup_Files\Create tables\Script\Local Machine.sql"
echo Your Tables have been Created Successfully!!
PAUSE