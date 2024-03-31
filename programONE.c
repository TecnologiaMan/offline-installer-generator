#include <stdio.h>
#include <stdlib.h>
#include "install.h"

int main(void){
	char buffer[1024];
	
	snprintf(buffer, sizeof(buffer), "");	

	install(1);
	
	FILE *open = fopen(buffer, "r");

	if(open == NULL){
		return 1;
	}else{
		fclose(open);
		if(system(buffer) == 0){
			
		}	
	}
	
}

