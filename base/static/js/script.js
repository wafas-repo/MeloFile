document.addEventListener('DOMContentLoaded', function() {

    startTab()

    document.querySelectorAll('.edit_Request_Button').forEach(btn => {

        btn.onclick = function () {
            let id = btn.dataset.song_id;
            btn.style.display = 'none'
            let lyrics_div = document.querySelector(`#song-lyrics-${id}`);
            let curr_lyrics = lyrics_div.querySelector('.lyric-content').innerText;
            lyrics_div.querySelector('.lyric-content').style.display = 'none';
            
            var edit_text = document.createElement("textarea");
            //edit_text.style.width = '100%';
            edit_text.setAttribute('form', 'editrequestform');
            edit_text.classList.add('editTextArea');
            edit_text.value = curr_lyrics;
            lyrics_div.appendChild(edit_text);
            var edit_request_form = document.createElement("form");
            edit_request_form.setAttribute('id', 'editrequestform');
            edit_request_form.classList.add('song-page-btns');

            const save_edit = document.createElement('input');
            save_edit.type = 'submit';
            save_edit.value = 'Propose Edit';

            const cancel_edit = document.createElement('button');
            cancel_edit.type = 'button';
            cancel_edit.textContent = 'Cancel';
            cancel_edit.style.color = 'white';
            cancel_edit.style.backgroundColor = '#5ba7c2';

            edit_request_form.appendChild(save_edit);
            edit_request_form.appendChild(cancel_edit);
            lyrics_div.appendChild(edit_request_form);

            cancel_edit.addEventListener("click", function() {
                edit_request_form.style.display = 'none';
                edit_text.style.display = 'none';
                lyrics_div.querySelector('.lyric-content').style.display = 'block';
                btn.style.display = 'block'
            });

            let str = document.querySelector('.lyric-content').innerHTML;
            var last_lyrics = str.replaceAll("<p>", "")
                            .replaceAll("</p>", "")
                            .replaceAll("<br>", '\n');

            console.log(last_lyrics)
            edit_request_form.onsubmit = (e) => {  
                if(last_lyrics == edit_text.value) {
                    alert('No changes detected')
                    e.preventDefault();
                } else {
                    fetch('/edit-request/' + id, {
                        method: 'PUT',
                        body: JSON.stringify({
                            edited_content: edit_text.value
                        })
                    })
                    .then(result => {
                        if (result.error) {
                            console.log(`Error editing post: ${result.error}`);
                        } else {
                            edit_request_form.style.display = 'none';
                            edit_text.style.display = 'none';
                            lyrics_div.querySelector('.lyric-content').style.display = 'block';
                            btn.style.display = 'block'
                        }
                    })
                }
                
            }
        }

    })

    document.querySelectorAll('.edit_Approve_Button').forEach(btn => {

        btn.onclick = function () {
            console.log('clicked')
            let id = btn.dataset.request_id;
            console.log(id)
            content = document.querySelector('#post').innerHTML

            fetch('/approve-request/' + id, {
                method: 'PUT',
                body: JSON.stringify({
                    content: content
                })
            })
            .then(result => {
                if (result.error) {
                    console.log(`Error approving request: ${result.error}`);
                } else {
                    alert('Request Sent!')       
                }
            })
        } 
        
    })
    

});

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

document.querySelectorAll('.edit-song-link').forEach(btn => {
    btn.addEventListener("click", () => {
       change()
    });
})

function startTab() {

    if (document.getElementById("defaultOpen")) {
        document.getElementById("defaultOpen").click();
    } else {
        
    }
    
}

function profileTabs(evt, tabname) {

    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabname).style.display = "block";
    evt.currentTarget.className += " active";
}



   



