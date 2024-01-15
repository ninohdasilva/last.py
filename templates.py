class Page() :

    def __init__(self) -> None:
        self.components = []
    
    def create_page(self) :
        self.components = [
            """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="{{ url_for('static', filename='style.css') }}" rel="stylesheet" />
    <title>Double Value SPA</title>
</head>
<body>"""
] + self.components + [
"""
<script>
function doubleValue() {
    var inputValue = document.getElementById('inputValue').value / 100;

    // Send a POST request to the server
    fetch('/calculer_salaire', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'input_value=' + encodeURIComponent(inputValue),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('result').innerHTML = 'Salaire annuel net avant impôts : <br><br> Entre <strong>' + data.result_min + '€ </strong> et <strong>' + data.result_max + '€ </strong>';
        } else {
            document.getElementById('result').innerHTML = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Ajouter un écouteur d'événements pour mettre à jour la valeur du span
document.getElementById('inputValue').addEventListener('input', function() {
    // document.getElementById('sliderValue').textContent = this.value;
    doubleValue(); // Appelle votre fonction pour effectuer l'action souhaitée
});


// Ajoutez ce gestionnaire d'événements pour intercepter la soumission du formulaire
document.getElementById('doubleForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Empêche la soumission par défaut du formulaire
    doubleValue(); // Appelle votre fonction pour effectuer l'action souhaitée
});

</script>

</body>
</html>

"""
        ]

        
    def add_form(self, title, type) :
        self.components.append( f"""
<form id="doubleForm">
    <label for="inputValue">{title}</label>
    <input type="{type}" id="inputValue" name="input_value">
    <button type="button" onclick="doubleValue()">Submit</button>
</form>
<div id="result"> </div>
        """)

    def join_and_write(self, file_path):
        content = " ".join(self.components)
        with open(file_path, "w") as f:
            f.write(content)
