#!/bin/bash

function check_arguments {
    if [ $# -ne 2 ]; then
        echo "Error: Debe introducir dos argumentos."
        exit 1
    fi

    # Check if the first argument is a string
    if [[ ! "$1" =~ ^[a-zA-Z]+$ ]]; then
        echo "Error: El primer argumento debe ser un string."
        exit 1
    fi

    # Check if the second argument is a string
    if [[ ! "$2" =~ ^[a-zA-Z]+$ ]]; then
        echo "Error: El segundo argumento debe ser un string."
        exit 1
    fi
}

function check_multiples {
    check_arguments "$1" "$2"

    # Calculate the lengths of the arguments
    length1=${#1}
    length2=${#2}

    # Check if the length of the first argument is a multiple of the length of the second argument
    if [ "$((length1 % length2))" -eq 0 ]; then
        echo "El primer argumento es múltiplo del segundo."
    else
        echo "El primer argumento no es múltiplo del segundo."
    fi
}

check_multiples "$1" "$2"
