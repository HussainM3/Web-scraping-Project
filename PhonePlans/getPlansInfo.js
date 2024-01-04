// File to be used for reading phone plans for displaying on website through html file

const { get } = require('http');

// function for reading file and getting phone plan content
function getFileData(){
    const fs = require('fs');

    // explicitly specify 'utf8' the encoding for proper text
    var data = fs.readFileSync('PhonePlans/plans.txt', 'utf8') 

    // array to be used for each plan
    const plansData = [];

    // split data into carrier sections (remove empty sections)
    var plansSections = data.split('**************************************************');
    plansSections = plansSections.slice(1,plansSections.length - 1);
    
    
    console.log(plansSections + "TESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST");
}

getFileData();

