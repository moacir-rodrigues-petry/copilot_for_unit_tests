# Copilot for Tests

## Run tests

### Javascript

```bash
npm test
```

### Python

```bash
python -m unittest *Test.py
```

## Demo Sequence

1. Ask ide how to run tests. i.e. "@workspace How do I run tests?"

2. Run tests for Javascript.

3. Fix failing test with Copilot's helps. /fix command

4. Completement the calculator tests with Copilot's suggestion (can also be done using Copilot Chat).

5. Create python test for `CatsFileProcessor.py`. /tests command (this should create a test file)

6. Run tests for Python. Ask Copilot if necessary.

7. Add tests in empty file `CatsStorageServiceTest.py` with Copilot's help. /tests command and run tests.

8. Slightly review Code for `CatsPartnerFinder.py` and run tests. (this code has a code smell)

9. Fix code smell by reacotring implementation of `CatsPartnerFinder.py` to extract PersonPreferences class.

10. Update tests after refactoring with Copilot's help (maybe Copilot Edits). Run tests.

# Debugging runtime errors

Install a package to run the code. For example, if you are using express in your code, you need to install it.

`npm install express`

Create a file called `index.js` and add the following code:

```javascript
const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  const name = "World";
  res.send(`Hello, ${nmae}!`);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```

Run the code with `node index.js` and check the output in the browser.

The code will break because of a typo in the variable name `nmae`. Fix the code with Copilot's help. You can also use the `/fix` command to fix the code.

Use the **#terminalSelection** into Copilot Chat and select the code broken by the error. This will help Copilot to understand the context of the code and suggest a fix.
You can also use the `/debug` command to debug the code. This will help you to understand the error and fix it.

After show the fix resolution, go back to the `nmae` incorrect variable.
Use this prompt: `how can I debug this part of the code?`, highlighting the lines below:

```javascript
const name = "World";
res.send(`Hello, ${nmae}!`);
```

Copilot will say to add a breakpoint to the code (in those lines).
Go to **Run and Debug** in the left menu and add in **Watch** the variable `name`.
Then, go to **Run** and **Start Debugging** and access on the browser the [http://localhost:3000](http://localhost:3000).
This will load data on **Variables** side, and also the `name` variable will change the state.
Click on the **Continue** button to see the next state of the `name` variable.

With that, we will see and understand the variable is ok, the state is changing properly (type `name` on **DEBUG CONSOLE** as well to double-check this variable is assigning properly the value "World").

So, when click on the **Continue** button again, the code will break, but now you can see the error is in the `nmae` variable, you will be able to see on the browser and in **DEBUG CONSOLE** throwing the error `ReferenceError: nmae is not defined`.

Debug is done 🎉

---

# Generate a more complex one

`Generate an additional Express route in my Node.js app called /process-data. Inside, simulate async behavior with a fake database fetch (use setTimeout or a Promise), then perform a transformation on the returned data. Introduce a subtle runtime bug (like a typo in a variable name, or misuse of await in a non-async function) that would cause an error at runtime but not be caught at compile time. Keep the function logic realistic and more than 12 lines long.`

This is an interesting one, because sometimes we have a lot of lines of code, like hundreds or even thousands, and it's difficult to find the error.

```javascript
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
```

We can use prompts like these:

`Is there any issue in those lines?`

`Can you find the error in this code?`
