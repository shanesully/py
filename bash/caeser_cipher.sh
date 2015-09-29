#!/bin/bash
# shanesully 
#
# Caeser Cipher Encryption Script
#   

function print_usage {
    # Print commandline usage info
    printf "\nProgram: \n\t$0\n"
    printf "\nUsage:\n"
    printf "\t$ $0 $args\n"
    printf "\nNotes:\n"
    printf "\t- Run with or without arguments\n"
    printf "\t- Run without arguments for usage info\n"
    printf "\n"
}

function caeser_encrypt {
    # Encrypt using Caeser Cipher 
    local ciphertext=`echo $1 | tr 'A-Za-z' 'X-ZA-Wx-za-w'`
    printf $ciphertext
}

function caeser_decrypt {
    # Reverse Caeser Cipher
    local plaintext=`echo $1 | tr 'X-ZA-Wx-za-w' 'A-Za-z'`
    printf $plaintext
}

function display_output {
    # Pretty-print cipher process
    printf "Original Message:\n$1\n"
    printf "Encrypted Message:\n$2\n"
    printf "Decrypted Message:\n$3\n"
    printf "\n"
}

function run_cipher_process {
    # Process messages
    # Original message
    original_msg=$1
    # Encrypt message
    ciphertext=$(caeser_encrypt $original_msg)
    # Decrypt Message
    plaintext=$(caeser_decrypt $ciphertext)

    # Display content
    display_output $original_msg $ciphertext $plaintext
}

function get_new_msg {
    # Get message from user
    echo "Enter message or (q)uit?"
    read anwser

    if [ $anwser = "q" ]; then
        exit
    else
        printf ""
        # Run cipher process on message 
        run_cipher_process $anwser 
    fi
}

# If no args passed
if [ $# -eq 0 ]; then
    # Print program usage for future sessions
    print_usage
fi

# Encrypt messages from commandline
for a in ${BASH_ARGV[*]}; do
    run_cipher_process $a
done

# Encrypt message from user until
# they choose to quit
while :
do
    get_new_msg 
done
