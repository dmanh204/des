#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "des.h"

int main(){
    
    unsigned char* key = (unsigned char*) malloc(8*sizeof(char));
    unsigned char* in = (unsigned char*) malloc(8*sizeof(char));
    unsigned char* out = (unsigned char*) malloc(8*sizeof(char));
    int mode;
    generate_key(key);
    printf("Nhap mode (0= encrypt, 1= decrypt): ");
    scanf("%d",&mode);
    printf("Nhap input 0~255\n");
    for(int i =0; i< 8; i++){
        scanf("%d", &in[i]);
    }

    key_set* ks = (key_set*) malloc(17*sizeof(key_set));

    generate_sub_keys(key, ks);
    process_message(in, out, ks, mode);
    printf("output: ");
    for(int i=0; i<8; i++){
        printf("%c", out[i]);
    }
    free(key);
    free(out);
    free(in);
    free(ks);
    return 0;
}