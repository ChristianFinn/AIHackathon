const jsonToObject = require('./CoPilot'); // adjust the path as needed

describe('jsonToObject', () => {
    test('converts valid JSON to object', () => {
        const jsonString = '{"name":"John", "age":30, "city":"New York"}';
        const expected = {name: "John", age: 30, city: "New York"};
        expect(jsonToObject(jsonString)).toEqual(expected);
    });

    test('returns null for invalid JSON', () => {
        const jsonString = '{"name":"John", "age":, "city":"New York"}'; // missing value for age
        expect(jsonToObject(jsonString)).toBeNull();
    });

    test('returns null for empty string', () => {
        expect(jsonToObject('')).toBeNull();
    });


    test('returns null for null', () => {
        expect(jsonToObject(null)).toBeNull();
    });

    test('returns expected result for testc case', () => {
        const jsonString = '{"tools":["copilot","cody","whisper","copilot"],"email":"thecookiemonster@cookiejar.com"}';
        const expected = {tools: ["copilot","cody","whisper","copilot"], email: "thecookiemonster@cookiejar.com"};
        expect(jsonToObject(jsonString)).toEqual(expected);
    })
});