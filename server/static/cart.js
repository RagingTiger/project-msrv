// setup cart object
const cart = {
  items: new Map(),
  addItem: function(itm) {
    // check if item is already in hash map data structure
    if (!this.items.has(itm.name)) {
      // add item to internal storage
      this.items.set(itm.name, itm.price)
    }
  },
  addMultItem: function() {
    // iterate over special "arguments" object in JavaScript
    for (var i=0; i < arguments.length; i++) {
      // call method for adding item object
      this.addItem(arguments[i]);
    }
  },
  log: function() {
    // print items hash map to console
    console.log(this.items);
  },
  rmItem: function(itm_name) {
    // remove item by name (expects string)
    this.items.delete(itm_name)
  }
};

// create item generating function
function genItem(name, price) {
  // new item
  const item = {    
    name: name,
    price: parseFloat(price)
  };
  // get new item
  return item;
}

// event response for add2Cart button
function putInCart(event) {
  // get button element from event
  let btn = event.target;

  // now get dataset attribute from button element
  let data = btn.dataset;

  // now generate new item using item name and price
  const item = genItem(data.name, data.price)

  // finally add to cart
  cart.addItem(item);
}

// get all add to cart buttons
var buttons = document.querySelectorAll('.add2Cart');

// add event listeners for clicks using => arrow functions
buttons.forEach((button)=>{
  button.addEventListener('click', putInCart, false);
});
