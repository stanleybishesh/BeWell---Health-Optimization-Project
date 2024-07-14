document.addEventListener('DOMContentLoaded', () => {
    const countdownElement = document.getElementById('countdown');
    const counterElement = document.getElementById('counter');
    const takenBtn = document.getElementById('taken-btn');
    const skipBtn = document.getElementById('skip-btn');
    let timer;
    let waterCount = 0;
    let waterIntervalSeconds = waterInterval * 60;
  
    function startCountdown(duration) {
      let timeRemaining = duration;
      timer = setInterval(() => {
        let minutes = Math.floor(timeRemaining / 60);
        let seconds = timeRemaining % 60;
  
        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;
  
        countdownElement.textContent = `${minutes}:${seconds}`;
  
        if (timeRemaining === 0) {
          clearInterval(timer);
          notifyUser();
          resetTimer();
        } else {
          timeRemaining--;
        }
      }, 1000);
    }
  
    function resetTimer() {
      clearInterval(timer);
      startCountdown(waterIntervalSeconds);
    }
  
    function incrementCounter() {
      waterCount++;
      counterElement.textContent = waterCount;
    }
  
    function notifyUser() {
      if ('Notification' in window && Notification.permission === 'granted') {
        new Notification('Water Reminder', { body: 'Time to drink water!' });
      }
    //    else {
    //     alert('Time is up! Please take your water.');
    //   }
    }
  
    takenBtn.addEventListener('click', () => {
      incrementCounter();
      resetTimer();
    });
  
    skipBtn.addEventListener('click', () => {
      resetTimer();
    });
  
    // Request notification permission and start countdown on permission granted
    if ('Notification' in window && Notification.permission !== 'denied') {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          startCountdown(waterIntervalSeconds);
        } else {
          startCountdown(waterIntervalSeconds);
        }
      });
    } else {
      startCountdown(waterIntervalSeconds);
    }
  });
  



// wake up time and bed time Notification

