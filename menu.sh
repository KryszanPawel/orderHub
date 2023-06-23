#!/bin/bash
((answer = "b"))
while [ $answer != "q" ] && [ $answer != "Q" ]
do
    clear
    echo Order Hub
    echo Choose action:
    echo "(R)ead tables and extract to .xlsx"
    echo "(O)pen table reader log file"
    echo "(Q)uit application"
    echo "----------------------------------"
    read answer
    clear

    case ${answer:0:1} in
        r | R)
            echo "Extraction Starts"
            ./venv/Scripts/python.exe ./tableReader/tableReader.py 
            echo "Extraction Completed!" ;;
        q | Q)
            break;;
        o | O)
            cat tableReader/log/log.txt
            echo "";;
        *)
            echo "CHOOSE AGAIN"
            sleep 1
            continue ;;
    esac

    echo "------------------------------------------"
    echo "Do you want to do anything else (YES/NO)?"
    read doEnd

    case ${doEnd:0:1} in
        n | N)
            break ;;
        *)
            continue;;
    esac
    
done
clear