const spawn = require('child_process').spawn;
const child = spawn('main.exe');

child.stdin.end('12 34 56');
child.stdout.on('data', data => {
  console.log(data);
});
child.on('close', code => console.log('Exit code: ' + code));
