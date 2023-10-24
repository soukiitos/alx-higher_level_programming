#!/usr/bin/node
const fs = require('fs');
try {
	const i = fs.readFileSync(process.argv[2], 'utf8');
	console.log(i);
} catch (err_or) {
	console.error(err_or);
}
