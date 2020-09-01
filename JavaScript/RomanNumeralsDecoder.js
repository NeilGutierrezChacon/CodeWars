const Test = require("./Test");
function solution(roman){
    return roman.split("").map((value)=>{
        switch (value) {
            case 'M':
                return 1000;
            case 'D':
                return 500;
            case 'C':
                return 100;
            case 'L':
                return 50;
            case 'X':
                return 10;
            case 'V':
                return 5;
            case 'I':
                return 1;
            default:
                return 0;
        }
    }).reduce((total,cv,ci,arr)=>{
        if(total>=cv) return total+=cv;
        else return Math.abs(total-=cv);
    });
}
Test.assertEquals(solution('XXI'), 21);
Test.assertEquals(solution('I'), 1);
Test.assertEquals(solution('IV'), 4);
Test.assertEquals(solution('MMVIII'), 2008);
Test.assertEquals(solution('MDCLXVI'), 1666);

/* END */