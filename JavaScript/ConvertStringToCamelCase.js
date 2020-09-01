function toCamelCase(str){
   return  str.split("").map((value,i,arr)=>{
        if(arr[i-1]=="-" || arr[i-1]=="_"){
            return value.toUpperCase()
        }
        return value;
    }).filter((value)=> value!='-' && value !='_').join("");
}

console.log(toCamelCase("the-stealth-warrior"));
console.log(toCamelCase("The_Stealth_Warrior"));
console.log(toCamelCase(""));
console.log(toCamelCase("ABC"));

/* END */