// function sayHello(){  
//     console.log("Hello, World!")
// }
// sayHello()
// function displayWarning(){
//     console.log("Warning! System Overload!")
// }
// displayWarning()
// function printStatus(){
//     console.log("System Status: Active")
// }
// printStatus()
// function initialize(){
//     shutdown()
//     console.log("Initialization Complete.")
    
// }
// initialize()
// function shutdown(){
//     console.log("System Shutting Down…")
// }
// function startProcess(){
//     console.log("Process Started.")
//     endProcess()
// }
// function endProcess(){
//     console.log("Process Ended.")
// }
// startProcess()
// function greetUser(){

// }
// function greetUser(name){
//     console.log("Hello,",name)
// }
// greetUser("gopal")

// function calculateSum(a,b){
//     console.log(a+b)
// }
// calculateSum(5,95)

// function beginSession(){
//     endSession()
//     console.log("Session Started")
// }
// beginSession()
// function countDown(){
//     for(var a=5;a>=1;a--){
//         console.log(a)
//     }
// }
// countDown()
// var b=67
// function chechEvenOdd(){
//     if (b%2==0)    {
//         console.log("Even")
//     }
//     else{
//         console.log("Odd") 
//     }

// }
// chechEvenOdd()


// function endSession(){
//     console.log("Session Ended.")
// }
// var e=48
// function gopal(e,b){
//     console.log(e)
//     var e=e+b
//     console.log(e)
// }
// gopal(48,88)
// console.log(undefined+undefined+20+t)
// var t=55
// console.log(t)
// console.log(k)
// var k=66
// console.log(4+7)
// for(var a;a<10;a++){
//     console
// }
// a=2

// function sum(a,b){
//     console.log(a+b)
//     console.log(b())
// }
// sum(10,function(){
//     console.log("hello")
// })

// function first(test){
//     console.log("naga")
//     console.log(test())
//     console.log(second())
// }
// first(second)
// function second(){
//     console.log("gopal")
// }
// function add(a,b){
//     console.log(a+b)
// }
// function sub(a,b){
//     console.log(a-b)
// }
// function mul(a,b){
//     console.log(a*b)
// }
// function cal(v1,v2,opration){
//     opration(v1,v2)
// }
// cal(2,3,sub)

//named functions
// var a=function (a,b){
//     return a+b

// }
// console.log(a(10,20))

// //callback
// var first=function (a,b){
//     console.log("gopal")
//     console.log(a)
//     console.log(b)

// }
// first(10,second)


// function second(){
//     console.log("naga")
// }


// var sum=function(a,b){
//     console.log(a+b)
// }
// var sub=function(a,b){
//     console.log(a-b)
// }
// var mult=function(a,b){
//     console.log(a*b)
// }

// function calucate(v1,v2,opration){
//         opration(2,4)
//     //mult(2,4)
// }
// calucate(2,4,sub)

// var processNumbers=function(a,b,callback){
//     return callback(a,b)
// }

// var callback=function(x,y){
//     return x+y
// }
// callback(5,6)
// console.log(processNumbers(3,4,callback))

// var processNumbers=function(a,b,call){
//     return call(a,b)
// }
// var call= function(x,y){
//     return x+y
// }
// console.log(processNumbers(3,4,call))

// var greet=function(vinay){
//     return vinay("Alice")
// }
// var result=greet(function(name){
//     return "Hello, " + name + "!"
// })
// console.log(result)


// function calculate(a,b,c){
//     return c(a,b)

// }
// var c=calculate(10,5,function(x,y){
//     return x-y
// })
// console.log(c)

// var function_name=function(a,b,c){
//     console.log(c())
// }
// function_name(2,3,one)
// function one(){
//     console.log("hello")
// }



var add=function(a,b){
    return a+b
}
var sub=function(a,b){
    return(a-b)
}
var mult=(a,b)=>a*b

function cal(a,b,callback){
    console.log(callback(a,b))
}
cal(2,3,mult)




