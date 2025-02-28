// varibles are three types 
// var(es1)
// let(es6)
// const(es6)
// varible syntax
// three ways
//----------------
// varible identifier=value:
// varible identifier:
// varible=CSSFontFeatureValuesRule:
// var a=30
// var b=40
// console.log(c)
// var c=a+b
// console.log(a)
// console.log(b)
// console.log(c)
// // console.log(d)
// var x=undefined
// console.log(x+20)
// var N_66="gopal"
// console.log(N_66)
// z=66
// console.log(z)
// console.log(x);
// var x = 15;
// var y = 1;  
// var y = 2;  
// y = 3;  
// console.log(y)
// var b;
// console.log(b);
// var a = 1;
// {
//     var a = 2;
// }
// console.log(a);
// {
//     var c = 10;
// }
// console.log(c);
// var p;
// console.log(p);
// p = 20;
// var q = 5;  
// var q = 10;  
// console.log(q);
// var r;
// r = 30;
// var r = 50;
// console.log(x);
// var x = 25;
// var t = 10;  
// var t;  
// console.log(t);
// x = 100;  
// var x;  
// console.log(x);
// var z = 1;  
// z = 2;  
// console.log(z);
// var _Xyz12$;
// _Xyz12$ = 45;
// console.log(_Xyz12$);
// var $num_Val = 8;  
// $num_Val = 16;  
// console.log($num_Val);
// console.log(_x_Val12);  
// var _x_Val12 = 27
// var Val_12X$ = 10;  
// Val_12X$ = 20;  
// console.log(Val_12X$);
// console.log(VAL_num);  
// var VAL_num = "Test";  
// var $count = 5;  
// $count = $count + 3;  
// console.log($count);
// var _alpha$ = 50;  
// var _alpha$ = 100;  
// console.log(_alpha$);
// var $$$ = 99;  
// $$$ = 88;  
// console.log($$$);
// var _vA_rX = "Code";  
// console.log(_vA_rX);

// var X_$12; 
// console.log(X_$12);
// X_$12 = 123;
// var VaR_$$ = "Testing";  
// console.log(VaR_$$);
// var 12x$var_ = 100;  
// console.log(12x$var_);
// console.log(a)
// var a=20
// var a=21
// console.log(a)
// var a=23
// console.log(a)
// document.write (a)
// var f=
// console.log(f+30)
// {
//     var b=50
//     console.log(b)
// }
// console.log(b)
// var b=60
// console.log(b)

// function gopal(a,b){
//     // return '23'
//     return a+b+"hgfdfghjop"
// }
// console.log(gopal(20,40))
//data types
//string

//

// var add=(a,b,c)=>
//     console.log(`this is add${a},
//         ${b} opration ${a+b} , 
//         ${a-b},${c()}`)
//         console.log(c(a,b))
// add(3,5,one)
// var one=(a,b)=>
//     console.log(`hello how are you ! ${a}`)

// var str=`Hii hlo, gopal`
// console.log(str.length)
// console.log(str[12]) //length
// console.log(str.toUpperCase())
// console.log(str.toLowerCase())
// var b=str.trim()
// console.log(b.length)
// console.log((str.split("")))
// console.log(str.replace('i','k'))
// console.log(str.includes('hlo gopal'))
// console.log(str.substring(0,6))
// console.log(str.slice(1,6))


// var function_name=(a,b,c)=>{
//     console.log(`hello`)
//     console.log(a+b)
//     console.log(c())

// }
// function_name(2,4,name1)
// function name1(){

// return `this is gopal`
// }


// a=`heLlo`
// console.log(a.toUpperCase())
// console.log(a.toLowerCase())
// console.log(a.split())
// console.log(a.replace('h','H'))
// console.log((a.trim()).length)
// console.log(a.length)
// console.log(a.slice(1,5))
// //named function



// //named function
// function add(a,b){
//     return a+b
// }
// //anonymous function
// var sub=function (a,b){
//     return a-b
// }
// //arrow function//
// var mult=(a,b)=> a*b


// var demo=(a,b,opt)=>{
//     console.log(add(a,b)) //call back//
// }
// demo(2,3,add)


// function sum(a,b,callback1,arrowfun1){
//     console.log(callback1(2,4))
//     arrowfun1("sandhya")
//     var result = a-b
//     console.log(result)
// }    
// // var jum =sum(2,6,function(x,y){return x+y},(name) =>{console.log(name)})
// // console.log(jum)

// sum(2,6,function(x,y){return x+y},(name) =>{console.log(name)})
// // console.log(jum)


//  function add(val, callback) {
//     var res = val + 15;
//     callback(res, true);
// }
// function sub(val, callback) {
//     var res = val - 10;
//     callback(res, true);
// }
// function mul(val, callback) {
//     var res = val * 2;
//     callback(res, true);
// }
// function div(val, callback) {
//     var res = val / 5;
//     callback(res, true);
// }
// add(20, hello)

// var hello=(addRes, status) =>{
//     if (status == true) {
//         sub(addRes, (subRes, status) => {
//             if (status == true) {
//                 mul(subRes, (mulRes, status) => {
//                     if (status == true) {
//                         div(mulRes, (divRes, status) => {
//                             if (status == true) {
//                                 console.log(Final Result : ${divRes});
//                             }
//                             else {
//                                 console.error("Division Failed.");
//                             }
//                         })
//                     } else {
//                         console.error("Multiplication Failed.")
//                     }
//                 })
//             }
//             else {
//                 console.error("Substraction Failed");
//             }
//         })
//     } else {
//         console.error("Addition Failed...")
//     }
// })


// var a=20
// var a=49
// console.log(a)

// let b=20
// b=20
// console.log(b)
  
// const c=20
// console.log(c)
// let a=30
// ++a
// str=`hello
//     jeevvan
//     Jeevan ${a}`
// console.log(str.toLowerCase())

// console.log(str.replace('h','GG'))
// console.log(typeof a)



// function add(a,num){
//     var result=a+10
// }
// var sub=(a,num)=>{
//     var result=a-20
// }
// var mult=function(a,num){
//     var result=a*2
// }
// add(10,fg)
// function fg()

// function add(val,callback){
//     callback(val+20)
// }
// sub=(val,callback)=>{
//     callback(val-2)
// }
// mult=(val,callback)=>{
//     callback(val-30)
// }
// add(4,(hello)=>{
//     console.log(hello)
//     sub(hello,(subref)=>{
//         console.log(subref)
//         mult(subref,(multref)=>{
//             console.log(multref)
//         })
//     })
// })




// function add(val,callback){
//     var result=val+20
//     callback(result,true)
// }

// var sub=function(val,callback){
//     var result=val-10
//     callback(result,)

// }
// sub(15,(sub)=>{console.log(sub)})

// var mult=(val,callback)=>{
//     callback(val*3)
// }

// add(2,(add,status)=>{console.log(add)})

// let x =9999999999999999n;
// console.log(typeof x)
// let y=BigInt(99999999999999999)
// console.log(typeof y)
// let z=BigInt(x*y)
 // console.log(z)
// let na=33
// let ma=3n
// console.log(ma*na)
// let height=Number(prompt(`enter your height(cm)`))
// let weight=Number(prompt(`enter your weight(cm)`))
// const BMI=weight/(height)**2
// console.log(BMI)
// console.log(30+ +'10'+'20')
// console.log('40'**'80')
// a=false
/* if(a){
    console.log(a)
} */



// console.log(5+ +"5")
// console.log("5"+5)
// console.log(10+"5"+false)
// console.log(+50+false)
// console.log(typeof(30*"70"))
// console.log(NaN**0)
// console.log(""-2)



