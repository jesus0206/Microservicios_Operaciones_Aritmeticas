var express=require('express'); 

var app=express();

app.get('/resta',function(req,res){
    let n1=req.query.n1;
    let n2=req.query.n2;
    let resul=parseInt(n1)-parseInt(n2);
    console.log(resul)
    res.send({resultado:resul});
});

app.listen(8000,function(){
    console.log('servicio de resta de nodejs')
	console.log('aplicacion corriendo en el puerto 8000');
});