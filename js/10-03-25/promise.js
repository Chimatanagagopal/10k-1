function OrderReceived(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("order Recevied")
        },1000)
    })
}
function PreparingFood(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Preparing food")
        },3000)
    })
}
function Packingfood(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Packing food")
        },2000)
    })
}
function Assigning_a_delivery_person(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Assigning a delivery person")
        })
    })
}
function DeliveringFood(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve(" Delivering Food")
        },4000)
    })
}
OrderReceived()
.then((res)=>{console.log(res);return PreparingFood()})
.then((res)=>{console.log(res);return Packingfood()})
.then((res)=>{console.log(res);return Assigning_a_delivery_person()})
.then((res)=>{console.log(res);return DeliveringFood()})
.catch((err) => {
    console.error("Error:", err);
});


//Movie Ticket Booking
function SelectingSeats(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Selecting seats")
        },2000)
    })
}

function ProcessingPayment(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Processing payment")

        },3000)
    })
}
function GeneratingTicket(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Generating ticket")
        },1000)
    })
}

function Sending_confirmation_email(){
    return new Promise((resolve,reject)=>{
setTimeout(()=>{
    resolve("Sending confirmation email")
})
    },2000)
}

SelectingSeats()
.then((res)=>{console.log(res); return ProcessingPayment()})
.then((res)=>{console.log(res); return GeneratingTicket()})
.then((res)=>{console.log(res); return Sending_confirmation_email()})
.catch((err) => {
    console.error("Error:", err);
});

//Car Service Center
function Car_check_in(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Car check-in complete")

        },1000)
    })
}
function OilChange(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Oil changed")
        },2000)
    })
}
function EngineCheck(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Engine check")
        },3000)
    })
}
function CarWash(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("car wash")
        },2000)
})
}
function Final_quality_check(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Final quality check")
        },2000)
    })
}
Car_check_in()
.then((res)=>{console.log(res);return OilChange()})
.then((res)=>{console.log(res);return EngineCheck()})
.then((res)=>{console.log(res);return CarWash()})
.then((res)=>{console.log(res);return Final_quality_check()})
.catch((err) => {
    console.error("Error:", err);
});

//Laptop Repair Service

function DiagnosingIssue(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Diagnosing issue")
        },3000)
    })
}
function Replacing_faulty_parts(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Replacing faulty parts")
        },3000)
    })
}
function UpdatingSoftware(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Updating software")
        },2000)
    })
}

function Final_testing(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Final testing")
        },2000)
    })
}

function Returning_to_customer(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Returning to customer")
        },1000)
    })
}
DiagnosingIssue()
.then((res)=>{console.log(res); return Replacing_faulty_parts()})
.then((res)=>{console.log(res); return UpdatingSoftware()})
.then((res)=>{console.log(res); return Final_testing()})
.then((res)=>{console.log(res); return Returning_to_customer()})
.catch((err) => {
    console.error("Error:", err);
});

//Online Course Enrollment
function Checking_course_availability(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Checking course availability")
        },1000)
    })
}
function Processing_payment1(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Processing payment")
        },3000)
    })
}
function Generating_enrollment_ID(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Generating enrollment ID")
        },1000)
    })
}
function Sending_course_materials(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Sending course materials")
        },2000)
    })
}

function Granting_access_to_live_classes(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            resolve("Granting access to live classes")
        })
    },2000)
}
Checking_course_availability()
.then((res)=>{console.log(res);return Processing_payment1()})
.then((res) => {console.log(res);return Generating_enrollment_ID();})
.then((res)=>{console.log(res);return Sending_course_materials()})
.then((res)=>{console.log(res);return Granting_access_to_live_classes()})
.catch((err) => {
    console.error("Error:", err);
});