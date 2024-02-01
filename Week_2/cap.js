


// let lol  =  [9,8,7,6];
// let lol1 = [1,2];
// let res =  [9,8,7,6][1,2];

// // console.log(lol,lol1);

// for(let i=0; i< 4; i++){
//     res[i] += 1;

//     console.log(res[i])
// }


let lol = [9, 8, 7, 6];
let lol1 = [1, 2];
let res = [];

// Using lol1 to determine which elements from lol to add to res
for (let i = 0; i < lol1.length; i++) {
    console.log(lol[lol1[i]])
    res.push(lol[lol1[i]]);
}

// console.log(res);

// const arr = [1,2,3];

// arr[1] = 4;
// console.log(arr);


const num = 10;
let num1= 10;


final_array = [];

for (let i=0; i<10; i++){
    final_array.push(num - i)
}

console.log(final_array)

// console.log(res)
// console.log(lol)