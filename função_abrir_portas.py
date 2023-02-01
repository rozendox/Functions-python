def porta():
    """
    codigo da porta dianteira esquerda ou direita
    dianteira ou traseira
    """

    senha_usuario = 123

    senha1 = int(input("informe a senha"))

    """
    A variável só será liberada no caso do valor da variavel senha_usuario
    for a mesmo valor da senha1 que será obtida pelo usuário 
    
    """

    fechamento = """Fechando porta...
                    -----------------
                    Porta fechada...
                    -----------------
                    Sensor de travas acionado
                    ------------------
                    Travas acionadas, Operação finalizada..."""

    abertura_um = """Abrindo Porta...
    ----------------\n
    Porta Aberta...
    ----------------\n
    -Angulação limte de 80º alcançada-
    -Operação abertura de portas bem sucessida-"""

    abertura_dois = """Abrindo Porta...
    ----------------\n
    Portas Abertas...
    ----------------\n
    -Angulação limte de 80º alcançada em ambos os lados-
    -Operação abertura de portas bem sucessida-"""

    if senha1 == senha_usuario:



        print("acesso liberado\n")
        print("Sr(a), Por favor, em qual porta deseja realizar a operação?")

        # variável que vai guardar qual porta vai ser realizada a operação.
        qual_porta = str(input("esquerda ou direita?"))

        # variável que vai guardar se a porta é dianteira ou traseira
        locdoor = str(input("informe se a porta é a dianteira ou traseira"))

        if qual_porta == "esquerda" or " direita":
            if locdoor == "dianteira" or "traseira":
                print("Porta identificada.")

            x = input("A Porta encontra-se aberta ou fechada?")
            if x == "fechada":
                print("Deseja abrir-la?")
                y = input("y or n")

                if y == "y":
                    print(abertura_um)

                elif y == "n":
                    print("Obrigado por Utilizar a IA")
                    print("Finalizando a operação")

            elif x == "aberta":
                print("Deseja fechar-la?")

            # valor de positivo ou negativo, para continuação ou não da operação
            z = input("y o r n")

            if z == "y":
                print(fechamento)

            elif z == "n":
                print("Mantendo porta aberta...")

            else:
                print("OPÇÃO INVALIDA")
                print("Por Favor utilize outra opção...")

        # ----- 2 portas ---------

        if qual_porta == "esquerda e direita":
            if locdoor == "dianteira" or "traseira":
                print("Porta identificada.")

            x = input("A Porta encontra-se aberta ou fechada?")
            if x == "fechada":
                print("Deseja abrir-la?")
                y = input("y or n")

                if y == "y":
                    print(abertura_dois)

                elif y == "n":
                    print("Obrigado por Utilizar a IA")
                    print("Finalizando a operação")

            elif x == "aberta":
                print("Deseja fechar-la?")

            # valor de positivo ou negativo, para continuação ou não da operação
            z = input("y o r n")

            if z == "y":
                print(fechamento)

            elif z == "n":
                print("Mantendo porta aberta...")

            else:
                print("OPÇÃO INVALIDA")
                print("Por Favor utilize outra opção...")

        # porta malas

        if qual_porta == "porta_malas":
            x = input("O Porta-Malas encontra-se aberto ou fechado?")
            if x == "fechada":
                print("Deseja abrir-la?")
                y = input("y or n")

                if y == "y":
                    print("Abrindo Porta...")
                    print("----------------\n")
                    print(" Porta Aberta...")
                    print("----------------\n")

                    # Especificando a abertura do porta malas que alcança uma angulação maior

                    print("-Angulação limte de 90º alcançada-\n")
                    print("-Operação abertura de portas sucessida-")

                elif y == "n":
                    print("Obrigado por Utilizar a IA")
                    print("Finalizando a operação")

            elif x == "aberta":
                print("Deseja fechar-la?")

            # valor de positivo ou negativo, para continuação ou não da operação
            z = input("y o r n")

            if z == "y":
                print(fechamento)
            elif z == "n":
                print("Mantendo porta aberta...")

            else:
                print("OPÇÃO INVALIDA")
                print("Por Favor utilize outra opção...")
