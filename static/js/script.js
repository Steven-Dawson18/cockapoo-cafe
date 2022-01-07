var clicked = false;

function toggle(){
    if (!clicked){
        clicked = True;
        document.getElementsByClassName('like-btn'). innerText = 'Unlike';
    } else {
        clicked = False;
        document.getElementsByClassName('like-btn'). innerText = 'like';
    }
}