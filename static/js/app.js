var div,button;

window.onload=function(){
    div=document.getElementsByTagName('div');
    button=document.getElementsByTagName('button');
    for(let index = 0; index < button.length; index++) {
        button[index].addEventListener('click',mostrar);
    }
    ocultar();
}
function ocultar(){
    for(let index = 0; index < div.length; index++) {
        div[index].className="hidden_form";        
    }
}
function mostrar(e){
    ocultar();
    let index=e.target.name;
        button[index].addEventListener('click',mostrar);
        div[index].classList.remove("hidden_form");        
}