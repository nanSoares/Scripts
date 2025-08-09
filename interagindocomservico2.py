#!/usr/bin/python3
import telnetlib

def main():
    ip = input("Digite o IP: ")
    porta = 23

    try:
        tn = telnetlib.Telnet(ip, porta)
        banner = tn.read_until(b"\n", timeout=5)
        print(f"Recebido (banner): {banner.decode('utf-8', errors='ignore')}")

        print("Enviando Senha")
        tn.write(b"PASS OLA#\r\n")
        
        response = tn.read_until(b"\n", timeout=5)
        print(f"Recebido (resposta): {response.decode('utf-8', errors='ignore')}")

    except Exception as err:
        print(f"Erro ao conectar: {err}")
    finally:
        tn.close()

if __name__ == "__main__":
    main()
