import hashlib
import re

from database.conexao import supabase


def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def senha_valida(senha):

    if len(senha) < 8:
        return "Mínimo 8 caracteres"

    if not re.search(r"[A-Z]", senha):
        return "Precisa de letra maiúscula"

    if not re.search(r"\d", senha):
        return "Precisa de número"

    return "ok"


def criar_usuario(nome, email, tipo_usuario, senha):

    validar = senha_valida(senha)

    if validar != "ok":
        return validar

    existe = (
        supabase.table("usuarios")
        .select("id")
        .eq("email", email)
        .execute()
    )

    if existe.data:
        return "Email já cadastrado"

    supabase.table("usuarios").insert({
        "nome": nome,
        "email": email,
        "tipo_usuario": tipo_usuario,
        "senha": criptografar_senha(senha)
    }).execute()

    return "ok"


def login(email, senha):

    senha_hash = criptografar_senha(senha)

    res = (
        supabase.table("usuarios")
        .select("*")
        .eq("email", email)
        .eq("senha", senha_hash)
        .execute()
    )

    if res.data:
        return res.data[0]

    return None
