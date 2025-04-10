const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  const name = "World";
  res.send(`Hello, ${nmae}!`);
});

app.get("/process-data", async (req, res) => {
  try {
    // Simulate a fake database fetch with a Promise
    const fetchData = () =>
      new Promise((resolve) => {
        setTimeout(() => {
          resolve({ id: 1, value: 42 });
        }, 1000);
      });

    // Fetch data
    const data = await fetchData();

    // Perform a transformation on the data
    const transformedData = {
      id: data.id,
      computedValue: data.value * 2,
      timestamp: new Date().toISOString(),
    };

    // Introduce a subtle runtime bug (typo in variable name)
    res.send(`Processed Data: ${transformedData.computedValu}`);
  } catch (error) {
    res.status(500).send("An error occurred while processing data.");
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
