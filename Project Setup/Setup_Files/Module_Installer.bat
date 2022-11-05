@echo off
cd Setup_Files\Modules
echo Installing mysql-connector-python
cd mysql_connector
pip install mysql_connector_python-8.0.28-cp310-cp310-win_amd64.whl
cd ..

echo Installing tkcalendar
cd tkcalendar
pip install tkcalendar-1.6.1-py3-none-any.whl

PAUSE