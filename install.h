#include <stdio.h>
#include <stdlib.h>

#ifndef FILES_H
#define FILES_H

int hex2bin(char c){
    if (c >= '0' && c <= '9')
        return c - '0';
    if (c >= 'a' && c <= 'f')
        return c - 'a' + 10;
    if (c >= 'A' && c <= 'F')
        return c - 'A' + 10;
    return -1;
}

void hexstr2binstr(const char* hexstr, unsigned char* binstr, int len){
    for(int i = 0; i < len; i += 2){
        binstr[i/2] = hex2bin(hexstr[i]) * 16 + hex2bin(hexstr[i+1]);
    }
}

int install(int i){
	char buffer[1024];
	snprintf(buffer, sizeof(buffer), "");
	FILE *open = fopen(buffer, "wb");
	if(i == 1){
		char hex[] = "";
		int len = sizeof(hex) - 1;
		unsigned char bin[len/2];
		hexstr2binstr(hex, bin, len);
		fwrite(bin, 1, sizeof(bin), open);
        	fclose(open);
	}else if(i == 2){
		char hex2[] = "";
		int len = sizeof(hex2) - 1;
		unsigned char bin[len/2];
		hexstr2binstr(hex2, bin, len);
		fwrite(bin, 1, sizeof(bin), open);
        	fclose(open);
	}
}


#endif
