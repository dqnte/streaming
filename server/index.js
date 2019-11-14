const path = require('path');
const express = require('express');
const morgan = require('morgan');
const fs = require('fs');
const PORT = process.env.PORT || 8080;
const app = express();

module.exports = app;

app.use(morgan('dev'));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, '..', 'public')));

app.get('/stream', (req, res, next) => {
  try {
    const d = new Date(); // get time stamp

    // get chunk of file
    const file = fs.readFileSync(path.join(__dirname, 'wp4144054.jpg'));
    res.set('stamp', [d.getTime()]);
    res.send(file);
  } catch (err) {
    next(err);
  }
});

app.get('/', (err, req, res, next) => {
  res.status(500).send(err);
});

app.listen(PORT, () => {
  console.log(`
    
    App is listening on port ${PORT}

    `);
});
