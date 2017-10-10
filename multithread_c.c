#include <stdlib.h>
#include <pthread.h>

void *runner(); /* the thread */
#define M 3
#define K 2
#define N 3
#define NUM_THREADS M * N

// serverIP
// socket_set

int main(){
// system("ls");
	int intr=1;
	// system("gcc server/testc.c -o server/testc");
	// system("./server/testc");
	// system("gcc server/2test.c -o server/2test");
	// system("./server/2test");
	pthread_t workers[NUM_THREADS];
	int thread_num;
	thread_num=0;
	int tt=0;
	while(tt<2){
		if (intr==1)
		{
			if(thread_num==0){
				thread_num=1;
			}else{
				thread_num=0;
			}
			pthread_create(&workers[tt], NULL, runner,NULL);
			printf("%d\n",tt);
		}
		tt++;
	}
}
void *runner()
{	
	/* Casting paramater to struct v pointer */
	// if (num==0)
	// {
		printf("0000\n");
		system("gcc server/testc.c -o server/testc");
		system("./server/testc");
		
	// }else{
	// 	system("gcc server/2test.c -o server/2test");
	// 	system("./server/2test");
	// }
}
