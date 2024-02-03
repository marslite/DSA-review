
// var isValid = function(s){
    // var pars 
// }


// s = '()'
// var c = s.split('');
// console.log(c);

var isValid = function(s) {
    var pars = ['(',')','[',']','{','}']
    stack = []
    var c = s.split('')

    // c.forEach((item) =>{
    //     var idx = pars.indexOf(item) 
    //     if(idx % 2 == 0){
    //         stack.push(item)
    //     }else{
    //         if(stack.length == 0){
    //             return false
    //         }else{
    //             val = stack.pop()
    //             if(val != pars[idx -1]){
    //                 return false
    //             }else{
    //                 return true
    //             }
    //         }
    //     }
    // } )

    for(let i =0; i<s.length; i++){
        var idx = pars.indexOf(s[i]);
        if(idx % 2 == 0){
            stack.push(s[i])
        }else{
            if(stack.length == 0){
                return false;
            }else{
                val = stack.pop()
                if(val != pars[idx -1]){
                    return false;
                }else{
                    return true;
                }
            }
        }
    }

    if(stack.lenght === 0){
        return true
    }else{
        return false
    }
    
};

s = '()'
s1 = '()[]{}'
s2 = '(]'

console.log(isValid(s));
console.log(isValid(s1));
console.log(isValid(s2));