const settopic = document.getElementById("settopic")
const gametime = document.getElementById("showgametime")
const gametimeval = document.getElementById("gametime")
const setting = document.getElementById("setting")
const message = document.getElementById("message")

gametime.innerText = "遊戲時長 : " + gametimeval.value + "秒"

document.addEventListener("input", function () {
    gametime.innerText = "遊戲時長 : " + gametimeval.value + "秒"
})




let questions, topic, team, score, resttime

function start() {
    for (let i = 3; i > 0; i--) {
        setTimeout(() => {
            message.innerText = i
        }, 1000);
    }

    

}
const baseip = ""
async function finish_setting() {
    const res = await fetch(`http://${baseip}/newtopic`)
    questions = await res.json()
    
    document.addEventListener("keydown", function(event) {
        message.innerText = "TEAM 1 ARE U READY? /n PRESS ANY KEYS TO START"
        start()
    })
}