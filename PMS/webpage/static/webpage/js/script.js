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
            if(id == 0){
                let url = new URL(`${window.location.href}`);
                url.searchParams.delete(param_name);
                window.location.replace(url);
            }
            else{
                let url = new URL(`${window.location.href}`);
                url.searchParams.set(param_name, id);
                window.location.replace(url);
            }
        })
    }
}

let dropdown_item_managers = document.querySelectorAll('.managers_filter_item');
let dropdown_item_companies = document.querySelectorAll('.companies_filter_item');
urlRedirecter(dropdown_item_companies, 'company');
urlRedirecter(dropdown_item_managers, 'manager');



let wb = XLSX.utils.table_to_book(document.querySelector('#projects'),{sheet:"Sheet JS"});

let wbout = XLSX.write(wb, {booktype: 'xlsx', bookSST: true, type: 'binary'});

function s2ab(s) {
              let buf = new ArrayBuffer(s.length);
              let view = new Uint8Array(buf);
              for (var i=0; i<s.length; i++) view[i] = s.charCodeAt(i) & 0xFF;
              return buf;
            }

document.querySelector('#download').addEventListener('click', ()=>{
    saveAs(new Blob([s2ab(wbout)],{type:"application/octet-stream"}), 'test.xlsx');
})