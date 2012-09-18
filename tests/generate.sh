#!/bin/sh

COUNT="${1}"

rm test_*.cpp

echo "def build(bld):" > wscript

for ((I=1; I<=${COUNT}; I++)); do
  echo "#include \"test.hpp\"" > test_${I}.cpp
  echo "    bld.program(features='test', source='test_${I}.cpp', target='test_${I}')" >> wscript
done
