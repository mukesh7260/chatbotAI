const http = require('http');
const httpProxy = require('http-proxy');

const proxy = httpProxy.createProxyServer({ target: 'http://127.0.0.1:8000/' }); // Change the target to your Django app's address and port

const server = http.createServer(function (req, res) {
  proxy.web(req, res);
});

server.listen(3000); // Change this to the port you want to use for your Node.js server
