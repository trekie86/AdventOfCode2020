if [ -z "$1" ]
  then
    echo "No argument supplied"
fi

figlet Advent Of Code Day $1

mkdir day$1
touch day$1/__init__.py
touch day$1/part_1.py
touch day$1/part_2.py
touch day$1/sample.txt
touch day$1/input.txt

echo '"""Advent of Code 2020 day '$1' part 1"""' > day$1/part_1.py
echo '"""Advent of Code 2020 day '$1' part 2"""' > day$1/part_2.py
