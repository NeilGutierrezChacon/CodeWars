const Test = {
    assertEquals: function(func,result,debug = true){
        console.log(func == result);
        if(debug){
            console.log(`Result:${func}`);
        }
    }
}
module.exports = Test