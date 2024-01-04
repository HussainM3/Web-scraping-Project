// File to be used for reading phone plans for displaying on website through html file

const { get } = require('http');

// function for reading file and getting phone plan content
function getFileData(){
    const fs = require('fs');

    // explicitly specify 'utf8' the encoding for proper text
    var data = fs.readFileSync('PhonePlans/plans.txt', 'utf8') 

    console.log(data);
}

getFileData();

