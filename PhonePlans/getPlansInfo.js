// File to be used for reading phone plans for displaying on website through html file

const { get } = require('http');

// function for reading file and getting phone plan content
function getFileData(){
    var fs = require('fs');

    // reads file and saves to variable 
        // first param is file to read
        // second param is call back which contains err (if exists) and data read
    const allData = fs.readFile('/plans.txt', (err, data) => {
        if (err) throw err;
        console.log(data);
    });
}

getFileData();

