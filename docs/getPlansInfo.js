// File to be used for reading phone plans for displaying on website through html file

console.log('Script is running!'); // debug to ensure function is running

// add event listener to render phone deals when page loads
document.addEventListener('DOMContentLoaded', function() {

    // reading from text file and rendering data
    fetch('plans.txt')
    .then(response => response.text()) //  first then() in the chain is used to process the Response object
    .then(data => {                     // next then() in the chain processes the data extracted from the response
        const phoneDeals = getFileData(data);
        renderPhoneDeals(phoneDeals);
    })
    .catch(error => console.error('Error reading file:', error));


    // function for reading file and getting phone plan content
    function getFileData(data){
        // array to be used for each plan
        var plansArray = [];

        // split data into carrier sections (remove empty sections)
        var plansSections = String(data).split('**************************************************');
        plansSections = plansSections.slice(1,plansSections.length - 1);
        
        // loop through each section
        for (var section of plansSections){        
            // getting carrier
            var carrier = section.substring(0, section.indexOf(':')).trim();

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
        console.log('plansarray:', plansArray);
        return plansArray;
    }

    // function to render phone deals on a HTML page
    function renderPhoneDeals(phoneDeals){
        
        const dealsContainer = document.getElementById('phoneDealsContainer');    
        
        // Clear any deals content previously rendered
        dealsContainer.innerHTML = '';

        // Loop through each deal and render it
        for (let i = 0; i < phoneDeals.length; i++){
            const deal = phoneDeals[i];
            
            // Create div for each deal
            const dealDiv = document.createElement('div');

            // Create separate elements for each piece of information
            const carrierElement = document.createElement('p');
            carrierElement.textContent = `${deal.carrier}`;
            
            const nameElement = document.createElement('p');
            nameElement.textContent = `${deal.name}`;
            
            const priceElement = document.createElement('p');
            priceElement.textContent = `${deal.price}`;
            
            const descElement = document.createElement('p');
            descElement.textContent = `${deal.desc}`;
            
            const featuresElement = document.createElement('p');
            featuresElement.textContent = `${deal.features}`;
            
            const perksElement = document.createElement('p');
            perksElement.textContent = `${deal.perks}`;

            // Append each element to the dealDiv
            dealDiv.appendChild(carrierElement);
            dealDiv.appendChild(nameElement);
            dealDiv.appendChild(priceElement);
            dealDiv.appendChild(descElement);
            dealDiv.appendChild(featuresElement);
            dealDiv.appendChild(perksElement);

            // Append each deal div to deals container
            dealsContainer.appendChild(dealDiv);
        }
        console.log('Content of dealsContainer:', dealsContainer);
    }

});