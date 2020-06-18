// item constructor
function Item(name, price) {
  // item name
  this.name = name;
  // convert string to float
  this.price = parseFloat(price);
}

// event response for add2Cart button
function putInCart(event) {
  // get button element from event
  let btn = event.target;

  // now get dataset attribute from button element
  let data = btn.dataset;

  // now generate new item using item name and price
  const item = new Item(data.name, data.price);

  // check if item is already in hash map data structure
  if (!cart[item.name]) {
    // add item temp cart
    cart[item.name] = item.price;

    // and update storage
    localStorage.setItem('cart', JSON.stringify(cart));
  }
}

function rmFromCart(event) {
  // get button element from event
  let btn = event.target;

  // now get dataset attribute from button element
  let data = btn.dataset;

  // check if item is already in hash map data structure
  delete cart[data.name]

  // update storage
  localStorage.setItem('cart', JSON.stringify(cart));

  // get parent of parent of button element
  let grandparent = btn.parentElement.parentElement;

  // delete grandparent
  grandparent.remove();
}

function setupAddBtn() {
  // get all add to cart buttons
  var buttons = document.querySelectorAll('.add2Cart');

  // add event listeners for clicks using => arrow functions
  buttons.forEach((button)=>{
    button.addEventListener('click', putInCart, false);
  });
}

function setupDelBtn() {
  // get all add to cart buttons
  var buttons = document.querySelectorAll('.rmItem');

  // add event listeners for clicks using => arrow functions
  buttons.forEach((button)=>{
    button.addEventListener('click', rmFromCart, false);
  });
}

// check to see if cart exists and parse to JSON
let cart = JSON.parse(localStorage.getItem('cart'));

// if cart is null
if (!cart) {
  // create new cart, basically a JSON dictionary
  cart = {};

  // store cart
  localStorage.setItem('cart', JSON.stringify(cart));
}
