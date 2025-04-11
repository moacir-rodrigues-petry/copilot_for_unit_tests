const express = require("express");
const app = express();
const port = 3000;

// Fake products data
const products = [
  { id: 1, name: "Product A", price: 10.99 },
  { id: 2, name: "Product B", price: 20.99 },
  { id: 3, name: "Product C", price: 30.99 },
];

// /products endpoint
app.get("/products", (req, res) => {
  res.json(products);
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
