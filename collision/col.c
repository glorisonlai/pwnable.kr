#include <stdio.h>
#include <string.h>
#include <stdlib.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        unsigned long res=0;
        for(i=0; i<5; i++){
                printf("ip[%d]: %d\n", i, ip[i]);
                res += ip[i];
        }
        printf("%s\n", ip[0]);
        unsigned long diff = hashcode - res;
        printf("diff: %d\n", diff);
        printf("res: %d\n", res);
        printf("hashcode: %d\n", hashcode);
        return res;
}

int main(int argc, char* argv[]){
        char *passcode = "zzzzzzzzzzzzzzzzzzzz"; 

        if(strlen(passcode) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( passcode )){
                system("/bin/cat flag");
                return 0;
        }

        printf("wrong passcode.\n");
        return 1;
}
