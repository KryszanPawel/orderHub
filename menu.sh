#!/bin/bash
unameOut="$(uname -s)"
echo $unameOut
case ${unameOut:0:1} in
    L | l)
        source /venv/bin/activate;;
    M | m)
        source /venv/Scripts/activate;;
    *)
        echo "System not recognized"
        sleep 2
        exit 404;;
esac

((answer = "b"))
while [ $answer != "q" ] && [ $answer != "Q" ]
do
    clear
    echo Order Hub
    echo Choose action:
    echo "(R)ead tables and extract to .xlsx"
    echo "(O)pen table reader log file"
    echo "(S)ort files by order and thickness"
    echo "(Q)uit application"
    echo "----------------------------------"
    read answer
    clear

    case ${answer:0:1} in
        r | R)
            echo "Extraction Starts"
            python3 ./tableReader/tableReader.py 
            echo "Extraction Completed!" ;;
        q | Q)
            break;;
        o | O)
            cat tableReader/log/log.txt
            echo "";;
        s | S)
            echo "Sorting"
            python3 ./fileSorter/fileSorter.py
            echo "Sorted!" ;;
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
