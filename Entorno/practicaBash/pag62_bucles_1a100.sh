#!/bin/env bash

echo "Con un bucle for"
for i in $(seq 1 100);
do
  echo "Cuento $i"
done

echo "Con un bucle while"
i=0
while [ $i -le 100 ]
do
  echo "Cuento $i"
  i=$((i+1))
done

exit 0
