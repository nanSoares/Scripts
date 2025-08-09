#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(int argc, char *argv[]){
	
	int mysocket;
	int conecta;

	int porta;
	int inicio = 0;
	int final = 65535;
	char *destino;
	destino = argv[1];

	struct sockaddr_in alvo;

	for(porta=inicio;porta<final;porta++){

	mysocket = socket(AF_INET,SOCK_STREAM,0);
	alvo.sin_family = AF_INET;
	alvo.sin_port = htons (porta);
	alvo.sin_addr.s_addr = inet_addr(destino);

	conecta = connect(mysocket, (struct sockaddr *)&alvo, sizeof alvo);

	if(conecta == 0){
		printf("Porta Aberta: %d \n", porta);
		close(mysocket);
		close(conecta);
	
	} else {
		close(mysocket);
		close(conecta);
	}
	}
}
