const ws = new WebSocket('ws://localhost:5800/teste');

ws.addEventListener('open', () => {
  console.log('Connected to WebSocket server');

  // Enviando uma mensagem para o servidor
  ws.send('Hello from client');
});

ws.addEventListener('message', (message) => {
  json_data = JSON.parse(message.data);
  console.log("Message: ", json_data);
  info = json_data["info"]
  console.log("info: ", info);
  value = json_data["value"]
  console.log("value: ", value);
  window.location.href = 'page2/' + info + "/" + value;
});

ws.addEventListener('close', () => {
  console.log('Disconnected from WebSocket server');
});