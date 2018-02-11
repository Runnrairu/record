#include <stdio.h>
#include <stdlib.h>
char meiro[100][50][51],com[2500];//null文字への配慮
int point[100][2],now[100][3],c;



int getstart(int i,int &h,int &w){//初期位置を取得する関数
	int flg=0,hg,wg;
	for(hg=0;hg<50;hg++){
		for(wg=0;wg<50;wg++){
			if(meiro[i][hg][wg]=='@'){
				flg=1;
				break;
			}
		}
		if(flg==1){
			break;
		}
	}
	h = hg;
	w = wg;
}

void move_yoso(int *h,int *w,int v){//現在地とコマンドを入力したら次の座標の予定が返ってくる関数
	if(v==0){//U
		*h = *h-1 ;
	}else if(v==1){//D
		*h = *h+1;
	}else if(v==2){//L
		*w = *w-1;
	}else{//R
		*w = *w+1;
	}
}

int conv(char s){
	if(s=='U'){//U
		return 0 ;
	}else if(s=='D'){//D
		return 1;
	}else if(s=='L'){//L
		return 2;
	}else{//R
		return 3;
	}
}



int calc(int vec[][4]){//得点
	int i,v,h,w;
	for(i=0;i<100;i++){
		if(now[i][2]==1){
			for(v=0;v<4;v++){//向き
			    h=now[i][0];
		                w=now[i][1];
			    move_yoso(&h,&w,v);
			    if(meiro[i][h][w]=='x'){
				vec[i][v] = c-2500*0.77;//強化学習やっている暇はないので、罠を踏んだ罰則は適当に決定した
			    }else if(meiro[i][h][w]=='o'){
			    	vec[i][v] = 1;
			    }
			
		    }
		}
		
	}
}



char don(void){//貪欲法によって次進む方向を決める
	int vec[100][4]={0},i,hyo[4]={0},max_c,max;
	calc(vec);
	for(i=0;i<100;i++){
		hyo[0] += vec[i][0];//U
		hyo[1] += vec[i][1];//D
		hyo[2] += vec[i][2];//L
		hyo[3] += vec[i][3];//R
	}
	max_c = -1;
	max = -1;
	for(i=0;i<4;i++){
		if(max<hyo[i]){
			max=hyo[i];
			max_c =i;
		}
	}
	if(max_c==0){
		return 'U';
	}else if (max_c==1){
		return 'D';
	}else if(max_c==2){
		return 'L';
	}else{
		return 'R';
	}

	
}

int compare(const void *a,const void *b){
	return ((int*)b)[1]-((int*)a)[1];
}

int main(void) {
	int N,K,H,W,T;
	int i,j;
	scanf("%d %d %d %d %d",&N,&K,&H,&W,&T);
	
	for(i=0;i<100;i++){//迷路名
		for(j=0;j<50;j++){//行のほう
			scanf("%s",meiro[i][j]);
		}
	}
	int h,w;//初期位置の記録
	for(i=0;i<100;i++){
		getstart(i,h,w);
		now[i][0] = h;
		now[i][1] = w;
		now[i][2] = 1;//まだ罠にハマっていないことを表す
	}
	for(c=0;c<2500;c++){
		com[c]=don();
		for(i=0;i<100;i++){
			point[i][0]=i;
			if(now[i][2]==1){
				h = now[i][0];
				w = now[i][1];
				move_yoso(&now[i][0],&now[i][1],conv(com[c]));
				if(meiro[i][now[i][0]][now[i][1]]=='x'){
					now[i][2] = 0;
				}else if(meiro[i][now[i][0]][now[i][1]]=='o'){
					point[i][1] +=1;
					meiro[i][now[i][0]][now[i][1]]='@';
				}else if(meiro[i][now[i][0]][now[i][1]]=='#'){
					now[i][0]=h;
					now[i][1]=w;
				}
				
			}
		}
	}
	qsort(point,100,sizeof(int*),compare);
	printf("%d %d %d %d %d %d %d %d",point[0][0],point[1][0],point[2][0],point[3][0],point[4][0],point[5][0],point[6][0],point[7][0]);
	for(c=0;c<2500;c++){
		printf("%c",com[c]);
	}
	
	return 0;
}
