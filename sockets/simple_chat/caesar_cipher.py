CAESAR_KEY = 3

def cod_cesar(texto, chave):
    result = ""
    for char in texto:
        enc_char = ord(char)+chave
        if enc_char-chave == 10:
            enc_char = 10 #Pular linha. Obs.: Uma bela gambiarra
        elif enc_char > 126:
            enc_char = enc_char-94
        elif enc_char < 32:
            enc_char = enc_char+94
        result += chr(enc_char)
    return result

def decod_cesar(texto, chave):
    return cod_cesar(texto, -chave)