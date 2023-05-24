import { createClient, print } from 'redis';

const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server:', err));
client.on('connect', connect => console.log('Redis client connected to the server'));

const setNewSchool = async (schoolName, value) => {
	await client.set(schoolName, value, print)
}

const displaySchoolValue = async (schoolName) => {
	await client.get(schoolName, (error, value) => {
	  if (error) {
	    return console.log(error.message);
	  }
	  console.log(value);
	});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
