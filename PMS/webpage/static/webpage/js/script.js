let order = document.querySelectorAll('.order');
for(let i=0; i<order.length; i++){
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





let checkboxes = document.querySelector('#allCheck');
if (checkboxes != null){
    checkboxes.addEventListener('click', (event)=>{
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
}


let downloadBtn = document.querySelector('#download');
if(downloadBtn != null){
    downloadBtn.addEventListener('click', ()=>{


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
}


let slug = document.querySelector('input[name="slug"]');
let title = document.querySelector('input[name="title"]');
if (slug != null && title != null){
    title.addEventListener('input', (event)=>{
        function translit(word){
            let answer = '';
            let converter = {
                'а': 'a',    'б': 'b',    'в': 'v',    'г': 'g',    'д': 'd',
                'е': 'e',    'ё': 'e',    'ж': 'zh',   'з': 'z',    'и': 'i',
                'й': 'y',    'к': 'k',    'л': 'l',    'м': 'm',    'н': 'n',
                'о': 'o',    'п': 'p',    'р': 'r',    'с': 's',    'т': 't',
                'у': 'u',    'ф': 'f',    'х': 'h',    'ц': 'c',    'ч': 'ch',
                'ш': 'sh',   'щ': 'sch',  'ь': '',     'ы': 'y',    'ъ': '',
                'э': 'e',    'ю': 'yu',   'я': 'ya',

                'А': 'A',    'Б': 'B',    'В': 'V',    'Г': 'G',    'Д': 'D',
                'Е': 'E',    'Ё': 'E',    'Ж': 'Zh',   'З': 'Z',    'И': 'I',
                'Й': 'Y',    'К': 'K',    'Л': 'L',    'М': 'M',    'Н': 'N',
                'О': 'O',    'П': 'P',    'Р': 'R',    'С': 'S',    'Т': 'T',
                'У': 'U',    'Ф': 'F',    'Х': 'H',    'Ц': 'C',    'Ч': 'Ch',
                'Ш': 'Sh',   'Щ': 'Sch',  'Ь': '',     'Ы': 'Y',    'Ъ': '',
                'Э': 'E',    'Ю': 'Yu',   'Я': 'Ya',   ' ': '-'
            };

            for (let i = 0; i < word.length; ++i ) {
                if (converter[word[i]] == undefined){
                    answer += word[i];
                } else {
                    answer += converter[word[i]];
                }
            }

            return answer.toLowerCase();
        }
        slug.value = translit(event.target.value);
    })
}



let update_container = document.querySelector('.update_container');
if (update_container!=null){
    let dateInput = update_container.querySelector("input[type='date']")
    console.log(dateInput.value)
}
//
// let create_container = document.querySelector('.create_container');
// if (create_container!=null){
//     let dateInput = create_container.querySelector("input[type='date']")
//     dateInput.addEventListener('input',()=>{
//
//     })
// }


// let note_input = document.querySelector('.note_input');
// if(note_input!=null){
//     note_input.addEventListener('submit',(event)=>{
//         event.preventDefault();
//         let data = {
//             'msg': note_input.querySelector('input[type=text]').value
//         };
//
//
//         let xhr = new XMLHttpRequest();
//         xhr.open("POST", document.URL);
//         xhr.setRequestHeader("Accept", "application/json");
//         xhr.setRequestHeader("Content-Type", "application/json");
//
//         xhr.send(data);
//     })
// }