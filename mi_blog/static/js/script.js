// HEADER NAVBAR
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
    navLinks.classList.toggle("active");
    hamburger.classList.toggle("open");
});

// Main Slider
const slider = document.querySelector("[data-slider]");
const sliderContainer = document.querySelector("[data-slider-container]");
const sliderPrevBtn = document.querySelector("[data-slider-prev]");
const sliderNextBtn = document.querySelector("[data-slider-next]");

let totalSliderVisibleItems = Number(getComputedStyle(slider).getPropertyValue("--slider-items"));
let totalSlidableItems = sliderContainer.childElementCount - totalSliderVisibleItems;

let currentSlidePos = 0;

const moveSliderItem = () => {
    sliderContainer.style.transform = `translateX(-${sliderContainer.children[currentSlidePos].offsetLeft}px)`;
}

// Next Slide
const slideNext = () => {
    const slideEnd = currentSlidePos >= totalSlidableItems;

    if (slideEnd) {
        currentSlidePos = 0;
    } else {
        currentSlidePos++;
    }

    moveSliderItem();
}

sliderNextBtn.addEventListener("click", slideNext);

// Previous Slide
const slidePrev = () => {
    if (currentSlidePos <= 0) {
        currentSlidePos = totalSlidableItems;
    } else {
        currentSlidePos--;
    }

    moveSliderItem();
}

sliderPrevBtn.addEventListener("click", slidePrev);

// Responsive
window.addEventListener("resize", () => {
    totalSliderVisibleItems = Number(getComputedStyle(slider).getPropertyValue("--slider-items"));
    totalSlidableItems = sliderContainer.childElementCount - totalSliderVisibleItems;

    moveSliderItem();
});