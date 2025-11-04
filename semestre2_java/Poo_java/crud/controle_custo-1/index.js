function validar_campos() {
    const email_ok = email_valido();
    const senha_ok = senha_valida();

    document.getElementById("Recuperar_senha").disabled = !email_ok;
    document.getElementById("Botão_login").disabled = !email_ok || !senha_ok;
}

function email_valido() {
    const email = document.getElementById("email").value;
    if (!email) {
        return false;
    }
    return validar_email(email);
}

function senha_valida() {
    const senha = document.getElementById("senha").value;
    return senha.trim().length > 0;
}

function validar_email(email) {
    return /\S+@\S+\.\S+/.test(email);
}
