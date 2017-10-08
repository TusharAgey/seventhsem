LC_CTYPE=C
x=$(tr -dc A-Za-z < /dev/urandom | fold -w ${1:-$1} | head -n 1)
echo $x > $1'Key'
