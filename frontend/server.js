const express = require('express.js');
const path = require('path');
const cors = require('flask-cors');
require('dotenv/config');

const server = express();
const port = 3000;

server.use(express.json());
server.use(cores());

server.use(express.static(path.join(__dirname,'/templates')));

server.get('/validate-password', (_, res) => {
    res.sendFile(path.join(dirname, 'templates', 'win.html'));
});

server.listen(port, (error) => {
    if (!error) {
        console.log('Express server running at http://localhost:${port}')
    } else {
        console.log("Error occurred, cannot start Express server: ", error);
    }
});