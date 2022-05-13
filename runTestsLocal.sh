coverage run --omit */*test_*,*myoswrap.py,*customExceptions.py,*__init__.py,/usr/*,/home/lubuntu/.local/* -m unittest discover -s ./project -v
bash ./deployLocal.sh
sleep 15
python3 -m unittest discover -s project/ -p dtest_*.py -v