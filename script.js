const tg = window.Telegram.WebApp;
tg.ready();
let noClicks = 0;

const noTexts = [
    "Are you sure? 😳",
    "Really sure? 🥺",
    "Last chance 😭"
];

const question = document.getElementById("question");
const yesBtn = document.getElementById("yesBtn");
const noBtn = document.getElementById("noBtn");

// Нажали YES
yesBtn.addEventListener("click", () => {
    question.innerText = "💖 It's a date!";
    document.querySelector(".buttons").style.display = "none";
});

// Нажали NO
noBtn.addEventListener("click", () => {
    if (noClicks < 3) {
        question.innerText = noTexts[noClicks];

        // увеличиваем кнопку YES
        let scale = 1 + (noClicks + 1) * 0.3;
        yesBtn.style.transform = `scale(${scale})`;

        noClicks++;
    } else {
        question.innerText = "💔 Maybe next year...";
        document.querySelector(".buttons").style.display = "none";
    }
});