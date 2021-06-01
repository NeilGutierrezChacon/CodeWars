function solution(list){
    let resp = '';
    for (let i = 0; i < list.length; i++) {
        let element = list[i];
        let cont = 0;
        resp += `${element}`;
        for (let j = i+1; j < list.length; j++) {
            /* console.log(element+1,'==',list[j]); */
            /* console.log("Cont: ",cont);      */   
            if(element+1 != list[j] || j == list.length-1){
                if(cont >= 2){
                    if(j == list.length-1){
                        resp +=`-${element+1}`;
                        i = j;
                    }else{
                        resp +=`-${element}`;
                        i = j-1;
                    }
                    
                }
                break;
            }else{
                element++;
                cont++;
            }
        }
        if( i!= list.length-1)
            resp += ',';
        
    }
    return resp; 
}

console.log(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]));
console.log(solution([-3,-2,-1,2,10,15,16,18,19,20]));