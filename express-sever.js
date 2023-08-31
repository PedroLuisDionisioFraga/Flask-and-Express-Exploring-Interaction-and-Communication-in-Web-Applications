const express = require('express');
const cors = require('cors');
const WebSocket = require('ws');

const port_to_express = 5600;
const port_to_web_socket = 5800;

const wss = new WebSocket.Server({port: port_to_web_socket});
const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Rota pra atualiza a letra na tela
app.post('/teste', (req, res) => {
  const data = req.body;
  console.log("data in post: ", data);
  res.send({ "info": data["info"] });
  const json_data = JSON.stringify(data);
  wss.clients.forEach(client => {
    client.send(json_data);
  });
  console.log("Dados enviados....");
});

app.get('/teste', (req, res) => {
  const data = req.body;
  console.log("data in get: ", data)
  res.send({ "info": data["info"] })
});

app.listen(port_to_express, () => {
  console.log(`API running on port ${port_to_express}`);
});

//! Web Sever
wss.on('connection', (ws) => {
  console.log(`Client connected to WebSocket in port ${port_to_web_socket}`);

  ws.on('message', (message) => {
    console.log(`Received message: ${message}`);
  });

  ws.on('close', () => {
    console.log('Client disconnected from WebSocket');
  });
});
