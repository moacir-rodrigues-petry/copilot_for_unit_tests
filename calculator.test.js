describe('Calculator', () => {
    let calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    describe('add', () => {
        it('should add two numbers', () => {
            const result = calculator.add(1, 2);
            expect(result).toBe(3);
        });
    });

    describe('subtract', () => {
        it('should subtract two numbers', () => {
            const result = calculator.subtract(3, 2);
            expect(result).toBe(1);
        });
    });

    describe('multiply', () => {
        it('should multiply two numbers', () => {
            const result = calculator.multiply(2, 3);
            expect(result).toBe(6);
        });
    });

    describe('divide', () => {
        it('should divide two numbers', () => {
            const result = calculator.divide(6, 3);
            expect(result).toBe(2);
        });

        it('should throw an error when dividing by zero', () => {
            expect(() => calculator.divide(6, 0)).toThrow();
        });
    });
});
