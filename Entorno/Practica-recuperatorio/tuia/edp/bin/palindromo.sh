if [ $(echo $1 | rev) = $1 ]; then
    echo "Es palindromo"
else
    echo "No es palindromo"
fi
