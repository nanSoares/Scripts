#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(void){
	
	int mysocket;
	int conecta;

	struct sockaddr_in alvo;

	mysocket = socket(AF_INET,SOCK_STREAM,0);
	alvo.sin_family = AF_INET;
	alvo.sin_port = htons (80);
	alvo.sin_addr.s_addr = inet_addr("172.16.0.1");

	conecta = connect(mysocket, (struct sockaddr *)&alvo, sizeof alvo);

	if(conecta == 0){
		printf("Porta Aberta \n");
		close(mysocket);
		close(conecta);
	
	} else {
		printf("Porta Fechada\n");
	}
}
