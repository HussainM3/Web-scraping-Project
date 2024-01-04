// File to be used for reading phone plans for displaying on website through html file

const { get } = require('http');

// function for reading file and getting phone plan content
function getFileData(){
    const fs = require('fs');

    // explicitly specify 'utf8' the encoding for proper text
    var data = fs.readFileSync('PhonePlans/plans.txt', 'utf8') 

    // array to be used for each plan
    const plansArray = [];

    // split data into carrier sections (remove empty sections)
    var plansSections = data.split('**************************************************');
    plansSections = plansSections.slice(1,plansSections.length - 1);
    
    // loop through each section
    for (var section of plansSections){        
        // getting carrier
        const carrier = section.substring(0, section.indexOf(':')).trim();

        // trimming section to just plans
        section = section.substring(section.indexOf('Name:'));
        
        // splitting each plan into list
        subSections = section.split("\n\n")
        subSections = subSections.slice(0, subSections.length - 1);

        // iterating through each plan and collecting info
        for (var eachPlanInfo of subSections){
            // dictionary for each plan
            plan = {};
            plan.carrier = carrier;
            plan.name = eachPlanInfo.substring(eachPlanInfo.indexOf('Name:') + 6, eachPlanInfo.indexOf('\nPrice:'));
            plan.price = eachPlanInfo.substring(eachPlanInfo.indexOf('Price:') + 7, eachPlanInfo.indexOf('\nDesc'));
            plan.desc = eachPlanInfo.substring(eachPlanInfo.indexOf('Description:') + 13, eachPlanInfo.indexOf('\nFeatures:')).replace(/\n/g, '; ');
            plan.features = eachPlanInfo.substring(eachPlanInfo.indexOf('Features:') + 10, eachPlanInfo.indexOf('\nPerks:')).replace(/\n/g, '; ');
            plan.perks = eachPlanInfo.substring(eachPlanInfo.indexOf('Perks:') + 7).replace(/\n/g, '; ');
            plansArray.push(plan);
        }
    }
    return plansArray;
}
var fileData = getFileData();
console.log(fileData);

