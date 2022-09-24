let order = document.querySelectorAll('.order');
for(i=0; i<order.length; i++){
    order[i].innerText = i+1;
}

let statusFields = document.querySelectorAll('.status');
for(let s=0; s<statusFields.length; s++){
    statusFields[s].addEventListener('dblclick', (event) => {
        
    });
}
