#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include <sys/socket.h>
#include <arpa/inet.h>

#define MAX_LEN_MSG	2000

void get_pressure(int *high, int *low) {
	*high = rand() % 20;

	if (*high < 6)
		*high = 6;

	*low = rand() % *high;
	if (*low < (*high / 2))
		*low = *high / 2;
}

// get_pressure_json allocs memory and the user of this function should free it.
char *get_pressure_json() {
	int high, low;
	char *json_data;

	json_data = malloc((strlen("{\"data_name\": \"pressure\", \"value\": \"XX;XX\"}") + 1) * sizeof(char));
	high = 0;
	low = 0;

	get_pressure(&high, &low);
	sprintf(json_data, "{\"data_name\": \"pressure\", \"value\": \"%d;%d\"}", high, low);

	return json_data;
}

int main(int argc, char* argv[]) {
	int socket_desc, client_sock, c, read_size;
	struct sockaddr_in server , client;
	char client_message[MAX_LEN_MSG];
	char *json_data = NULL;
	const char *cmd_error = "{\"error\": \"command not found\"}";
	int high, low;



	// Create socket
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	if (socket_desc == -1)
		printf("Could not create socket\n");

	printf("Socket created\n");

	// Prepare the sockaddr_in structure
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons(8888);

	// Bind
	if (bind(socket_desc, (struct sockaddr *)&server , sizeof(server)) < 0) {
		//print the error message
		perror("bind failed. Error");
		return 1;
	}

	printf("bind done\n");

	// Listen
	listen(socket_desc , 3);

	// Accept and incoming connection
	printf("Waiting for incoming connections...\n");
	c = sizeof(struct sockaddr_in);

	//accept connection from an incoming client
	client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t *)&c);
	if (client_sock < 0) {
		perror("accept failed");
		return 1;
	}
	printf("Connection accepted\n");

	memset(client_message, 0, MAX_LEN_MSG);
	while (1) {
		read_size = recv(client_sock, client_message, MAX_LEN_MSG, 0);
		if (read_size > 0)	{
			//Send the message back to client
			printf("DEBUG: %s\n", client_message);
			if (strncmp(client_message, "get", 3) == 0) {
				json_data = get_pressure_json();
				write(client_sock, json_data, strlen(json_data));

				if (json_data != NULL)
					free(json_data);
			}
			else {
				write(client_sock, cmd_error, strlen(cmd_error));
			}
		} else {
			// Listen
			listen(socket_desc , 3);

			// Accept and incoming connection
			printf("Waiting for incoming connections...\n");
			c = sizeof(struct sockaddr_in);

			//accept connection from an incoming client
			client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t *)&c);
			if (client_sock < 0) {
				perror("accept failed");
				return 1;
			}
			printf("Connection accepted\n");
		}
		memset(client_message, 0, MAX_LEN_MSG);
	}

	return 0;
}
