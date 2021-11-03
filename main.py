#Varbutibu kalkulators
# Autors: X
# Datums: 03.11.2021 V2V

def statistiska():
    #Ja 𝑘 neatkarīgos mēģinājumos notikums 𝐴 iestājas 𝑚 reizes,
    # tad 𝑚 sauc par 𝐴 absolūto biežumu,
    # bet attiecību 𝑊(𝐴)=𝑚/𝑘 par notikuma 𝐴 relatīvo biežumu. Rezultātu izsaki procentos

    #lietotāja vertibu ievade
    # aprekins
    #izvade
    return print("Coming soon!")


def geometriksa():
    #Šis varbūtību aprēķināšanas likums ir spēkā arī telpiskiem ķermeņiem.
    # Pieņemsim, ka telpā doti ģeometriski ķermeņi 𝐺 un 𝑔,
    # pie kam, ķermenis 𝐺 ietver sevī ķermeni 𝑔.
    # Uz labu laimi izvēlas punktu no ķermeņa 𝐺.
    # Varbūtība, ka izvēlētais punkts piederēs arī ķermenim 𝑔, ir 𝑃(𝐴)=𝑉(𝑔)/𝑉(𝐺)

    # lietotāja vertibu ievade
    # aprekins
    # izvade
    return print("Coming soon!")


def klasiska():
    #P(A) = (labvēlīgo notikumu skaits) / (visu notikumu kopskaits)

    # lietotāja vertibu ievade
    # aprekins
    # izvade
    return print("Coming soon!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    choice = input("Kada veida varbutibas aprekini Tev sodien padoma? \n"
                   "Ievadi burtu:\n-K klasiska metode n no n\n"
                   "-G geometriksa varbutiba\n"
                   "-S statiska varbutiba k m reizes\n")
    if choice.lower() == 'k':
        klasiska()
    if choice.lower() == 'g':
        geometriksa()
    if choice.lower() == 's':
        statistiska()
    else:
        exit(0)
