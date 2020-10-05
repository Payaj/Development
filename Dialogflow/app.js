////////////////////////////////////////////only modify the code below if required (update the credentials/ connection info)///////////////////////////////
'use strict';
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

var https = require('https');
var request = require('request');
var fetch = require('fetch');
const axios = require('axios');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');


// initialize DB connection
const admin = require('firebase-admin');
var serviceAccount = require("./XXXX-firebase-adminsdk-l5rib-XXXX.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://XXXX.firebaseio.com/',
});

process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
var t = 1;

//////////////////////////////////////make changes from here//////////////////////////////////

// Copy paste all of your functions here (from fulfillment of your dialogbox). To provide more specific answers you can use any of your product's or third party Rest API.
// For example you can use google api inside a function.
// You can also save user's questions in a database.

function WebhookProcessing(req, res) {
    const agent = new WebhookClient({request: req, response: res});
    console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
    console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
  
    function welcome(agent) {
    const Request1 = agent.parameters.Request1;
    admin.database().ref('userInfo').child(t).set({Request1:Request1});
  }
 
  function fallback(agent) {
    agent.add(`I didn't understand`);
    agent.add(`I'm sorry, can you try again?`);
  }
  
  //save customerrequest1(valuation/agent)  
  function Agent(agent){
    const CustomerRequest1 = agent.parameters.CustomerRequest1;
    admin.database().ref('userInfo').child(t).update({CustomerRequest1:CustomerRequest1});
  }
 
  //Below example shows, how you can use get request with a rest api (here google api) to return the result. It also shows how you can save the results in the db.
  function Address(agent){
    var result='';
    const CustomerRequest2 = agent.parameters.CustomerRequest2;
    const Address = agent.parameters.Address;
    admin.database().ref('userInfo').child(t).update({CustomerRequest2:CustomerRequest2,Address:Address});
    var api = `https://maps.googleapis.com/maps/api/geocode/json?address=${Address}&key=XXXX`;
    return axios.get(api)
    .then((result) =>{
      agent.add(`Here is the latitude and longitude of your address: ` + result.data.results[0].geometry.location.lat + `, ` +result.data.results[0].geometry.location.lng);
      let ga = {'name':'googleadd','parameters':{'googleadd':result.data.results[0].formatted_address, 'lat':result.data.results[0].geometry.location.lat, 'long':result.data.results[0].geometry.location.lng}};
       agent.setContext(ga);
       //console.log(result.data.results[0]);
      
    });
  }
  
  // // Uncomment and edit to make your own Google Assistant intent handler
  // // uncomment `intentMap.set('your intent name here', googleAssistantHandler);`
  // // below to get this function to be run when a Dialogflow intent is matched
  // function googleAssistantHandler(agent) {
  //   let conv = agent.conv(); // Get Actions on Google library conv instance
  //   conv.ask('Hello from the Actions on Google client library!') // Use Actions on Google library
  //   agent.add(conv); // Add Actions on Google library responses to your agent's response
  // }
  // // See https://github.com/dialogflow/dialogflow-fulfillment-nodejs/tree/master/samples/actions-on-google
  // // for a complete Dialogflow fulfillment library Actions on Google client library v2 integration sample

  // Run the proper function handler based on the matched Dialogflow intent name
  let intentMap = new Map();
  //intentMap.set('Welcome', welcome);
  intentMap.set('Default Fallback Intent', fallback);

  intentMap.set('address', Address);

  intentMap.set('Agent', Agent);

  agent.handleRequest(intentMap);
}

//////////////////////////////////////only modify the code below if required///////////////////////////////////////////
// Webhook
app.post('/', function (req, res) {
    console.info(`\n\n>>>>>>> S E R V E R   H I T <<<<<<<`);
    WebhookProcessing(req, res);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
  console.log('Press Ctrl+C to quit.');
});
