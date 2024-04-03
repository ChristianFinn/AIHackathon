function jsonToObject(jsonString) {
    try {
        var obj = JSON.parse(jsonString);
        return obj;
    } catch (error) {
        console.error("Invalid JSON string", error);
        return null;
    }
}

module.exports = jsonToObject;