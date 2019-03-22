function setCurrentMenu() {
  currentMenuStyle = 'menu__item--' + document.querySelector(".current-menu").innerHTML;
  menuItems = document.querySelectorAll('.menu__item');
  for(let i = 0; i < menuItems.length; i++) {
    if(menuItems[i].classList.contains(currentMenuStyle)) {
      menuItems[i].classList.toggle('menu__item--active');
    }
  }
  console.log(currentMenuStyle);
  // menuItem = document.querySelectorAll('.menu__item');
  // for(let i = 0; i < menuItem.length; i++)
  // console.log(menuItem.classList.contains('menu__item--projects'))
}

function run() {
  setCurrentMenu();
}

window.onload = run;