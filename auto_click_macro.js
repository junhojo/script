//1. 진행률 확인 후 넘기는 코드
//=======================================
function macro() {
if(parseFloat(document.getElementsByClassName('vjs-progress-holder vjs-slider vjs-slider-horizontal')[0].ariaValueNow) >= 99.9) {
if(document.getElementsByClassName('lectureroom_nav_bar open')[0].innerText.match('학습전'))
next_ScoBtn()
else {
alert('현재차시 끝. 다음 차시를 실행후 macro() 스크립트 함수 다시 실행하세요.')
return
}
}
setTimeout(() => { macro() }, 1000)
}
macro()

//video.currentTime(4000)
//=======================================


//2. 시간지나면 자동으로 눌러주는코드
//=======================================
const customXpath = "/html/body/section/div/div/div[4]/button[9]";
const customButton = document.evaluate(customXpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
const customTotalTime = 1200000; // 전체 시간 (20분)
const customInterval = 30000; // 인터벌 시간 (30초)

let customRemainingTime = customTotalTime;

// 시작 시간 출력
const customStartTime = new Date();
console.log(`시작 시간: ${customStartTime.toLocaleTimeString()}`);

const customTimer = setInterval(() => {
    customRemainingTime -= customInterval;
    console.log(`남은 시간: ${customRemainingTime / 1000}초`);
    
    if (customRemainingTime <= 0) {
        clearInterval(customTimer); // 타이머 정지
        if (customButton) {
            customButton.click(); // 버튼 클릭 실행
            console.log("버튼이 클릭되었습니다."); // 클릭 확인 로그
        } else {
            console.log("버튼을 찾을 수 없습니다.");
        }
    }
}, customInterval);

//=======================================







