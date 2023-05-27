import { createClient, print } from 'redis';
import express from 'express';
import { promisify } from 'util';

const app = express();

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', connect => console.log('Redis client connected to the server'));

const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4,
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10,
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2,
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5,
    },
];

// async getter and setter for redis client (promisify)
const getter = promisify(client.get).bind(client);

const getItemById = (id) => {
  return listProducts.find((item) => item.id === id);
}

const reserveStockById = (itemId, stock) => {
  client.set(itemId, stock)
}

const getCurrentReservedStockById = async (itemId) => {
  const stock = await getter(itemId);
  return stock;
}

app.get('/list_products', (req, res) => {
    res.send(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId)
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).send({ status: 'Product not found' });
  }

  itemStock = await getCurrentReservedStockById(item.id);

  res.send({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity: itemStock ? parseInt(stock) : item.stock,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
      return res.status(404).send({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(item.id);
  
  if (reservedStock && parseInt(reservedStock) >= item.stock) {
      return res.status(400).send({status: 'Not enough stock available', itemId: item.id});
  }

  await reserveStockById(item.id, reservedStock + 1);
  res.send({ status: 'Reservation confirmed', itemId: item.id });
});



app.listen(1245, () => {
  console.log("app listening on port 1245")
});
