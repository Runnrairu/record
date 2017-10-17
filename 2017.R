rm(list=ls())
nyuryoku <- function() {
    first <- readline("大見出し\n")
    second <- readline("中見出し\n")
　　　 third<- readline("小見出し（不要なときは「なし」と入力）\n")
    return(list(first,second,third))
}
main <- function(code){
n　<- length(A)
judge <- 0
code[1]<- paste("#",code[1])
code[2]<- paste("##",code[2])
if(code[3]!="なし"){
code[3]<- paste("###",code[3])
} #ifの終わり

n　<- length(A)
for(i in 1:n){ #coden1について解析
 if(A[i]==as.character(code[1][1])){
　　for(j in (i+1):n){
　　　if(A[j]==as.character(code[2][1])){
　　　　if(code[3]=="なし"){
　　　　　for(k in (j+1):n){
　　　　　　if (startsWith(A[k],"## ")){
　　　　　　　judge<-1
　　　　　　　break
       }#3文字判定終わり
　　　　　　else{
　　　　　　　print(A[k],quote=F)
　　　　　　　}#else終わり
　　　　　　}#forなし終わり
　　　　　}#code3なし判定if終わり
　　　　else{ #code3がなしじゃないやつはじめ
　　　　　for(k in (j+1):n){
       if(A[k]==as.character(code[3][1])&&judge==0){
        for(l in (k+1):n){
　　　　　　　 if(startsWith(A[l],"### ")){
　　　　　　　　 judge <- 1
　　　　　　　　 break
　　　　　　　　 }
　　　　　　　 else{
　　　　　　　　 print(A[l],quote=F)
          }
　　　　　　　
         }#forl終わり
　　　　　　　}#ifcode3Ak終わり
　　　　　　　if(judge==1){break}
　　　　　　}#for3print終わり
　　　　　
　　　　　}#code3がなしじゃないやつ終わり
   }#2つめのcode2を解析するif終わり
   if(judge!=0){break}#すでに終わってたらここで抜ける
　 }#2つ目のfor終わり
 }#１つめのif終わり
 if(judge!=0){break}#すでに終わってたらここで抜ける
}#１つめのfor終わり
}#mainの終わり
A <- scan("portfolio.md", what = character(), sep = "\n", blank.lines.skip = F)
main(nyuryoku())
