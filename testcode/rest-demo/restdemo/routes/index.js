var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


router.get('/json', function(req, res, next){
  res.json({
    code: 'success',
    msg: {
        id: 1,
        name: 'yeah'
    }
  });
});

/* Post */
router.post('/json', function(req, res, next){
  console.log(req.body);
  var n = req.body.username;
  res.json({
    code: 'success',
    msg: {
      id: 2,
      name: n
    }
  });
});

module.exports = router;
