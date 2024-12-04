
$(document).ready(function() {
    // Enviar o formulário via AJAX
    $('#userForm').on('submit', function(e) {
        e.preventDefault();

        // Captura os valores do formulário
        var nome = $('#nome').val();
        var email = $('#email').val();

        // Faz a requisição AJAX para o servidor Flask
        $.ajax({
            url: 'http://127.0.0.1:5000/usuarios', // URL do endpoint da API
            method: 'POST',
            contentType: 'application/json', // Tipo de conteúdo enviado
            data: JSON.stringify({
                nome: nome,
                email: email
            }), // Dados enviados para a API
            success: function(response) {
                // Mensagem de sucesso

                alert('Usuário cadastrado com sucesso!');
                $('#userForm')[0].reset(); // Limpa o formulário
            },
            error: function(xhr, status, error) {
                // Exibe mensagem de erro
                console.error('Erro ao cadastrar usuário:', error);
                if (xhr.responseJSON && xhr.responseJSON.error) {
                    alert(`Erro: ${xhr.responseJSON.error}`);
                } else {
                    alert('Erro ao cadastrar o usuário. Verifique o servidor.');
                }
            }
        });
    });
});
