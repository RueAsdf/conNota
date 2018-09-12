#!/bin/bash

PS3='Por favor ingrese una opcion: '

options=("1-Apagar" "2-Reiniciar" "3-Ver informacion del SO" "4-Ver informacion del kernel" "5-Ver autor" "6-Ejecutar proyecto1" "7-Salir" )

select opt in "${options[@]}"

do
    case $opt in

        "1-Apagar")
            sudo poweroff
            ;;

        "2-Reiniciar")
            sudo reboot
            ;;

        "3-Ver informacion del SO")
            sudo uname -o
            ;;

        "4-Ver informacion del kernel")
            sudo uname
            ;;

        "5-Ver autor")
            echo "Diego Jorquera"
	    echo "24 años"
	    echo "Vive en Rancagua"
	    echo "Estudia en santo tomas"
            ;;

        "6-Ejecutar proyecto1")
            cd ..
	    cd proyecto_1
	    python3 Calculadora.py
            ;;

        "7-Salir")
            break
            ;;

        "Quit")
            break
            ;;

        *) echo "opcion incorrecta $REPLY";;
    esac
done
