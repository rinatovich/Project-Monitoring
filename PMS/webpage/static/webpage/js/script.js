let order = document.querySelectorAll('.order');
for(i=0; i<order.length; i++){
    order[i].innerText = i+1;
}

let statusFields = document.querySelectorAll('.status');
for(let s=0; s<statusFields.length; s++){
    statusFields[s].addEventListener('dblclick', (event) => {
        
    });
}


function urlRedirecter(elements,param_name){
    for(let dd =0; dd< elements.length; dd++){
        elements[dd].addEventListener('click',(event)=>{
            event.preventDefault();
            id = event.target.id;
            let url = new URL(`${window.location.href}`);
            url.searchParams.set(param_name, id);
            window.location.replace(url);
        })
    }
}

let dropdown_item_managers = document.querySelectorAll('.managers_filter_item');
urlRedirecter(dropdown_item_managers, 'manager');

