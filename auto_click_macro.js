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
const MINUTES = 1; // 총 시간 (분 단위)
const CUSTOM_TOTAL_TIME = 1000 * 60 * MINUTES; // 총 시간 (밀리초)
const CUSTOM_INTERVAL = 1000 * 30; // 인터벌 시간 (30초)

let customRemainingTime = CUSTOM_TOTAL_TIME;

// XPath를 통해 버튼 요소를 가져옵니다.
const getCustomButton = () => {
    return document.evaluate(customXpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
};

const customTimer = setInterval(() => {
    const customButton = getCustomButton(); // 매번 버튼을 가져옵니다.

    // 남은 시간 출력
    customRemainingTime -= CUSTOM_INTERVAL;
    // 남은 시간 계산
    const remainingMinutes = Math.floor(customRemainingTime / 1000 / 60); // 남은 분
    const remainingSeconds = Math.floor((customRemainingTime / 1000) % 60); // 남은 초

    console.log(`남은 시간: ${remainingMinutes}분 ${remainingSeconds}초`);

    if (customRemainingTime > 0) {
        // 버튼이 존재하는 경우 클릭합니다.
        if (customButton) {
            customButton.click(); // 버튼 클릭 실행
            console.log("버튼이 클릭되었습니다."); // 클릭 확인 로그
        } else {
            console.log("버튼을 찾을 수 없습니다.");
            clearInterval(customTimer); // 버튼을 찾을 수 없으면 타이머 정지
        }
    } else {
        clearInterval(customTimer); // 시간이 다 되면 타이머 정지
        console.log("정해진 시간이 경과했습니다. 타이머가 정지되었습니다.");
    }
}, CUSTOM_INTERVAL);

// 시작 시간 출력
const customStartTime = new Date();
console.log(`시작 시간: ${customStartTime.toLocaleTimeString()}`);

//=======================================







