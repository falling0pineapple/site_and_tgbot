
    const send_button = document.getElementById("SendPostButton")
    const post_title = document.getElementById("PostTitle")
    const post_author = document.getElementById("PostAuthor")

    send_button.addEventListener("click", async () => {
    if (post_author.value === '') {
    document.getElementById("SiteTitle").textContent = "You should write author"}
    else if (post_title.value === '') {
    document.getElementById("SiteTitle").textContent = "Post should not be empty"}
    else {
    const response = await fetch("http://127.0.0.1:8000/push/post/in/tg/chanel", {

        method: "POST",
        headers: {
        "Content-Type": "application/json"
        },
        body: JSON.stringify({
        title: post_title.value,
        author: post_author.value
        })
        });

    const data = await response.json();

    console.log(data);
    if (response.status === 200){document.getElementById("SiteTitle").textContent = "Sended!"}
    else {document.getElementById("SiteTitle").textContent = "Not sended, try new!"}
}
});

