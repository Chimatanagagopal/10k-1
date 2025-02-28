//   1   //
function findLarger(num1, num2, callback) {
    console.log(callback(num1, num2) + 5)
}
findLarger(12, 20, callback = (n1, n2) => {
    if (n1 > n2) {
        return n1
    }
    else {
        return n2
    }
})

//2//
function calculate(num1, num2, callback) {
    console.log(callback(num1, num2) * 3)
}
calculate(10, 5, (num1, num2) => {
    if (num1 > num2) {
        return num1 + num2
    }
    else {
        if (num2 > num1) {
            return num1 - num2
        }
        else {
            return 0
        }
    }
})
//3//
function checkEvenOdd(num, callback) {
    if (callback(num) == 'even') {
        return '"even number"'
    }
    else {
        return '"odd number"'
    }

}
console.log(checkEvenOdd(8, (num) => {
    if (num % 2 == 0) {
        return "even"
    }
    else {
        return "odd"
    }
}))

//4//
function checkSign(num, callback) {
    let value = callback(num)
    console.log(`${value} value`)

}
checkSign(-10, (num) => {
    if (num == 0) {
        return "zero"
    }
    else if (num > 0) {
        return "positive"
    }
    else if (num < 0) {
        return "Negative"
    }

})

//5//
function multiplyConditionally(num1, num2, callback) {
    console.log(callback(num1, num2) * 4)
}
multiplyConditionally(4, 6, (num1, num2) => {
    if (num1 > num2) {
        return num1 * num2
    }
    else if (num2 > num1) {
        return num1 + num2
    }
    else {
        return num1
    }
})
