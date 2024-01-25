#!/bin/env bash

var1="this is A text9 strin7g with numb3rs in it"
var2="this is A text string without numbers in it"
var3="NoNumbersNoSpaces"
regex="^[A-Za-z]+$"

if [[ $var1 =~ $regex ]]
then
  echo $var1
fi
if [[ $var2 =~ $regex ]]
then
   echo $var2
fi
if [[ $var3 =~ $regex ]]
then
   echo $var3
fi

exit 0
