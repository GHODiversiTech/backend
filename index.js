const express = require('express'); 
  
const app = express(); 
const PORT = 8080; 
  
const resourceRoute = require("./routes/router");
app.listen(PORT, (error) =>{ 
    if(!error) 
        console.log("Server is Successfully Running, and App is listening on port "+ PORT) 
    else 
        console.log("Error occurred, server can't start", error); 
    } 
); 
app.use("/", resourceRoute);
