// File to be used for reading phone plans for displaying on website through html file

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

// function to render phone deals on a HTML page
function renderPhoneDeals(){
    const phoneDeals = getFileData();
    const dealsContainer = document.getElementById('phoneDealsContainer');    
    
    // Clear any deals content previously rendered
    dealsContainer.innerHTML = '';

    // Loop through each deal and render it
    for (let i = 0; i < phoneDeals.length; i++){
        const deal = phoneDeals[i];
        
        // Create div for each deal
        const dealDiv = document.createElement('div');

        // Set text content for each deal
        dealDiv.textContent = `${deal.carrier} ${deal.name} ${deal.price} ${deal.desc} ${deal.features} ${deal.perks}`;

        // Append each deal div to deals container
        dealsContainer.appendChild(dealDiv);
    }
}

// call function to render phone deals when page loads
window.onload = renderPhoneDeals;