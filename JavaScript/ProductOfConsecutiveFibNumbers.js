function productFib(prod){
    let f1 = 0 , f2 = 1;
    let equal = true;
    while (f1*f2<prod) {
        let temp = f2;
        f2=f1+f2;
        f1=temp;
        if(f1*f2>prod) equal = false;
    }
    return [f1,f2,equal];
}

console.log(productFib(4895));
console.log(productFib(5895));
console.log(productFib(74049690));
console.log(productFib(84049690));
console.log(productFib(193864606));
console.log(productFib(447577));
console.log(productFib(602070));