const express = require("express");
const app = express();

// Fake users data
const fakeUsers = [
  { id: 1, name: "John Doe", email: "john.doe@example.com" },
  { id: 2, name: "Jane Smith", email: "jane.smith@example.com" },
  { id: 3, name: "Alice Johnson", email: "alice.johnson@example.com" },
];

// Middleware to parse JSON
app.use(express.json());

// /users route
app.get("/users", (req, res) => {
  res.json(fakeUsers);
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
