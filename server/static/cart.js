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

  // check if item is already in hash map data structure (global cart object)
  if (!cart[item.name]) {
    // add item temp cart
    cart[item.name] = item.price;

    // and update storage
    localStorage.setItem('cart', JSON.stringify(cart));
  }
}

function cartIsEmpty() {
  // else create div for empty cart
  let empty = document.createElement('div');

  // set div class, and inner HTML on empty div
  empty.className = 'emptyCart';
  empty.innerHTML = 'Empty';

  // finally get cart-view div and append item div
  let cart_view = document.getElementById('cart-view');
  cart_view.appendChild(empty);
}

function rmFromCart(event) {
  // get button element from event
  let btn = event.target;

  // now get dataset attribute from button element
  let data = btn.dataset;

  // check if item is already in hash map data structure (global cart object)
  delete cart[data.name]

  // update storage
  localStorage.setItem('cart', JSON.stringify(cart));

  // get parent of parent of button element (i.e. div with 'item' class)
  let grandparent = btn.parentElement.parentElement;

  // get parent of parent of parent of button element (i.e div id=cart-view)
  let greatgrandparent = btn.parentElement.parentElement.parentElement;

  // delete grandparent
  grandparent.remove();

  // check if all class='item' divs are deleted in div id='cart-view'
  if (greatgrandparent.childElementCount == 0) {
    // show cart is empty
    cartIsEmpty();
  }
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

// check to see if cart exists and parse to global cart object
let cart = JSON.parse(localStorage.getItem('cart'));

// if cart is null
if (!cart) {
  // create new global cart object, basically a JSON dictionary
  cart = {};

  // store cart
  localStorage.setItem('cart', JSON.stringify(cart));
}
