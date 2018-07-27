python -B spiderAppartment.py | grep 'typeid=89' | awk '{$1=$2="";print $0}' > rental.html
grep -i 'sage' rental.html > result.html
python -B sendlink.py
