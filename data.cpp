#include <stdio.h>
#include <stdlib.h>
int rc[16000][2]={0};
int map[200][200]={0};
int mdif[16000]={0};


int wmin(int n,int m){
	if (n<m){
		return n;
	}else{
		return m;
	}
}

int how_far(int i){ //削減できるコスト
	int before_h,before_w,now_h,now_w,after_h,after_w,h_cost,w_cost;
	before_h=rc[i-1][0];
	before_w=rc[i-1][1];
	now_h=rc[i][0];
	now_w=rc[i][1];
	after_h=rc[i+1][0];
	after_w=rc[i+1][1];
	h_cost=abs(before_h-now_h)+abs(now_h-after_h)-abs(before_h-after_h);
	w_cost = abs(before_w-now_w)+abs(now_w-after_w)-abs(before_w-after_w);
	return h_cost+w_cost;
}


int main(void) {
	int H,W,D,K;
	scanf("%d %d %d %d",&H,&W,&D,&K);
	int i,j,max,maxi,far;
	for(i=0;i<16000;i++){
	    scanf("%d %d",&rc[i][0],&rc[i][1]);
	    map[rc[i][0]][rc[i][1]] = i;
	    if(i>0){
	    	mdif[i-1]=abs(rc[i][0]-rc[i-1][0])+abs(rc[i][1]-rc[i-1][1]);//i-1からiに行くコスト
	    	
	    }
	}
	for(j=0;j<4000;j++){
	    max = 0;
	    maxi=1;
	    for(i=1;i<15999;i++){

	        far=how_far(i);
	        if(far>max){
	        	max=far;
	        	maxi=i;
	        }

	    	
	    }
	    int kkk,lll
	    kkk = rc[maxi][0];
	    rc[maxi][0]= rc[(rc[maxi-1][0]+rc[maxi+1][0])/2][0];
	    lll= rc[maxi][1]
	    rc[maxi][0]=rc[(rc[maxi-1][0]+rc[maxi+1][0])/2][1];
	    rc[maxi][1]=
	    rc[(rc[maxi-1][1]+rc[maxi+1][1])/2][1];

	    printf("%d %d %d %d\n",rc[maxi][0],rc[maxi][1],(rc[maxi-1][0]+rc[maxi+1][0])/2,(rc[maxi-1][1]+rc[maxi+1][1])/2);  
	    }
	return 0;
	
}

	

