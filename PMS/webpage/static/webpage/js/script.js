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





//let wb = XLSX.utils.table_to_book(document.querySelector('#projects'),{sheet:"Sheet JS"});
//
//let wbout = XLSX.write(wb, {booktype: 'xlsx', bookSST: true, type: 'binary'});
//
//function s2ab(s) {
//              let buf = new ArrayBuffer(s.length);
//              let view = new Uint8Array(buf);
//              for (var i=0; i<s.length; i++) view[i] = s.charCodeAt(i) & 0xFF;
//              return buf;
//            }

//document.querySelector('#download').addEventListener('click', ()=>{
//    saveAs(new Blob([s2ab(wbout)],{type:"application/octet-stream"}), 'test.xlsx');
//})





document.querySelector('#allCheck').addEventListener('click', (event)=>{
    let table = document.querySelector('#projects');
    let checkboxes = document.querySelectorAll('.checkboxes');

    if(event.target.checked){
        checkboxes.forEach((checkbox)=>{
            checkbox.checked = true;
        })
    }
    else{
        checkboxes.forEach((checkbox)=>{
            checkbox.checked = false;
        })
    }
})


document.querySelector('#download').addEventListener('click', ()=>{
    

    let table = document.querySelector('#projects');


    let temp = table.cloneNode(true);


     function removeCheckboxes(tbale){
         let checkboxes = tbale.querySelectorAll('.checkbox');
         for(let c = 0; c<checkboxes.length; c++){
             checkboxes[c].remove()
         }
     }

     function removeCheckcedRaws(originalTable, TempTable){
         let checkboxes = originalTable.querySelectorAll('.form-check-input');
         let trs = temp.querySelectorAll('tr');
         let ids = [];

         for(let c=0; c<checkboxes.length; c++){
             if(checkboxes[c].checked){
                 ids.push(c);
             }
         }
         for( let d=0; d<trs.length; d++){
             for(let i=0; i<ids.length; i++){
                 if(!ids.includes(d) && d!=0){
                     trs[d].remove();
                 }
             }
         }
         let id_el = temp.querySelectorAll('.order');
         for(i=0; i<id_el.length; i++){
             id_el[i].innerText = i+1;
         }
     }


     removeCheckcedRaws(table,temp);
     removeCheckboxes(temp)

     let  title = document.querySelector('.cat_active').innerText;


    
     let wb = XLSX.utils.table_to_book(temp,{sheet:"Sheet JS"});
 
     let wbout = XLSX.write(wb, {booktype: 'xlsx', bookSST: true, type: 'binary'});
 
     XLSX.writeFile(wb, `${title}.xlsx`);
})