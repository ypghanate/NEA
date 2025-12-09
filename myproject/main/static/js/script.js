const form = document.getElementById("upload-view");
const loading = document.getElementById("loading"); 
const output = document.getElementById("output");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    loading.style.display = "block";
    output.innerHTML = "";

    const formData = new FormData(form);

    try {
        const response = await fetch(form.action || window.location.href, {
            method: "POST",
            headers: {
                "X-CSRFToken": form.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: formData
        });

        const resultText = await response.text();
        output.innerHTML = resultText;

    } catch (error) {
        console.error(error);
        output.innerHTML = "<p style='color:red;'>Something went wrong.</p>";
    } finally {
        loading.style.display = "none";
    }
});
