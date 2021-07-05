let selectedItems = []

function handleClick(id) {
    let selectedItem = document.getElementById(id)
    if (!selectedItem.className.includes("active")){
        selectedItems.push(id)
        selectedItem.className +="active"
    }
    else if(selectedItem.className.includes("active")){
        selectedItems = selectedItems.filter(item => {
           return item !== id
        })
        let newClass = selectedItem.className.replace("active","")
        selectedItem.className = newClass
    }
console.log(selectedItems)
}

function deleteItems() {
    $.ajax({
        url : "delete/", // the endpoint
        type : "POST", // http method
        data : {
            the_post : selectedItems.toString(),
            csrfmiddlewaretoken: window.CSRF_TOKEN
        }, // data sent with the post request

        // handle a successful response
        success : function(data) {
            window.location.reload()
            console.log("success");// another sanity check
            console.log(data)

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log("error")
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}