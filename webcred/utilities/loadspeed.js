var page = require('webpage').create(),
  system = require('system');

var t = Date.now();
page.open(system.args[1], function(status) {
  if (status !== 'success') {
    console.log('error');
  }
  else {
    console.log(Date.now() - t);
  }
  phantom.exit();
});
