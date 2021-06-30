const thumbsDown = document.querySelector(".thumbs-down")

const markCorrect = (event) => {
  event.preventDefault() // disable the link
  const thumbIcon = event.target
  const url = event.currentTarget.href // get the url from the a element in the DOM
  fetch(url, {
    headers: {'X-Requested-With': 'XMLHttpRequest'},
  })
    .then(res => res.json())
    .then(data => {
      // The data can tell me if the card is wrong or not
        console.log("DATA: ", data)
        if (data["correct"]) {
          thumbIcon.classList.replace("fa-solid", "fa-regular")
        } else {
          thumbIcon.classList.replace("fa-regular", "fa-solid")
        }
    } )
}
console.log("Hello World")

correct-link.addEventListener('click', markCorrect)