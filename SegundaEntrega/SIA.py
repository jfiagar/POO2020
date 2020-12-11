import basededatosMATERIAS as BDM        #Importa el Modulo de la Base de Materias actual y lo importa con la abreviacion BDM
import BDMateriasAntigua as BDMA        #Importa el Modulo de la Base de materias Antiguas y lo importa con la abreviacion BDMA
import inscripcion as INS           #Importa el Modulo de Inscripcion y lo importa con la abreviacion INS
import BDEstudiantes as BDE         #Importa el Modulo de la Base de Estudiantes y lo importa con la abreviacion BDE
import BaseDocentes as BDD          #Importa el Modulo de la Base de Docentes y lo importa con la abreviacion BDD
import os               #El módulo "os" nos permite acceder a funcionalidades dependientes del Sistema Operativo. en este caso lo usamos para limpiar la consola
import os.path          # submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios



def menu_principalSIA():            #Función del menú principal del SIA
    borrarPantalla()        # Borra los valores de la consola de windows, limpia la consola
    print("\n\n------------------Bienvenido al SIA---------------------")       # Saludo :v
    print("MENÚ PRINCIPAL")             # Imprime Menú principal
    print("\t[0]  Entrar a la base de datos de materias Actual")            # Imprime en pantalla el texto de la opción "0"
    print("\t[1]  Entrar a la base de datos de materias Antigua")           # Imprime en pantalla el texto de la opción "1"
    print("\t[2]  Entrar a la base de datos de Estudiantes")            # Imprime en pantalla el texto de la opción "2"
    print("\t[3]  Entrar a la base de datos de Docentes")           # Imprime en pantalla el texto de la opción "3"
    print("\t[4]  Inscribir materias")              # Imprime en pantalla el texto de la opción "4"
    print("\t[5]  Salir del programa")              # Imprime en pantalla el texto de la opción "5"

def borrarPantalla():                       #Definimos la función estableciendo el nombre de Borrar Pantalla
    if os.name == "posix":              #Verifica si el sistema operativo es Unix/Linux/MacOS/BSD
        os.system ("clear")             #Si el sistema es Unix/Linux/MacOS/BSD limpia la consola con la función system clear
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":        #Verifica si el sistema operativo es Windows, o sistemas desarrollados por Microsoft
        os.system ("cls")                       #Si el sistema es DOS/Windows limpia la consola con la función system cls



borrarPantalla()    #Inicia borrando la pantalla
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("""
        &&&&&&&&&&&&&&&&,          &&&&&           &&&&#     &&&&/    %%%%*           %%%%     %%%%%%%%%%%%%%%      %%%%%%%%%%%%%%,                %%%%%                  
        &&&&&&&&&&&&&&&&&&&&       &&&&&&/         &&&&(     &&&&/    %%%%%%          %%%%     %%%%%%%%%%%%%%%   %%%%%%%%    .%%%%%%%*            %%%%%%%                 
        &&&&            &&&&&*     &&&&&&&&        &&&&#     &&&&/    %%%%%%%%        %%%%     %%%%            #%%%%%             %%%%%          %%%%%%%%#                
        &&&&              &&&&/    &&&&,&&&&&      &&&&(     &&&&/    %%%%(%%%%#      %%%%     %%%%           ,****                 %%%%,       %%%%  %%%%.               
        &&&&               &&&&    &&&&, %&&&&%    &&&&#     &&&&/    %%%%, #%%%%.    %%%%     %%%%%%%%%%%%%%%%%%%%%%%%%%%           %%%%      %%%%    %%%%,              
        &&&&               &&&&    &&&&,   &&&&&.  &&&&(     &&&&/    %%%%,   %%%%%   %%%%     %%%%%%%%%%%%%%%%%%%%%%%%%%%           %%%%     %%%%      %%%%*             
        &&&&              #&&&&    &&&&,     &&&&& &&&&#     &&&&/    %%%%,     %%%%% %%%%     %%%%                                 (%%%%    %%%%        %%%%*            
        &&&&             %&&&&     &&&&,      /&&&&&&&&(     &&&&/    %%%%,      *%%%%%%%%     %%%%            %%%%#               %%%%%    %%%%,         %%%%,           
        &&&&          ,&&&&&&      &&&&,        %&&&&&&#     &&&&/    %%%%,        %%%%%%%     %%%%             %%%%%%.         .%%%%%#    %%%%,           %%%%.          
        &&&&&&&&&&&&&&&&&&&        &&&&,          &&&&&(     &&&&/    %%%%,          %%%%%     %%%%               %%%%%%%%%%%%%%%%%%,     %%%%.             %%%%(         
        &&&&&&&&&&&&&&.            &&&&,           .&&&#     &&&&/    %%%%,           .%%%     %%%%                   #%%%%%%%%%.        %%%%,               %%%%/
""")
print("---------------------------------------------------------- Dirección Nacional de Información Academica ---------------------------------------------------------------\n\n")
input("Presione la Tecla ENTER para continuar...") # Imprime el Logo de DNINFOA y luego pide un imput cualquiera para continuar


while True:                         #Ciclo while  siempre activo para garantizar que el programa no se cierra y vuelva al menú principal siempre
    menu_principalSIA()                 #Imprime la función Menu Principal
    opcion_elegida = input("Ingrese el número de la opción: ")              #Almacena el texto ingresado por el usuario
    if opcion_elegida == "0":          # Entra si la opción elegida en base al menuprincipalSIA es 0
        BDM.mainBDM()                   # Ejecuta la función MAIN (CÓDIGO PRINCIPAL) del modulo Base de datos de Materias
    elif opcion_elegida == "1":        # Entra si la opción elegida en base al menuprincipalSIA es 1
        BDMA.mainBDMAntigua()           # Ejecuta la función MAIN (CÓDIGO PRINCIPAL) del modulo Base de datos de Materias Antigua
    elif opcion_elegida=="2":          # Entra si la opción elegida en base al menuprincipalSIA es 2
        BDE.mainBDE()                   # Ejecuta la función MAIN (CÓDIGO PRINCIPAL) del modulo Base de datos de Estudiantes
    elif opcion_elegida == "3":        # Entra si la opción elegida en base al menuprincipalSIA es 3
        BDD.baseDocentes()               # Ejecuta la función MAIN (CÓDIGO PRINCIPAL) del modulo Base de datos de Docentes
    elif opcion_elegida == "4":        # Entra si la opción elegida en base al menuprincipalSIA es 4
        INS.main_inscripciones()          # Ejecuta la función MAIN (CÓDIGO PRINCIPAL) del modulo Inscripción
    elif opcion_elegida == "5":        # Entra si la opción elegida en base al menuprincipalSIA es 5
        print("\n\t Saliendo...")           #Imprime Saliendo- luego rompe el ciclo con Break
        break
    else:
        print("Opción no valida")        # Imprime opción no valida y continua el ciclo , vuelve a imprimir el menu principal