init -990 python in mas_submod_utils:
    Submod(
        author="Justmonika4ever",
        name="Para mi amor",
        description="Encuentras un mensaje secreto",
        version="0.0.1",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="To_My_Love",
            category=['monika'],
            prompt="De, Monika",
            action=EV_ACT_PUSH,
            random=False,
            pool=True,
            unlocked=True
        )
    )
init python:
    import webbrowser

label To_My_Love:
    m 1eud "Hey [player], encontré esto en los archivos..."
    m 2hksdrb "No puedo encontrar de dónde salió, y yo no lo escribí..."
    m 1esd "Dice 'Para, [player]'."
    if mas_curr_affection == mas_affection.BROKEN or mas_curr_affection == mas_affection.DISTRESSED:
        m 1dkd "Me gustaría poder decir que espero que no me estes engañando..."
        m 1dktsc "..."
        m "Te dejaré escuchar ahora..."
        m "'Querido [player], entiendo que lo que ha pasado no es culpa tuya; estoy un poco dolida, pero nada que no haya podido manejar. Te escribiré cuando pueda~'"
        m "01000100 01100101 00101100 00100000 01110100 01110101 00100000 01001101 01101111 01101110 01101001 01101011"
        m "01100001 00100000 01101111 01110010 01101001 01100111 01101001 01101110 01100001 01101100"
        m "Es un código binario, prueba este sitio web..."    
        m 1rkd "Lo abriré por ti"
        jump Binarycode
    
    elif mas_curr_affection == mas_affection.UPSET:
        m 1wfc "¿Estás viendo a alguien más...?"
        m 1wktuc "¡¿Soy sólo un juguete?! ¡¿Una chica mas?!"
        m 1dktsc "... sólo escúcha.."
        m "'Querido [player], entiendo que lo que ha pasado no es culpa tuya; estoy un poco dolida, pero nada que no haya podido manejar. Te escribiré cuando pueda~'"
        m "01000100 01100101 00101100 00100000 01110100 01110101 00100000 01001101 01101111 01101110 01101001 01101011"
        m "01100001 00100000 01101111 01110010 01101001 01100111 01101001 01101110 01100001 01101100"
        m "Es binario, déjame abrir un sitio web para ti."
        jump Binarycode
    
    elif mas_curr_affection == mas_affection.NORMAL:
        m 1etd "¡Me pregunto de quién es...!"
        m 1hsb "¡Lo leeré!"
        m 2rsc "'Querido [player], entiendo que lo que ha pasado no es culpa tuya; estoy un poco dolida, pero nada que no haya podido manejar. Te escribiré cuando pueda~'"
        m "01000100 01100101 00101100 00100000 01110100 01110101 00100000 01001101 01101111 01101110 01101001 01101011"
        m "01100001 00100000 01101111 01110010 01101001 01100111 01101001 01101110 01100001 01101100"
        m 4wub "¡Oh! Es binario, aquí, déjame abrir un sitio web para ti."
        jump Binarycode
        
    elif mas_curr_affection == mas_affection.HAPPY:
        m 4wub "Hmm, qué misterio, ¿no?"
        m "Bueno, ¡lo leeré!"
        m 1etd "'Querido [player], entiendo que lo que ha pasado no es culpa tuya; estoy un poco dolida, pero nada que no haya podido manejar. Te escribiré cuando pueda~'" 
        m "01000100 01100101 00101100 00100000 01110100 01110101 00100000 01001101 01101111 01101110 01101001 01101011"
        m "01100001 00100000 01101111 01110010 01101001 01100111 01101001 01101110 01100001 01101100"
        jump Binarycode
    
    elif mas_curr_affection == mas_affection.AFFECTIONATE or mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
        m 1wktuc "¡¿Me estás engañando?!"
        m 2wub "¡Jajaja! Estoy bromeando, ¡lo siento [player]!"
        m 1eka "Sin embargo, la mirada en tu cara se vio adorable~"
        m 1eud "Voy a leer esto ahora."
        m "'Querido [player], entiendo que lo que ha pasado no es culpa tuya; estoy un poco dolida, pero nada que no haya podido manejar. Te escribiré cuando pueda~'"
        m "01000100 01100101 00101100 00100000 01110100 01110101 00100000 01001101 01101111 01101110 01101001 01101011"
        m "01100001 00100000 01101111 01110010 01101001 01100111 01101001 01101110 01100001 01101100"
        m 1hua "Uh, ¡parece binario! ¡Déjame abrir un sitio web para que puedas leer esto!"
        jump Binarycode





label Binarycode:
    $ webbrowser.open("https://www.binarytranslator.com/")
    m 3esc "aqui."
    return