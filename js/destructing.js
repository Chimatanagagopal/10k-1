const person = {
    name: "John Doe",
    age: 30,
    address: {
        city: "New York",
        country: "USA"
    },
    hobbies: ["Reading", "Traveling"]
};
let { name: fullname, age, address: { city }, country = "Unknown", hobbies } = person
console.log(fullname, age, city)
let [a, ,] = hobbies
let firstHobby = a
console.log(firstHobby)

//task-2//
const fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple"];
let [s, b, ...c] = fruits
let arr = [s , b];
[b , s] = arr;
console.log(s, b)




//task-3
function sumNumbers(...k) {
    console.log(k.reduce((sum, next) => sum + next))
}
sumNumbers(1, 2, 3, 4)

//Task-4
const user = { name: "Alice", age: 25 };
const job = { title: "Developer", company: "TechCorp" };
// let{...s1}=user
// let{...s2}=job
let userProfile = { ...user, ...job, experience: "2 years" }
console.log(userProfile)

//Task-5
const numbers = [1, 2, 3, 4, 5];
let copy1 = [...numbers]
copy1[0] = 0
copy1[copy1.length - 1] = 6
console.log(numbers)
console.log(copy1)




