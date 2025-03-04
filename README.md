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
