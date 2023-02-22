document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.edit_Request_Button').forEach(btn => {

        btn.onclick = function () {
            let id = btn.dataset.song_id;
            btn.style.display = 'none'
            let lyrics_div = document.querySelector(`#song-lyrics-${id}`);
            let curr_lyrics = lyrics_div.querySelector('.lyric-content').innerText;
            lyrics_div.querySelector('.lyric-content').style.display = 'none';
            
            var edit_text = document.createElement("textarea");
            edit_text.style.width = '100%';
            edit_text.setAttribute('form', 'editrequestform');
            edit_text.value = curr_lyrics;
            lyrics_div.appendChild(edit_text);
            var edit_request_form = document.createElement("form");
            edit_request_form.setAttribute('id', 'editrequestform');

            const save_edit = document.createElement('input');
            save_edit.type = 'submit';
            save_edit.value = 'Propose Edit';

            const cancel_edit = document.createElement('button');
            cancel_edit.type = 'button';
            cancel_edit.textContent = 'Cancel';
            cancel_edit.style.color = 'white';
            cancel_edit.style.backgroundColor = '#d9534f';

            edit_request_form.appendChild(save_edit);
            edit_request_form.appendChild(cancel_edit);
            lyrics_div.appendChild(edit_request_form);

            cancel_edit.addEventListener("click", function() {
                edit_request_form.style.display = 'none';
                edit_text.style.display = 'none';
                lyrics_div.querySelector('.lyric-content').style.display = 'block';
                btn.style.display = 'block'
            });

            let last_lyrics = lyrics_div.querySelector('.lyric-content').innerText;

            edit_request_form.onsubmit = (e) => {
                if(last_lyrics === edit_text.value) {
                    alert('No Changes')
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
                            alert('Request Sent!')
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
            let id = btn.dataset.request_id;
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